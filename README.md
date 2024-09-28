# ai-bartender
A cocktail recipe recommendation engine

## Setup

Set your OpenAI API key

    # create .env file
    touch .env

    # Save the following in your .env file
    OPENAI_API_KEY="<secret_key>"

Setup virtual env and install requirements

    python3 -m venv venv
    . venv/bin/activate
    pip3 install -r requirements.txt


Run the server

    python app.py

## Deploy with Vercel

Initialize Vercel

    vercel
