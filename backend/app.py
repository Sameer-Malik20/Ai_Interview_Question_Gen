from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/interviewAI', methods=['POST'])
def interviewAI():
    data = request.get_json()
    topic = data.get('topic')

    
    
    
    prompt = f"""Generate a list of interview questions related to the topic: {topic}.
"""


    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        raw_content = response.candidates[0].content.parts[0].text
      

        return jsonify({"content": raw_content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
