import React, { useState } from "react";
import styles from "./Avatar.module.css";

export interface AvatarProps {
  src?: string;
  alt?: string;
  fallback: string;
  size?: "xs" | "sm" | "md" | "lg" | "xl";
  className?: string;
}

export const Avatar: React.FC<AvatarProps> = ({
  src,
  alt,
  fallback,
  size = "md",
  className,
}) => {
  const [hasError, setHasError] = useState(false);

  const containerClasses = [styles.avatar, styles[size], className]
    .filter(Boolean)
    .join(" ");

  const showFallback = !src || hasError;

  return (
    <div className={containerClasses}>
      {showFallback ? (
        <div className={styles.fallback} aria-label={alt || fallback}>
          {fallback}
        </div>
      ) : (
        <img
          src={src}
          alt={alt}
          className={styles.image}
          onError={() => setHasError(true)}
        />
      )}
    </div>
  );
};
