export class NoteView {
    constructor() {
        this.gridElement = document.getElementById('notes-grid');
        this.searchElement = document.getElementById('note-search');
        this.newNoteBtn = document.getElementById('new-note');
        this.sortElement = document.getElementById('note-sort');
        this.badgeElement = document.getElementById('note-badge');
    }

    render(notes) {
        this.gridElement.innerHTML = '';
        notes.forEach(note => {
            const card = this.createNoteCard(note);
            this.gridElement.appendChild(card);
        });
    }

    createNoteCard(note) {
        const div = document.createElement('div');
        div.className = `note-card ${note.pinned ? 'pinned' : ''}`;
        div.dataset.id = note.id;

        div.innerHTML = `
            <div class="note-card-header">
                <input type="text" class="note-title-input" value="${note.title}" placeholder="Note Title">
                <button class="pin-note" title="Pin note">${note.pinned ? 'Pinned' : 'Pin'}</button>
            </div>
            <textarea class="note-body-input" placeholder="Start typing...">${note.body}</textarea>
            <div class="note-card-footer">
                <div class="tags-container">
                    ${note.tags.map(tag => `<span class="tag">${tag}<button class="remove-tag" data-tag="${tag}">&times;</button></span>`).join('')}
                    <button class="add-tag">+ Tag</button>
                </div>
                <button class="delete-note">Delete</button>
            </div>
        `;

        return div;
    }

    updateBadge(count) {
        this.badgeElement.textContent = count;
    }
}
