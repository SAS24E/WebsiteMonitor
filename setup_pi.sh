#!/bin/bash
# Setup script for Raspberry Pi deployment

echo "Setting up WebsiteMonitor on Raspberry Pi..."

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

echo "Setup complete!"
echo ""
echo "Before running the script, set your Discord webhook URL:"
echo "export DISCORD_WEBHOOK_URL='your_webhook_url_here'"
echo ""
echo "Then run:"
echo ".venv/bin/python main.py"
