import React, { useId, forwardRef, useEffect, useRef } from 'react';
import styles from './Checkbox.module.css';

export interface CheckboxProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'type'> {
  label?: string;
  error?: string;
  indeterminate?: boolean;
}

export const Checkbox = forwardRef<HTMLInputElement, CheckboxProps>(
  ({ label, error, indeterminate, disabled, className, id, ...props }, ref) => {
    const generatedId = useId();
    const checkboxId = id || generatedId;
    const errorId = `${checkboxId}-error`;
    const internalRef = useRef<HTMLInputElement>(null);

    // Merge refs
    useEffect(() => {
      if (typeof ref === 'function') {
        ref(internalRef.current);
      } else if (ref) {
        ref.current = internalRef.current;
      }
    }, [ref]);

    useEffect(() => {
      if (internalRef.current) {
        internalRef.current.indeterminate = !!indeterminate;
      }
    }, [indeterminate]);

    const containerClasses = [
      styles.container,
      disabled ? styles.disabled : '',
      error ? styles.hasError : '',
      className,
    ].filter(Boolean).join(' ');

    return (
      <div className={containerClasses}>
        <label className={styles.checkboxLabel}>
          <div className={styles.inputWrapper}>
            <input
              type="checkbox"
              id={checkboxId}
              ref={internalRef}
              disabled={disabled}
              aria-invalid={!!error}
              aria-describedby={error ? errorId : undefined}
              className={styles.input}
              {...props}
            />
            <div className={styles.checkboxControl}>
              {indeterminate ? (
                <svg viewBox="0 0 24 24" className={styles.icon}>
                  <line x1="5" y1="12" x2="19" y2="12" stroke="currentColor" strokeWidth="3" strokeLinecap="round" />
                </svg>
              ) : (
                <svg viewBox="0 0 24 24" className={styles.icon}>
                  <polyline points="20 6 9 17 4 12" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
                </svg>
              )}
            </div>
          </div>
          {label && <span className={styles.labelText}>{label}</span>}
        </label>
        {error && (
          <p id={errorId} className={styles.errorMessage} role="alert">
            {error}
          </p>
        )}
      </div>
    );
  }
);

Checkbox.displayName = 'Checkbox';
