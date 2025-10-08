#!/bin/bash
# Simple script to serve the medication timeline locally
# Usage: ./serve.sh [port]

PORT=${1:-8000}

echo "Starting local web server on port $PORT..."
echo "Open your browser to: http://localhost:$PORT/meds.html"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 -m http.server $PORT
