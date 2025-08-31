from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Function to reverse a string
def return_backward_string(text: str) -> str:
    return text[::-1]

# Function to get mode from environment
def get_mode_value() -> str:
    # raise Exception() # -> To fail test with Exception
    return os.environ.get("APP_MODE", "development")

# Endpoint to reverse a string
@app.route("/", methods=["GET"])
def reverse_string():
    text = request.args.get("text", "")
    reversed_text = return_backward_string(text)
    return jsonify({"original": text, "reversed": reversed_text})

# Endpoint to get mode from environment variable
@app.route("/get-mode", methods=["GET"])
def get_mode():
    mode = get_mode_value()
    return jsonify({"mode": mode})

# Run code
if __name__ == "__main__":
    host = os.environ.get("FLASK_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host=host, port=port, debug=debug)
