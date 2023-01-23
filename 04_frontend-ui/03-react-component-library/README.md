# Module Name: Pulsar UI

A comprehensive React component library designed for flexibility, accessibility, and high visual impact.

## Features
- **Modern React**: Built with React 18 primitives.
- **Strictly Typed**: Fully written in TypeScript for robust development.
- **Accessible**: ARIA-compliant components following WAI-ARIA best practices.
- **Themable**: CSS Variables (Design Tokens) for easy customization and Dark Mode support.

## Learning Objectives
- Design component APIs that are flexible but not overly complex.
- Manage complex state (focus trap, keyboard nav) without a library.
- Write tests that verify behavior, not implementation details.

## Project Structure
- `src/components/`: Core UI components.
- `src/tokens/`: Design token definitions (CSS variables).
- `src/hooks/`: Reusable logic like `useForm` and `useToast`.
- `src/test/`: Global test configuration and utilities.

## Requirements
- Node.js 16+
- React 18+

## How to Run
Run the Storybook to see the components in action:
```bash
npm run storybook
```

## Theming
Wrap components with `ThemeProvider` to enable the built-in light or dark theme.

```tsx
import { ThemeProvider, useTheme } from "pulsar-ui";

const ThemeButton = () => {
	const { theme, setTheme } = useTheme();

	return (
		<button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
			Toggle theme
		</button>
	);
};

const App = () => (
	<ThemeProvider defaultTheme="light">
		<ThemeButton />
	</ThemeProvider>
);
```

## Testing
Run all tests using Vitest:
```bash
npm test
```
