# Specification: Python project requirements

**Version:** 0.1

**Last Updated:** 2025-05-11

## 1. Purpose & Scope

This document specifies the best practices a python project should follow.

## 2. Core Principles & Guidelines

[List the specific rules, guidelines, patterns, and constraints here.]

* Use the repository as the root of Python project.
* Use `uv` package manager and use `pyproject.toml` to manage packages instead of using `requirements.txt`
* Use `uv add <package>` instead of using `uv pip install`
* Ensure the virtual environmet directory is added to the `.gitignore` at the root of repository.

## 3. Rationale & Context

[Explain the reasoning behind the principles and guidelines.]

## 4. Examples

```
# initialize the python project in current directory
uv init

# add a module to the project
uv add requests
```

## 5. Related Specifications / Further Reading

[Use uv to manage project](https://docs.astral.sh/uv/guides/projects/)

## 6. Keywords
