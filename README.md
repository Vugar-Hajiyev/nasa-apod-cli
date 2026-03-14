# NASA APOD CLI Tool

A professional Command Line Interface (CLI) tool designed to fetch and manage NASA's "Astronomy Picture of the Day" (APOD). This project demonstrates clean code architecture, API integration, and secure credential management.

## What it does
This tool allows you to interact with the official NASA API directly from your terminal. It fetches the daily space image (or an image for a specific date), displays it instantly, and optionally saves it to your local machine with clean formatting.

## Features
- **Fetch by Date:** Retrieve stunning space images for any specific date in the past.
- **Auto-Download:** Locally save high-resolution images with cleaned, OS-compatible filenames directly into an `images/` directory.
- **Secure:** Implements professional-grade security using environment variables (API keys are never hardcoded).
- **Smart Media Handling:** Automatically detects if the daily content is a video instead of an image and provides a direct playable link without crashing.

## Setup & Installation

```bash
# 1. Clone the repository
git clone [https://github.com/Vugar-Hajiyev/nasa-apod-cli.git](https://github.com/Vugar-Hajiyev/nasa-apod-cli.git)
cd nasa-apod-cli

# 2. Install all necessary dependencies
pip install -r requirements.txt

# 3. Configure API Key (Create .env file)
# Get your free key at [https://api.nasa.gov/](https://api.nasa.gov/)
echo "NASA_API_KEY=your_actual_key_here" > .env

# 4. How to Use
# Fetch and view today's image:
python main.py fetch-image
#Fetch and securely save an image for a specific date:
python main.py fetch-image 2023-12-25 --save
```
## Tech Stack & Security
Built with: Python 3.14, Typer, Requests, Pillow, Python-dotenv.
Git Safety: The .gitignore file ensures that .env and system caches (__pycache__) are never exposed to the public repository.

Developed by Vugar Hajiyev