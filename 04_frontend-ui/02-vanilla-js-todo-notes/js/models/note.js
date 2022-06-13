import { generateId } from '../utils/uuid.js';

export class Note {
    constructor({ id = generateId(), title = '', body = '', pinned = false, tags = [], createdAt = Date.now(), updatedAt = Date.now() }) {
        this.id = id;
        this.title = title;
        this.body = body;
        this.pinned = pinned;
        this.tags = tags;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }

    update(title, body) {
        this.title = title;
        this.body = body;
        this.updatedAt = Date.now();
    }

    togglePin() {
        this.pinned = !this.pinned;
        this.updatedAt = Date.now();
    }

    addTag(tag) {
        if (!this.tags.includes(tag)) {
            this.tags.push(tag);
            this.updatedAt = Date.now();
        }
    }

    removeTag(tag) {
        this.tags = this.tags.filter(t => t !== tag);
        this.updatedAt = Date.now();
    }
}

export class NoteCollection {
    constructor(notes = []) {
        this.notes = notes.map(n => new Note(n));
    }

    add() {
        const note = new Note({ title: 'New Note', body: '' });
        this.notes.unshift(note);
        return note;
    }

    remove(id) {
        const index = this.notes.findIndex(n => n.id === id);
        if (index !== -1) {
            const removed = this.notes.splice(index, 1)[0];
            return removed;
        }
        return null;
    }

    restore(note) {
        this.notes.unshift(new Note(note));
    }

    getById(id) {
        return this.notes.find(n => n.id === id);
    }

    getFiltered({ search = '', tag = '', sortBy = 'updatedAt' }) {
        let filtered = this.notes.filter(note => {
            const matchesSearch = note.title.toLowerCase().includes(search.toLowerCase()) || 
                                note.body.toLowerCase().includes(search.toLowerCase());
            const matchesTag = tag === '' || note.tags.includes(tag);
            return matchesSearch && matchesTag;
        });

        filtered.sort((a, b) => {
            if (a.pinned !== b.pinned) return b.pinned ? 1 : -1;
            
            if (sortBy === 'title') {
                return a.title.localeCompare(b.title);
            }
            return b[sortBy] - a[sortBy];
        });

        return filtered;
    }

    getAllTags() {
        const tags = new Set();
        this.notes.forEach(note => note.tags.forEach(tag => tags.add(tag)));
        return Array.from(tags).sort();
    }

    toJSON() {
        return this.notes;
    }
}
