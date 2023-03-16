# Refactoring Analysis: From God Class to Patterns

## Problems in `before.py`
The original `DataProcessor` suffered from several issues:
1.  **Violation of Single Responsibility Principle (SRP)**: It handled configuration, logging, parsing for multiple formats, formatting, file I/O, and SMTP communication all in one class.
2.  **Violation of Open/Closed Principle (OCP)**: Adding a new source type (e.g., XML) would require modifying the `process_data` method directly with more `if/elif` branches.
3.  **High Coupling**: The parsing logic, formatting logic, and notification logic were tightly coupled, making it difficult to test or reuse any part independently.
4.  **Difficult to Maintain**: At only 200 lines, it's already becoming a "god object". As more features are added, it will become increasingly fragile.

## Patterns used in `after/`
To fix these issues, we refactored the logic using several design patterns:

### 1. Singleton (AppConfig)
- **What it fixed**: Managed application-wide configuration in a thread-safe way.
- **Why**: Ensures that only one configuration object exists and is shared across the system.

### 2. Factory Method (ParserFactory)
- **What it fixed**: Decoupled the processor from the specific parsing implementations.
- **Why**: Allows adding new data source parsers without modifying the main processing logic.

### 3. Strategy (DataParser implementations)
- **What it fixed**: Encapsulated different parsing algorithms into their own classes.
- **Why**: Makes the parsing logic interchangeable and testable in isolation.

### 4. Facade (NotificationFacade)
- **What it fixed**: Hid the complexity of the SMTP notification subsystem.
- **Why**: The `DataProcessor` only needs to know *how to notify*, not the details of SMTP protocols or server configurations.

## Conclusion
The refactored version is more modular, easier to test, and ready for future extensions. Each class has a single responsibility, and the system is more robust against changes in any individual component.
