// components/Button.tsx
import React, { ButtonHTMLAttributes, ReactNode } from 'react';

// Define the props for the Button component
interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
  // You can add more specific props as needed
}

// Button component
const Button: React.FC<ButtonProps> = ({ children, ...props }) => {
  return <button {...props}>{children}</button>;
};

export default Button;
