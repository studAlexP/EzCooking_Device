#!/bin/bash

host=10.0.0.18
port=8080

# Start the server
cd /home/pi/Server/
source .venv/bin/activate
uvicorn server:app --host $host --port $port
