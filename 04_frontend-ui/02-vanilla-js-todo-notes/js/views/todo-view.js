export class TodoView {
    constructor() {
        this.listElement = document.getElementById('todo-list');
        this.inputElement = document.getElementById('todo-input');
        this.dateElement = document.getElementById('todo-date');
        this.addButton = document.getElementById('add-todo');
        this.countElement = document.getElementById('todo-count');
        this.badgeElement = document.getElementById('todo-badge');
        this.filterButtons = document.querySelectorAll('.filter-btn');
        this.markAllBtn = document.getElementById('mark-all-complete');
        this.clearCompletedBtn = document.getElementById('clear-completed');
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

        // Inline editing
        const titleSpan = li.querySelector('.todo-title');
        titleSpan.addEventListener('dblclick', () => this.enterEditMode(li, todo));

        return li;
    }

    enterEditMode(li, todo) {
        const titleSpan = li.querySelector('.todo-title');
        const input = document.createElement('input');
        input.type = 'text';
        input.className = 'edit-input';
        input.value = todo.title;
        
        const originalContent = li.querySelector('.todo-item-content');
        originalContent.style.display = 'none';
        li.appendChild(input);
        input.focus();

        const exitEdit = (save) => {
            if (save) {
                const newTitle = input.value.trim();
                if (newTitle) {
                    li.dispatchEvent(new CustomEvent('todo-updated', { 
                        detail: { id: todo.id, title: newTitle },
                        bubbles: true 
                    }));
                }
            }
            input.remove();
            originalContent.style.display = 'flex';
        };

        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') exitEdit(true);
            if (e.key === 'Escape') exitEdit(false);
        });
        input.addEventListener('blur', () => exitEdit(true));
    }

    updateCount(remaining, total) {
        this.countElement.textContent = `${remaining} tasks remaining`;
        this.badgeElement.textContent = total;
    }

    setActiveFilter(filter) {
        this.filterButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.filter === filter);
        });
    }

    clearInput() {
        this.inputElement.value = '';
        this.dateElement.value = '';
    }
}
