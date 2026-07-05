#!/bin/bash
set -euo pipefail
echo "Setting up Patient Scheduling Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
