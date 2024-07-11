#!/bin/bash

# Update and upgrade the system
sudo apt update
sudo apt upgrade -y

# Install Python and Pip
sudo apt install -y python3 python3-pip python3-venv

# Create and activate a virtual environment
python3 -m venv myprojectenv
source myprojectenv/bin/activate

# Install Flask
pip install Flask

# Verify the installation
python -m flask --version

echo "Flask installation completed successfully!"