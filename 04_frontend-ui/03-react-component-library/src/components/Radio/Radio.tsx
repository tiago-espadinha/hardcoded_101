import React, { createContext, useContext, useId } from "react";
import styles from "./Radio.module.css";

interface RadioContextProps {
  name?: string;
  value?: string;
  onChange?: (value: string) => void;
  selectedValue?: string;
}

const RadioContext = createContext<RadioContextProps | undefined>(undefined);

export interface RadioGroupProps {
  name: string;
  value?: string;
  onChange: (value: string) => void;
  children: React.ReactNode;
  className?: string;
  style?: React.CSSProperties;
  label?: string; // Optional fieldset label
}

export const RadioGroup: React.FC<RadioGroupProps> = ({
  name,
  value,
  onChange,
  children,
  className,
  style,
  label,
}) => {
  const containerClasses = [styles.groupContainer, className]
    .filter(Boolean)
    .join(" ");

  return (
    <RadioContext.Provider value={{ name, selectedValue: value, onChange }}>
      <div
        className={containerClasses}
        role="radiogroup"
        aria-label={label}
        style={style}
      >
        {label && <span className={styles.groupLabel}>{label}</span>}
        {children}
      </div>
    </RadioContext.Provider>
  );
};

export interface RadioProps {
  value: string;
  label: string;
  disabled?: boolean;
  className?: string;
}

export const Radio: React.FC<RadioProps> = ({
  value,
  label,
  disabled,
  className,
}) => {
  const context = useContext(RadioContext);
  const generatedId = useId();
  const radioId = `radio-${generatedId}`;

  if (!context) {
    throw new Error("Radio component must be used within a RadioGroup");
  }

  const { name, selectedValue, onChange } = context;
  const isChecked = selectedValue === value;

  const handleChange = () => {
    if (!disabled && onChange) {
      onChange(value);
    }
  };

  const containerClasses = [
    styles.radioContainer,
    disabled ? styles.disabled : "",
    className,
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <label htmlFor={radioId} className={containerClasses}>
      <div className={styles.inputWrapper}>
        <input
          type="radio"
          id={radioId}
          name={name}
          value={value}
          checked={isChecked}
          onChange={handleChange}
          disabled={disabled}
          className={styles.input}
        />
        <div className={styles.radioControl}>
          <div className={styles.innerCircle} />
        </div>
      </div>
      {label && <span className={styles.labelText}>{label}</span>}
    </label>
  );
};
