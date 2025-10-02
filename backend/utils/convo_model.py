from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt2-medium", \
                                          use_fast=False)
tokenizer.do_lower_case = True

model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")
model.to(device)