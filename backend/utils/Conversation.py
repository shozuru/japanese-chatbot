from utils.convo_model import tokenizer, model, device
import torch

def generateConvoResponse(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    input_ids = inputs["input_ids"]

    outputs = model.generate(
        **inputs,
        max_length=30,
        do_sample=True,
        temperature=0.65,
        top_p=0.95,
        pad_token_id=tokenizer.pad_token_id
    )   

    generated_ids = outputs[0][input_ids.shape[-1]:]

    response = tokenizer.decode(generated_ids, skip_special_tokens=True)

    END_MARKS = ["。", "？", "！", ".", "?", "!"]
    for i in reversed(range(len(response))):
        if response[i] in END_MARKS:
            response = response[:i+1]
            break
    
    return response