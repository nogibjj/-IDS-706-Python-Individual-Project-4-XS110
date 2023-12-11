from flask import Flask, render_template, request
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#'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'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        gender = request.form.get("gender")
        age = request.form.get("age")
        goal = request.form.get("goal")

        prompt = (f"I am a {age} year old {gender}. I want to {goal}. "
                  "Can you provide a workout plan?")

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
            )
            workout_plan = response.choices[0].message["content"]
        except Exception as e:
            workout_plan = f"An error occurred: {str(e)}"

        return render_template("result.html", recommendation=workout_plan)

    # GET request returns the input form
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8000)
