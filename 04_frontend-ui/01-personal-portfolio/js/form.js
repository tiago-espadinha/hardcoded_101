document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form');
    if (!form) return;
    
    const successMsg = document.getElementById('form-success');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        let isValid = true;
        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const message = document.getElementById('message');

        // Simple validation
        if (name.value.trim() === '') {
            showError('name', 'Name is required');
            isValid = false;
        } else {
            clearError('name');
        }

        if (!/^\S+@\S+\.\S+$/.test(email.value)) {
            showError('email', 'Please enter a valid email');
            isValid = false;
        } else {
            clearError('email');
        }

        if (message.value.trim().length < 20) {
            showError('message', 'Message must be at least 20 characters');
            isValid = false;
        } else {
            clearError('message');
        }

        if (isValid) {
            successMsg.style.display = 'block';
            form.reset();
            setTimeout(() => {
                successMsg.style.display = 'none';
            }, 5000);
        }
    });

    function showError(field, msg) {
        const errorSpan = document.getElementById(`${field}-error`);
        if (errorSpan) errorSpan.textContent = msg;
        const fieldEl = document.getElementById(field);
        if (fieldEl) fieldEl.classList.add('error');
    }

    function clearError(field) {
        const errorSpan = document.getElementById(`${field}-error`);
        if (errorSpan) errorSpan.textContent = '';
        const fieldEl = document.getElementById(field);
        if (fieldEl) fieldEl.classList.remove('error');
    }
});
