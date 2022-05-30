import { TodoList } from '../models/todo.js';
import { NoteCollection } from '../models/note.js';
import { TodoView } from '../views/todo-view.js';
import { NoteView } from '../views/note-view.js';
import { Store } from '../storage/store.js';
import { debounce } from '../utils/debounce.js';

export class AppController {
    constructor() {
        this.todoList = new TodoList(Store.load('luma_todos') || []);
        this.noteCollection = new NoteCollection(Store.load('luma_notes') || []);
        this.settings = Store.load('luma_settings') || { theme: 'light', activePanel: 'todos' };
        
        this.todoView = new TodoView();
        this.noteView = new NoteView();
        
        this.currentFilter = 'all';
        this.noteFilter = { search: '', tag: '', sortBy: 'updatedAt' };
        
        this.init();
    }

    init() {
        this.renderTodos();
        this.renderNotes();
        this.applySettings();
        this.bindEvents();
    }

    applySettings() {
        document.body.className = `${this.settings.theme}-mode`;
        this.switchPanel(this.settings.activePanel);
    }

    renderTodos() {
        const filteredTodos = this.todoList.getFiltered(this.currentFilter);
        this.todoView.render(filteredTodos);
        this.todoView.updateCount(this.todoList.remainingCount, this.todoList.totalCount);
        Store.save('luma_todos', this.todoList.toJSON());
    }

    renderNotes() {
        const filteredNotes = this.noteCollection.getFiltered(this.noteFilter);
        this.noteView.render(filteredNotes);
        this.noteView.updateBadge(this.noteCollection.notes.length);
        Store.save('luma_notes', this.noteCollection.toJSON());
    }

    bindEvents() {
        // Navigation
        document.getElementById('nav-todos').addEventListener('click', () => this.switchPanel('todos'));
        document.getElementById('nav-notes').addEventListener('click', () => this.switchPanel('notes'));

        // Theme
        document.getElementById('theme-toggle').addEventListener('click', () => this.toggleTheme());

        // Todo Events (already implemented, just adding here)
        this.todoView.addButton.addEventListener('click', () => this.handleAddTodo());
        this.todoView.inputElement.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') this.handleAddTodo();
        });
        
        this.todoView.filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                this.currentFilter = btn.dataset.filter;
                this.todoView.setActiveFilter(this.currentFilter);
                this.renderTodos();
            });
        });

        this.todoView.markAllBtn.addEventListener('click', () => {
            this.todoList.markAllComplete();
            this.renderTodos();
        });
        this.todoView.clearCompletedBtn.addEventListener('click', () => {
            this.todoList.clearCompleted();
            this.renderTodos();
        });

        this.todoView.listElement.addEventListener('click', (e) => {
            const id = e.target.closest('.todo-item')?.dataset.id;
            if (!id) return;

            if (e.target.classList.contains('toggle-todo')) {
                this.todoList.toggleTodo(id);
                this.renderTodos();
            } else if (e.target.classList.contains('delete-todo')) {
                if (confirm('Are you sure you want to delete this task?')) {
                    this.todoList.remove(id);
                    this.renderTodos();
                }
            }
        });

        this.todoView.listElement.addEventListener('todo-updated', (e) => {
            const { id, title } = e.detail;
            const todo = this.todoList.getById(id);
            if (todo) {
                todo.update(title, todo.dueDate);
                this.renderTodos();
            }
        });

        // Note Events
        this.noteView.newNoteBtn.addEventListener('click', () => {
            this.noteCollection.add();
            this.renderNotes();
        });

        const debouncedSave = debounce((id, title, body) => {
            const note = this.noteCollection.getById(id);
            if (note) {
                note.update(title, body);
                Store.save('luma_notes', this.noteCollection.toJSON());
            }
        }, 2000);

        this.noteView.gridElement.addEventListener('input', (e) => {
            const id = e.target.closest('.note-card')?.dataset.id;
            if (!id) return;

            const card = e.target.closest('.note-card');
            const title = card.querySelector('.note-title-input').value;
            const body = card.querySelector('.note-body-input').value;
            
            debouncedSave(id, title, body);
        });

        this.bindDragEvents();
    }

    switchPanel(panel) {
        this.settings.activePanel = panel;
        Store.save('luma_settings', this.settings);

        document.getElementById('todo-panel').classList.toggle('hidden', panel !== 'todos');
        document.getElementById('note-panel').classList.toggle('hidden', panel !== 'notes');
        document.getElementById('nav-todos').classList.toggle('active', panel === 'todos');
        document.getElementById('nav-notes').classList.toggle('active', panel === 'notes');
    }

    toggleTheme() {
        this.settings.theme = this.settings.theme === 'light' ? 'dark' : 'light';
        document.body.className = `${this.settings.theme}-mode`;
        Store.save('luma_settings', this.settings);
    }

    // ... handleAddTodo and drag event methods as before ...
    handleAddTodo() {
        const title = this.todoView.inputElement.value.trim();
        const dueDate = this.todoView.dateElement.value;
        if (title) {
            this.todoList.add(title, dueDate);
            this.todoView.clearInput();
            this.renderTodos();
        }
    }

    bindDragEvents() {
        this.todoView.listElement.addEventListener('dragstart', (e) => {
            e.target.classList.add('dragging');
        });

        this.todoView.listElement.addEventListener('dragend', (e) => {
            e.target.classList.remove('dragging');
        });

        this.todoView.listElement.addEventListener('dragover', (e) => {
            e.preventDefault();
            const afterElement = this.getDragAfterElement(this.todoView.listElement, e.clientY);
            const draggable = document.querySelector('.dragging');
            if (afterElement == null) {
                this.todoView.listElement.appendChild(draggable);
            } else {
                this.todoView.listElement.insertBefore(draggable, afterElement);
            }
        });

        this.todoView.listElement.addEventListener('drop', (e) => {
            e.preventDefault();
            const items = Array.from(this.todoView.listElement.querySelectorAll('.todo-item'));
            const newOrderIds = items.map(item => item.dataset.id);
            const newTodos = newOrderIds.map(id => this.todoList.getById(id));
            this.todoList.todos = newTodos;
            this.renderTodos();
        });
    }

    getDragAfterElement(container, y) {
        const draggableElements = [...container.querySelectorAll('.todo-item:not(.dragging)')];
        return draggableElements.reduce((closest, child) => {
            const box = child.getBoundingClientRect();
            const offset = y - box.top - box.height / 2;
            if (offset < 0 && offset > closest.offset) {
                return { offset: offset, element: child };
            } else {
                return closest;
            }
        }, { offset: Number.NEGATIVE_INFINITY }).element;
    }
}
