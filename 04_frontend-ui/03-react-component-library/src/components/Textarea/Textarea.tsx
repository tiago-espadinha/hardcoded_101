import React, { useId, forwardRef } from "react";
import styles from "./Textarea.module.css";

export interface TextareaProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {
  label?: string;
  error?: string;
  hint?: string;
  leftAdornment?: React.ReactNode;
  rightAdornment?: React.ReactNode;
  showCharCount?: boolean;
}

export const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(
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
      rows = 3,
      maxLength,
      showCharCount,
      value,
      ...props
    },
    ref,
  ) => {
    const generatedId = useId();
    const textareaId = id || generatedId;
    const errorId = `${textareaId}-error`;
    const hintId = `${textareaId}-hint`;

    const containerClasses = [
      styles.container,
      disabled ? styles.disabled : "",
      error ? styles.hasError : "",
      className,
    ]
      .filter(Boolean)
      .join(" ");

    const wrapperClasses = [styles.wrapper].filter(Boolean).join(" ");

    const currentValue = (value as string) || "";
    const charCount = currentValue.length;

    return (
      <div className={containerClasses}>
        {label && (
          <label htmlFor={textareaId} className={styles.label}>
            {label}
            {required && <span className={styles.required}>*</span>}
          </label>
        )}
        <div className={wrapperClasses}>
          {leftAdornment && (
            <div className={styles.adornment}>{leftAdornment}</div>
          )}
          <textarea
            id={textareaId}
            ref={ref}
            disabled={disabled}
            required={required}
            maxLength={maxLength}
            rows={rows}
            aria-invalid={!!error}
            aria-describedby={
              [error ? errorId : null, hint ? hintId : null]
                .filter(Boolean)
                .join(" ") || undefined
            }
            className={styles.textarea}
            value={value}
            {...props}
          />
          {rightAdornment && (
            <div className={styles.adornment}>{rightAdornment}</div>
          )}
        </div>
        <div className={styles.footer}>
          <div className={styles.footerLeft}>
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
          {showCharCount && maxLength && (
            <span className={styles.charCount}>
              {charCount}/{maxLength}
            </span>
          )}
        </div>
      </div>
    );
  },
);

Textarea.displayName = "Textarea";
