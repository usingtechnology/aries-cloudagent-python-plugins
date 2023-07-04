#!/bin/bash
set -ex


# Convenience workspace directory for later use
WORKSPACE_DIR=$(pwd)

# Change some Poetry settings to better deal with working in a container
poetry config cache-dir ${WORKSPACE_DIR}/.cache
poetry config virtualenvs.in-project true
# Now install all dependencies
poetry install

export PATH=${PATH}:${WORKSPACE_DIR}/.venv/bin
# install this plugin code
# pip install --upgrade pip
# pip install -e ./