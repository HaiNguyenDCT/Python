# Copilot Instructions for This Codebase

## Overview
This project is a minimal Python environment, likely for learning or experimentation. It contains:
- A single script: `Lesson1.py` (simple input/output demo)
- A local virtual environment (venv) in `myenv/` with standard Python structure

## Project Structure
- `myenv/` — Python virtual environment (do not edit directly)
  - `Lesson1.py` — Main script, currently asks for user input and prints a greeting
  - `Lib/site-packages/` — Installed packages (e.g., pip)
  - `Scripts/`, `Include/`, `pyvenv.cfg` — venv internals

## Key Patterns & Conventions
- **All code should go in `Lesson1.py` or new scripts in `myenv/`**
- Do not modify files in `Lib/`, `Include/`, or `Scripts/` unless you are managing the environment itself
- No custom build, test, or debug workflows are present
- No external dependencies beyond standard venv and pip
- No project-specific code conventions or patterns are established yet

## Developer Workflows
- **Run scripts**: Activate the venv in `myenv/` and run Python files (e.g., `python Lesson1.py`)
- **Add dependencies**: Use pip inside the venv (e.g., `pip install <package>`)
- **No tests or CI/CD**: No test or automation setup is present

## Example: Adding a New Script
1. Create a new `.py` file in `myenv/` (e.g., `Lesson2.py`)
2. Write your code
3. Run with the venv activated: `python Lesson2.py`

## Integration Points
- None: This project is fully self-contained

## Summary
This is a basic Python learning environment. Follow standard Python practices. If you add new scripts, keep them in `myenv/` and avoid changing venv internals.
