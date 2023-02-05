import React, { useId, forwardRef } from "react";
import styles from "./Input.module.css";

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  hint?: string;
  leftAdornment?: React.ReactNode;
  rightAdornment?: React.ReactNode;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  (
    {
      label,
      error,
      hint,
      leftAdornment,
      rightAdornment,
      disabled,
      required,
      className,
      id,
      ...props
    },
    ref,
  ) => {
    const generatedId = useId();
    const inputId = id || generatedId;
    const errorId = `${inputId}-error`;
    const hintId = `${inputId}-hint`;

    const containerClasses = [
      styles.container,
      disabled ? styles.disabled : "",
      error ? styles.hasError : "",
      className,
    ]
      .filter(Boolean)
      .join(" ");

    const inputWrapperClasses = [
      styles.inputWrapper,
      props.value ? styles.filled : "",
    ]
      .filter(Boolean)
      .join(" ");

    return (
      <div className={containerClasses}>
        {label && (
          <label htmlFor={inputId} className={styles.label}>
            {label}
            {required && <span className={styles.required}>*</span>}
          </label>
        )}
        <div className={inputWrapperClasses}>
          {leftAdornment && (
            <span className={styles.adornment}>{leftAdornment}</span>
          )}
          <input
            id={inputId}
            ref={ref}
            disabled={disabled}
            required={required}
            aria-label={label}
            aria-invalid={!!error}
            aria-describedby={
              [error ? errorId : null, hint ? hintId : null]
                .filter(Boolean)
                .join(" ") || undefined
            }
            className={styles.input}
            {...props}
          />
          {rightAdornment && (
            <span className={styles.adornment}>{rightAdornment}</span>
          )}
        </div>
        {error && (
          <p id={errorId} className={styles.errorMessage} role="alert">
            {error}
          </p>
        )}
        {!error && hint && (
          <p id={hintId} className={styles.hintMessage}>
            {hint}
          </p>
        )}
      </div>
    );
  },
);

Input.displayName = "Input";
