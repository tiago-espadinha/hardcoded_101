import { TodoList } from '../models/todo.js';
import { TodoView } from '../views/todo-view.js';
import { Store } from '../storage/store.js';

export class AppController {
    constructor() {
        this.todoList = new TodoList(Store.load('luma_todos') || []);
        this.todoView = new TodoView();
        
        this.currentFilter = 'all';
        this.draggedItem = null;
        
        this.init();
    }

    init() {
        this.renderTodos();
        this.bindEvents();
    }

    renderTodos() {
        const filteredTodos = this.todoList.getFiltered(this.currentFilter);
        this.todoView.render(filteredTodos);
        this.todoView.updateCount(this.todoList.remainingCount, this.todoList.totalCount);
        Store.save('luma_todos', this.todoList.toJSON());
    }

    bindEvents() {
        // Add Todo
        this.todoView.addButton.addEventListener('click', () => this.handleAddTodo());
        this.todoView.inputElement.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') this.handleAddTodo();
        });
        
        // Filters
        this.todoView.filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                this.currentFilter = btn.dataset.filter;
                this.todoView.setActiveFilter(this.currentFilter);
                this.renderTodos();
            });
        });

        // Bulk Actions
        this.todoView.markAllBtn.addEventListener('click', () => {
            this.todoList.markAllComplete();
            this.renderTodos();
        });
        this.todoView.clearCompletedBtn.addEventListener('click', () => {
            this.todoList.clearCompleted();
            this.renderTodos();
        });

        // Delegation for Todo list actions
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

        // Edit listener
        this.todoView.listElement.addEventListener('todo-updated', (e) => {
            const { id, title } = e.detail;
            const todo = this.todoList.getById(id);
            if (todo) {
                todo.update(title, todo.dueDate);
                this.renderTodos();
            }
        });

        // Drag and Drop
        this.bindDragEvents();
    }

    bindDragEvents() {
        this.todoView.listElement.addEventListener('dragstart', (e) => {
            this.draggedItem = e.target.closest('.todo-item');
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
            
            // Reorder the actual list based on DOM order
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

    handleAddTodo() {
        const title = this.todoView.inputElement.value.trim();
        const dueDate = this.todoView.dateElement.value;
        if (title) {
            this.todoList.add(title, dueDate);
            this.todoView.clearInput();
            this.renderTodos();
        }
    }
}
