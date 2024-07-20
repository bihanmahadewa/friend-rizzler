# Rizz Detector Plugin

This plugin analyzes conversation transcripts to detect and measure 'rizz' levels.

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your environment variables in `.env`
4. Run the FastAPI app: `python main.py`

## Usage

The plugin listens for POST requests at the `/rizz-detector` endpoint. It expects a JSON payload with `uid`, `session_id`, and `segments` fields.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.