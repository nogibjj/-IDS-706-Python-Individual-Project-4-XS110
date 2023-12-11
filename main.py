from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Replace 'your_api_key' with your actual OpenAI API key
OPENAI_API_KEY = 'your_api_key'
headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
    'Content-Type': 'application/json'
}

def get_workout_recommendation(gender, age, goal):
    prompt = f"Provide a workout recommendation for a {age}-year-old {gender} who wants to {goal}."
    
    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        headers=headers,
        json={'prompt': prompt, 'max_tokens': 150}
    )
    return response.json()['choices'][0]['text']

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendation = ''
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        goal = request.form['goal']
        recommendation = get_workout_recommendation(gender, age, goal)
    return render_template('index.html', recommendation=recommendation)

if __name__ == '__main__':
    app.run(debug=True)
