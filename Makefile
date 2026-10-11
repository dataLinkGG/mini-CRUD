PYTHON ?= python3
VENV ?= .venv
BIN := $(VENV)/bin

.DEFAULT_GOAL := help

.PHONY: help install install-dev audit outdated upgrade hooks

help:
	@echo "Python dependency commands (virtualenv: $(VENV))"
	@echo "  make install      Install runtime dependencies"
	@echo "  make install-dev  Install runtime and development dependencies"
	@echo "  make audit        Check resolved dependencies for known vulnerabilities"
	@echo "  make outdated     List installed packages with newer releases"
	@echo "  make upgrade      Install the newest versions allowed by the ~= pins, then audit"
	@echo "  make hooks        Install the pre-commit git hook"

$(BIN)/pip:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip

install: $(BIN)/pip
	$(BIN)/pip install -r backend/requirements.txt

install-dev: $(BIN)/pip
	$(BIN)/pip install -r backend/requirements-dev.txt

audit: install-dev
	$(BIN)/pip-audit -r backend/requirements.txt
	$(BIN)/pip-audit -r backend/requirements-dev.txt

outdated: install-dev
	$(BIN)/pip list --outdated

upgrade: install-dev
	$(BIN)/pip install --upgrade -r backend/requirements-dev.txt
	$(BIN)/pip-audit -r backend/requirements.txt
	$(BIN)/pip-audit -r backend/requirements-dev.txt

hooks: install-dev
	$(BIN)/pre-commit install
