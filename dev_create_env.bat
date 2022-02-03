@echo off
if not exist ./env/ (
    python -m venv ./env
    dev_download_deps.bat
) else (
    echo Nothing to create, environment already exists.
)