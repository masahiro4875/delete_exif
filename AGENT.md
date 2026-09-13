# AGENT.md

## Project boundary

- This project is for removing EXIF metadata from PNG files.
- Do not implement the image-processing program unless the user explicitly asks for a specific implementation.
- Do not create application code, tests, or dependencies beyond the requested scope.
- Before making a code change, explain the proposed file and behavior briefly and wait for confirmation when the request is ambiguous.

## Development setup

- Use the local virtual environment at `.venv`.
- Install development tools into `.venv`; do not install them globally.
- Format Python files with Black:

  ```sh
  .venv/bin/black .
  ```

## Recommended structure

```text
delete_exif/
├── .venv/                 # Local virtual environment; do not commit
├── src/
│   └── delete_exif/       # Application package
├── tests/                 # Tests added by the user
├── AGENT.md               # Collaboration and scope rules
├── pyproject.toml         # Python and Black configuration
├── requirements-dev.txt   # Development dependencies
└── .gitignore
```

## Style

- Keep changes small and focused.
- Prefer the standard library unless a dependency is justified.
- Use type hints for new public functions.
- Keep user-facing behavior and file-overwrite behavior explicit.
