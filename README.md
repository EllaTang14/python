# AI Chat Application

This is a Python-based AI chatbot application that provides both web and CLI interfaces for interacting with the Gemini AI model.

## Features

- Web interface with a modern chat UI
- CLI interface for testing and direct interaction
- Uses Google's Gemini AI model
- Deployable to Vercel

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. The application is configured to use the Gemini AI model with the API key stored in vercel.json.

## Usage

### Web Interface

To run the web interface:
```bash
python api/app.py
```
Then open your browser and navigate to `http://localhost:5000`

### CLI Interface

To use the CLI interface:
```bash
python api/app.py --cli
```

## Deployment

The application is configured for deployment on Vercel. The configuration is stored in `vercel.json`, which includes:
- API key configuration
- Model selection
- Routing configuration

## Project Structure

- `api/app.py`: Main application file
- `api/templates/index.html`: Web interface template
- `vercel.json`: Vercel deployment configuration
- `requirements.txt`: Python dependencies 