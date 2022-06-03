import { generateId } from '../utils/uuid.js';

export class Todo {
    constructor(id, title, completed = false, dueDate = '', order = 0, createdAt = new Date().toISOString(), updatedAt = new Date().toISOString()) {
        this.id = id || generateId();
        this.title = title;
        this.completed = completed;
        this.dueDate = dueDate;
        this.order = order;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }

    update(title, dueDate) {
        this.title = title;
        this.dueDate = dueDate;
        this.updatedAt = new Date().toISOString();
    }

    toggle() {
        this.completed = !this.completed;
        this.updatedAt = new Date().toISOString();
    }
}

export class TodoList {
    constructor(todos = []) {
        this.todos = todos.map(t => new Todo(t.id, t.title, t.completed, t.dueDate, t.order, t.createdAt, t.updatedAt));
    }

    add(title, dueDate) {
        const order = this.todos.length;
        const todo = new Todo(null, title, false, dueDate, order);
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

    markAllComplete() {
        const allCompleted = this.todos.every(t => t.completed);
        this.todos.forEach(t => t.completed = !allCompleted);
    }

    clearCompleted() {
        this.todos = this.todos.filter(t => !t.completed);
    }

    reorder(newOrderIds) {
        this.todos = newOrderIds.map(id => this.getById(id)).filter(Boolean);
        this.todos.forEach((todo, index) => {
            todo.order = index;
        });
    }

    getFiltered(filter) {
        let result = [...this.todos];
        if (filter === 'active') result = result.filter(t => !t.completed);
        if (filter === 'completed') result = result.filter(t => t.completed);
        return result.sort((a, b) => a.order - b.order);
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
