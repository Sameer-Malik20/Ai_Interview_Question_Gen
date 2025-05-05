# 🧠 AI Interview Question Generator

This is a full-stack web application that generates interview questions using AI. Users can get a list of relevant questions based on the selected topic. The app uses a backend powered by Python (Flask/FastAPI) and integrates with Google's Gemini AI API to generate questions and answers dynamically.

---

## 🚀 Features

- 🔍 Generate interview questions based on a specific topic.
- 🤖 Each question comes with four multiple-choice options and the correct answer.
- 📄 AI-generated data using Gemini Pro API.
- 🧪 Easy-to-use and minimal UI built with React.
- 🎯 Real-time prompt-based question generation.

---

## 🛠️ Tech Stack

### Frontend
- ReactJS
- Tailwind CSS

### Backend
- Python (Flask or FastAPI)
- Google Gemini API
- RESTful APIs

---

## 📦 Installation

### Prerequisites
- Node.js & npm
- Python 3.x
- Gemini API Key (from Google AI Studio)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-interview-generator.git
cd ai-interview-generator
2. Setup Backend
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt

# Create a .env file and add your Gemini API key
echo "GEMINI_API_KEY=your-api-key-here" > .env

# Run the server
python app.py
3. Setup Frontend
bash
Copy
Edit
cd ../client
npm install
npm start
📌 Usage
Run the backend server (Flask).

Start the React development server.

Go to http://localhost:3000 in your browser.

Enter a topic like "JavaScript" or "Machine Learning" to generate a quiz.

📂 Folder Structure
arduino
Copy
Edit
ai-interview-generator/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   └── utils/
│       ├── TTS.py
│       └── caption_generator.py
├── client/
│   ├── public/
│   └── src/
│       └── InterviewAI.jsx
🧠 Sample Prompt Used for AI
txt
Copy
Edit
"Generate 5 interview questions about {topic}, with 4 options each, and mention the correct answer."
📜 License
This project is licensed under the MIT License. See LICENSE for more information.

🙌 Acknowledgements
Gemini API

React

TailwindCSS

yaml
Copy
Edit

---

Would you like this README in a downloadable `.md` file or want help customizing it for deployment inst
