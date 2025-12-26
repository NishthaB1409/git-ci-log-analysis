# Git-Based Continuous Integration for Log File Analysis

## Overview
This project demonstrates a Git-based Continuous Integration (CI) pipeline
that automatically analyzes system log files and validates them during each commit.

## Features
- Python-based log analysis tool
- Automated testing using pytest
- CI pipeline using GitHub Actions
- Linux-based execution environment

## How It Works
- The log analyzer counts INFO, WARNING, and ERROR messages
- If ERROR messages are detected, the CI pipeline fails
- Unit tests ensure correctness of the log parsing logic

## Run Locally
```bash
pip install -r requirements.txt
python log_analyzer.py sample.log
pytest
