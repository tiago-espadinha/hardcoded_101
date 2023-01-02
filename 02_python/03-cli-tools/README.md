# Module Name: DevKit CLI Tools

A comprehensive suite of developer productivity tools, including project scaffolding, encrypted password management, and personal finance tracking.

## Features
- **Scaffold**: Quickly bootstrap new projects using Jinja2-powered templates.
- **Vault**: Securely store and manage passwords using Fernet encryption and PBKDF2 key derivation.
- **Finance**: Track income and expenses with a built-in SQLite database and rich terminal visualizations.

## Learning Objectives
- Master modern CLI development using the Click library.
- Implement secure data storage with symmetric encryption and master password protection.
- Build interactive terminal experiences using the Rich library for tables, panels, and progress bars.
- Package and distribute Python applications using modern packaging standards.

## Project Structure
- `devkit/cli.py`: Main entry point for the CLI tool suite.
- `devkit/scaffold/`: Project templating and scaffolding logic.
- `devkit/vault/`: Encrypted password manager implementation.
- `devkit/finance/`: SQLite-backed personal finance tracker.
- `tests/`: Comprehensive test suite for all modules.

## Requirements
- Python 3.10+
- click
- rich
- cryptography
- pyperclip
- Jinja2

## How to Run
Install the package in editable mode:
```bash
pip install -e .
```

## Testing
Run all tests using pytest:
```bash
pytest
```
