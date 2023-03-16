/**
 * Factory for UI components (Button, Modal, Toast)
 */
class UIComponent {
    constructor(props) {
        this.props = props;
    }
    render() {
        throw new Error("Method 'render()' must be implemented.");
    }
}

class Button extends UIComponent {
    render() {
        return `<button class="${this.props.variant}">${this.props.label}</button>`;
    }
}

class Modal extends UIComponent {
    render() {
        return `<div class="modal"><h2>${this.props.title}</h2><p>${this.props.content}</p></div>`;
    }
}

class Toast extends UIComponent {
    render() {
        return `<div class="toast toast-${this.props.type}">${this.props.message}</div>`;
    }
}

class UIComponentFactory {
    static components = {
        'button': Button,
        'modal': Modal,
        'toast': Toast
    };

    static createComponent(type, props) {
        const ComponentClass = UIComponentFactory.components[type.toLowerCase()];
        if (!ComponentClass) {
            throw new Error(`Component type ${type} is not supported.`);
        }
        return new ComponentClass(props);
    }
}

// Example usage
const btn = UIComponentFactory.createComponent('button', { variant: 'primary', label: 'Submit' });
console.log(btn.render());

const toast = UIComponentFactory.createComponent('toast', { type: 'success', message: 'User created!' });
console.log(toast.render());
