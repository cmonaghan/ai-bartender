from flask import Flask, render_template, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/get-cocktail', methods=['POST'])
def get_cocktail():
    data = request.get_json()

    boozy = data.get('boozy')
    sweet = data.get('sweet')
    citrusy = data.get('citrusy')
    floral = data.get('floral')
    adventure = data.get('adventure')
    additional_preferences = data.get('additionalPreferences', '')

    # Construct the prompt based on user preferences
    prompt = f"""
    You are an expert mixologist. Create a unique and creative cocktail recipe based on the following preferences:

    - Boozy level (0-10): {boozy}
    - Sweetness (0-10): {sweet}
    - Citrusy level (0-10): {citrusy}
    - Floral notes (0-10): {floral}
    - Adventure level (0-10): {adventure}
    {f"- Additional preferences: {additional_preferences}" if additional_preferences else ""}

    Provide the recipe in the following format:

    Cocktail Name: [Name]

    Ingredients:
    - [List of ingredients]

    Instructions:
    1. [Step-by-step instructions]

    Ensure the recipe is precise, clear, and matches the user's preferences.
    """

    try:
        # Call the OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.8,
            top_p=1,
            n=1,
            stop=None
        )

        # Extract the recipe from the response
        recipe = response.choices[0].text.strip()
        return jsonify({'recipe': recipe})

    except Exception as e:
        print(f"Error generating cocktail recipe: {e}")
        return jsonify({'error': 'Error generating cocktail recipe'}), 500

if __name__ == '__main__':
    app.run(debug=True)
