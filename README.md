# Japanese Chatbot
An interactive chatbot that helps users learn Japanese through free-form translation, grammar correction, and conversation. Instead of relying on a fixed knowledge base, it uses pretrained NLP models to dynamically translate words, phrases, and sentences, correct grammar mistakes, and respond to user messages in Japanese.

# Features
* Free-form translation: Ask "how do you say dog in Japanese?"
* Grammar correction: Type "Can you fix this sentence", provide the sentence (e.g. 東京に行きたいだ) and the bot suggests corrections (e.g. 東京に行きたい)
* Conversation Mode: Type "let's have a conversation" for practice speaking in conversations.

# Tech Stack
Frontend:
* React
* Axios

Backend:
* FastAPI
* Uvicorn

NLP Models:
* Hugging Face Transformers
* Conversation model: rinna/japanese-gpt2-medium
* Translation model: RichardErkhov/webbigdata_-_ALMA-7B-Ja-V2-gguf
* Grammar model: shozuru/t5-japanese-grammar-corrector 

# Cloning
```
git clone https://github.com/shozuru/japanese-chatbot.git
cd japanese-chatbot
```

# Installing backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

# Installing frontend
```
cd frontend
npm install
npm run build
npm run preview
```
# License
This project is licensed under the CC BY-NC 4.0 License
