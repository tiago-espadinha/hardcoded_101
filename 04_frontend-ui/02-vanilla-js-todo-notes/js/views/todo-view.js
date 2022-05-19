export class TodoView {
    constructor() {
        this.listElement = document.getElementById('todo-list');
        this.inputElement = document.getElementById('todo-input');
        this.dateElement = document.getElementById('todo-date');
        this.addButton = document.getElementById('add-todo');
        this.countElement = document.getElementById('todo-count');
        this.badgeElement = document.getElementById('todo-badge');
    }

    render(todos) {
        this.listElement.innerHTML = '';
        todos.forEach(todo => {
            const li = this.createTodoElement(todo);
            this.listElement.appendChild(li);
        });
    }

    createTodoElement(todo) {
        const li = document.createElement('li');
        li.className = `todo-item ${todo.completed ? 'completed' : ''}`;
        li.dataset.id = todo.id;
        li.setAttribute('draggable', true);

        const dueDate = todo.dueDate ? `<span class="due-date">${new Date(todo.dueDate).toLocaleDateString()}</span>` : '';

        li.innerHTML = `
            <div class="todo-item-content">
                <input type="checkbox" ${todo.completed ? 'checked' : ''} class="toggle-todo">
                <span class="todo-title">${todo.title}</span>
                ${dueDate}
                <button class="delete-todo">Delete</button>
            </div>
        `;

        return li;
    }

    updateCount(remaining, total) {
        this.countElement.textContent = `${remaining} tasks remaining`;
        this.badgeElement.textContent = total;
    }

    clearInput() {
        this.inputElement.value = '';
        this.dateElement.value = '';
    }
}
