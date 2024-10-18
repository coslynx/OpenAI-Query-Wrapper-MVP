#!/bin/bash

# Start the AI Wrapper MVP

set -e

# Load environment variables
if [ -f ".env" ]; then
  source .env
fi

echo "Starting the backend server..."
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Wait for backend to start
sleep 5

echo "Backend server started."

# Check if the backend is running
ps aux | grep "uvicorn main:app" > /dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "Backend server failed to start. Exiting..."
  exit 1
fi

echo "AI Wrapper MVP started successfully."