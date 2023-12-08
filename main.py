from flask import Flask, render_template
import openai
from dotenv import load_dotenv
import os

app = Flask(__name__)

user_input = input("Write some sentence to be completed: ")

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route("/")
def text_complete():
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=50
    )

        tagline = response['choices'][0]['text'].strip()

        return render_template('index.html', tagline=tagline)
    

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)






