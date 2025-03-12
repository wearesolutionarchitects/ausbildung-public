# GitHub Copilot Custom Instructions

## Context

This project follows a structured and modular development approach with a focus on:

- **Separation of concerns**: Keeping business logic, presentation, and data access distinct.
- **Performance optimization**: Writing efficient and scalable code.
- **Code reusability**: Encouraging modular, **KISS (Keep It Simple, Stupid)** and **DRY (Don't Repeat Yourself)** principles.
- **Security best practices**: Avoiding vulnerabilities in authentication, authorization, and data handling.

---

## Code Style and Formatting

- Use **camelCase** for variables and functions.
- Use **PascalCase** for class names.
- Use **snake_case** for file and database table names.
- Follow **Prettier** for JavaScript and **YAML linting** for configuration files.
- Ensure **HTML5 and CSS3** compliance for web-related code.
- Prefer **ES6+ syntax** for JavaScript.

---

## Documentation & Comments

- Use **Markdown (.mdx)** for documentation with **MDX support** for interactive content.
- Maintain **structured YAML (.yaml) files** for configuration and data handling.
- Provide inline comments for complex logic.
- Write **clear and meaningful commit messages** following the format:

  ```plaintext
  feat: Short description of the feature
  fix: Short description of the fix
  refactor: Short description of refactoring
  ```

## Code Review Guidelines

- Ensure **no console logs** in production code.
- Use **meaningful variable and function names**.
- Avoid **hardcoded values**, use environment variables where needed.
- Follow the **MVC (Model-View-Controller) architecture** for structured code organization.
- Ensure **test coverage** for critical functionalities.

## Git Workflow

- Use **feature branches** (e.g., `feature/add-user-auth`).
- Follow **Pull Request (PR) templates** and request reviews before merging.
- Use **semantic versioning** (e.g., `v1.2.3`).

## AI-Assisted Suggestions

- Prefer **functionally correct** over purely optimized solutions.
- Suggest **secure** and **best-practice** implementations.
- Prioritize **readability and maintainability**.
- Assist in **debugging and error handling improvements**.

## Dependencies & Tools

- Framework: **Astro** (with .mdx file support)
- Backend: **Node.js (Express / Astro SSR)**
- Frontend: **React / CSS**
- Database: **PostgreSQL / MySQL**
- CI/CD: **GitHub Actions**
- Testing: **Playwright**
- API Documentation: **Swagger / OpenAPI**

---
