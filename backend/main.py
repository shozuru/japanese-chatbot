from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import IntentClassification, VocabPractice, GrammarCorrector, \
    Translation, Conversation
import re 

app: FastAPI = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ChatText(BaseModel):
    message: str

class VocabData(BaseModel):
    vocab: str
    guess: str


@app.post('/stopConvo')
async def stopConversation() -> dict[str, str]:
    return {"response": "Conversation has stopped."}

@app.post('/conversation')
async def generateResponse(inputText: ChatText) -> dict[str, str]:
    if not inputText:
        raise HTTPException(status_code=400,
                            detail="Input message cannot be empty")
    
    userMessage: str = inputText.message
    botResponse: str = Conversation.generateConvoResponse(userMessage)

    return {"response": botResponse}

@app.post('/answer')
async def check_vocab_answer(inputText: VocabData) -> dict[str, str]:
    if not inputText:
        raise HTTPException(status_code=400,
                            detail="Input message cannot be empty")

    correctness: bool = \
        VocabPractice.check_answer(inputText.vocab, inputText.guess)
    
    return {"response": str(correctness)}


@app.post('/grammar')
async def correct_sentence(inputText: ChatText) -> dict[str, str]:
    if not inputText:
        raise HTTPException(status_code=400,
                            detail="Input message cannot be empty")
    correctedSentence: str = \
        GrammarCorrector.getCorrectedSentence(inputText.message)

    response: dict[str, str] = {}

    if correctedSentence.strip():
        response = {
            "response": f"Corrected sentence: {correctedSentence}"
        }
    else:
        response = {
            "response" : "I could not correct the sentence you provided."
        }

    return response

@app.post('/chat')
async def chat_response(inputText: ChatText) -> \
            dict[str, str|IntentClassification.Intent]:
    
    if not inputText:
        raise HTTPException(status_code=400, 
                            detail="Input message cannot be empty")
    
    intent: IntentClassification.Intent = \
        IntentClassification.classify_intent(inputText.message.strip())
    
    response: dict[str, str] = {}

    # if intent == IntentClassification.Intent.VOCAB:
    #     vocab_word: str = VocabPractice.generate_random_vocab()
    #     question: str = f"How do you say '{vocab_word}' in Japanese?"
    #     response = {
    #             "intent": intent.value, 
    #             "vocab_word": vocab_word, 
    #             "response": question
    #             }
    
    if intent == IntentClassification.Intent.GRAMMAR:
        message: str = "Please enter the sentence you want corrected."

        response = {
            "intent": intent,
            "response": message
        }
    
    elif intent == IntentClassification.Intent.CHAT:
        print("the intent is to have a conversation")
        message: str = "Okay, let's practice having a conversation!"

        response = {
            "intent": intent,
            "response": message
        }
        
    elif intent == IntentClassification.Intent.TRANSLATION:
        textMessage = inputText.message.strip().lower()

        pattern = \
            re.compile(r"^how do you say\s+(.*?)(?:\s+in\s+japanese)?\??$", \
                             re.IGNORECASE)

        match = pattern.search(textMessage)

        if match:
            translatedSentece = \
                Translation.translateSentence(match.group(1))
        
            response = {
                "intent": intent,
                "response": translatedSentece
            }
        else:
            response = {
                "intent": intent,
                "response": "Could not get translation."
            }

    else:
        responseMessage = IntentClassification.generate_response(intent)
        response = {
            "intent": intent,
            "response": responseMessage
            }
        
    return response
