import { TodoList } from '../models/todo.js';
import { TodoView } from '../views/todo-view.js';
import { Store } from '../storage/store.js';

export class AppController {
    constructor() {
        this.todoList = new TodoList(Store.load('luma_todos') || []);
        this.todoView = new TodoView();
        
        this.currentFilter = 'all';
        
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
