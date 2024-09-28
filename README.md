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

    python index.py

## Deploy with Vercel

Create a new project and API key in the OpenAI developer portal: https://platform.openai.com/api-keys

Initialize Vercel

    vercel

Save the OpenAI API key to the project

In the project settings, disable [Vercel Authentication](https://vercel.com/cmonaghans-projects-a39a8622/ai-bartender/settings/deployment-protection)

Connect the [git repository](https://vercel.com/cmonaghans-projects-a39a8622/ai-bartender/settings/git)

Run locally using vercel (simulate how it will behave on deployment)

    vercel dev

Note, the app entrypoint MUST be named `index.py` otherwise vercel will 404.
