## Project Overview

This project presents an advanced Python-based calculator featuring a robust command-line interface (REPL) for an interactive and user-friendly experience. It is designed with clean, maintainable code and incorporates industry-standard software development practices. The application leverages design patterns, professional logging, dynamic configuration via environment variables, and Pandas for efficient calculation history management. Key highlights of the project include:

- **REPL Interface**: Supports basic arithmetic operations, manages calculation history, and allows extended functionalities through dynamically loaded plugins.
- **Plugin System**: Implements a flexible plugin architecture for seamless integration of new features without altering the core application.
- **Calculation History Management**: Utilizes Pandas for managing, saving, loading, and deleting the calculation history.
- **Design Patterns**: Incorporates Facade, Command, Factory Method, Singleton, and Strategy patterns to ensure scalable, maintainable architecture.
- **Professional Logging**: Configurable logging settings, including log levels and output destinations, controlled via environment variables, adhering to professional logging standards.
- **Testing and Code Quality**: Achieved over 90% code coverage using Pytest and adhered to PEP 8 standards, validated by Pylint.
- **Version Control**: Follows best practices by logically grouping commits for feature development and related tests.
 

## Key Design Patterns Used

- **Facade Pattern**: Simplifies interaction with complex Pandas operations for history management.
- **Command Pattern**: Efficiently organizes REPL commands for operation and history handling.
- **Factory Method, Singleton, and Strategy Patterns**: Enhance flexibility and scalability within the application.

## Environment Variables and Logging

The project configures logging settings, such as log levels and output destinations, through environment variables. This logging system ensures all critical operations and errors are tracked for thorough monitoring.

## Exception Handling: LBYL and EAFP

The project follows both "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches in exception handling, maintaining robust error handling while ensuring clean, efficient code.

## Video Demonstration - [Link](https://drive.google.com/file/d/1wgFL8_N3T00wfN9jpA-0A4NGbSJ0Wu6K/view)
