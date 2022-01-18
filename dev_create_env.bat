@echo off
if not exist ./env/ (
    python -m venv ./env
) else (
    echo Nothing to create, environment already exists.
)