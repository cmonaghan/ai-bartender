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

Initialize Vercel

    vercel

Share the OpenAI API key to the project under team settings

In the project settings, disable [Vercel Authentication](https://vercel.com/cmonaghans-projects-a39a8622/ai-bartender/settings/deployment-protection)

Connect the [git repository](https://vercel.com/cmonaghans-projects-a39a8622/ai-bartender/settings/git)

Add a vercel.json file

Deploy to prod

    vercel --prod
