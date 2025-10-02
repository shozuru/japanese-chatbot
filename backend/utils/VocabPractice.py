import json
import random
from pathlib import Path

with open(Path("./utils/knowledgeBase.json"), 'r', encoding="utf-8") as file:
    VOCAB_DATA: list[dict[str, str]] = json.load(file)

def generate_random_vocab() -> str:
    random_vocab = [pair["en"] for pair in VOCAB_DATA]
    return random.choice(random_vocab)

def check_answer(word: str, guess: str) -> bool:
    for pair in VOCAB_DATA:
        if pair["en"] == word:
            return guess == pair["jp"] 
    return False