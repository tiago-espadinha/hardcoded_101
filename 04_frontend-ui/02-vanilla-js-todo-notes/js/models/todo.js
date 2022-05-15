import { generateId } from '../utils/uuid.js';

export class Todo {
    constructor({ id = generateId(), title, completed = false, dueDate = null, order = 0, createdAt = Date.now(), updatedAt = Date.now() }) {
        this.id = id;
        this.title = title;
        this.completed = completed;
        this.dueDate = dueDate;
        this.order = order;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }

    toggle() {
        this.completed = !this.completed;
        this.updatedAt = Date.now();
    }

    update(title, dueDate) {
        this.title = title;
        this.dueDate = dueDate;
        this.updatedAt = Date.now();
    }
}

export class TodoList {
    constructor(todos = []) {
        this.todos = todos.map(t => new Todo(t));
    }

    add(title, dueDate) {
        const order = this.todos.length > 0 ? Math.max(...this.todos.map(t => t.order)) + 1 : 0;
        const todo = new Todo({ title, dueDate, order });
        this.todos.push(todo);
        return todo;
    }

    remove(id) {
        this.todos = this.todos.filter(t => t.id !== id);
    }

    getById(id) {
        return this.todos.find(t => t.id === id);
    }

    toggleTodo(id) {
        const todo = this.getById(id);
        if (todo) todo.toggle();
    }

    clearCompleted() {
        this.todos = this.todos.filter(t => !t.completed);
    }

    markAllComplete() {
        this.todos.forEach(t => {
            if (!t.completed) t.toggle();
        });
    }

    reorder(startIndex, endIndex) {
        const [removed] = this.todos.splice(startIndex, 1);
        this.todos.splice(endIndex, 0, removed);
        this.todos.forEach((t, index) => {
            t.order = index;
        });
    }

    getFiltered(filter) {
        switch (filter) {
            case 'active':
                return this.todos.filter(t => !t.completed);
            case 'completed':
                return this.todos.filter(t => t.completed);
            default:
                return this.todos;
        }
    }

    get remainingCount() {
        return this.todos.filter(t => !t.completed).length;
    }

    get totalCount() {
        return this.todos.length;
    }

    toJSON() {
        return this.todos;
    }
}
