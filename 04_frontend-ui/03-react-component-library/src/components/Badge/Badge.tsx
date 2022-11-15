import React from "react";
import styles from "./Badge.module.css";

export interface BadgeProps {
  variant?: "default" | "success" | "warning" | "error" | "info";
  size?: "sm" | "md";
  dot?: boolean;
  children?: React.ReactNode;
}

export const Badge: React.FC<BadgeProps> = ({
  variant = "default",
  size = "md",
  dot = false,
  children,
}) => {
  const classes = [
    styles.badge,
    styles[variant],
    styles[size],
    dot ? styles.dot : "",
  ]
    .filter(Boolean)
    .join(" ");

  return <span className={classes}>{!dot && children}</span>;
};
