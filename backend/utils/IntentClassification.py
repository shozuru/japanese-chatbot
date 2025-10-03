from enum import Enum, auto

class Intent(Enum):
    # VOCAB = "vocab_practice"
    GRAMMAR = 0
    CHAT = auto()
    HELP = auto()
    TRANSLATION = auto()

def classify_intent(message: str) -> Intent:
    lowerCaseMessage: str = message.lower()

    # if "vocab" in lowerCaseMessage:
    #     return Intent.VOCAB
    if "grammar" in lowerCaseMessage or "correct" in lowerCaseMessage \
            or "fix" in lowerCaseMessage:
        return Intent.GRAMMAR
    elif "chat" in lowerCaseMessage or "talk" in lowerCaseMessage or \
        "speak" in lowerCaseMessage or "convers" in lowerCaseMessage:
        return Intent.CHAT
    elif "how do you say" in lowerCaseMessage:
        return Intent.TRANSLATION
    else:
        return Intent.HELP

def generate_response(intent: Intent) -> str:
    if intent == Intent.HELP:
        return call_for_help()

# def vocab_practice() -> str:
#     return "Okay, let's practice vocab!"

def call_for_help() -> str:
    return "I didn't quite understand what you wanted to do. Could you " + \
            "repeat what you said?"