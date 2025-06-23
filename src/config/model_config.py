from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoConfig
from dotenv import load_dotenv
import torch
import os

load_dotenv(override=True)

MODEL_HS_NAME = os.getenv('MODEL_HS_NAME')
MODEL_SH_NAME = os.getenv('MODEL_SH_NAME')

model_hs_path = "./model/" + str(MODEL_HS_NAME) + "/bert_hs/"
tokenizer_hs_path = "./model/" + str(MODEL_HS_NAME) + "/tokenizer_hs/"

model_sh_path = "./model/" + str(MODEL_SH_NAME) + "/bert_sh/"
tokenizer_sh_path = "./model/" + str(MODEL_SH_NAME) + "/tokenizer_sh/"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("🕐 Loading Hate Speech Model...")

tokenizer_hs = AutoTokenizer.from_pretrained(tokenizer_hs_path, trust_remote_code=True)
print(f'loaded Hate Speech tokenizer from {tokenizer_hs_path}')

config_hs = AutoConfig.from_pretrained(model_hs_path)
model_hs = AutoModelForSequenceClassification.from_pretrained(model_hs_path, config=config_hs, trust_remote_code=True)
print(f'loaded Hate Speech model & config from {model_hs_path}')
# print("Tokenizer Special Map:", tokenizer_hs.special_tokens_map)
# print("Model config:", model_hs.config)
print("🎉 Loading Model Success...")

print("🕐 Loading Sexual Harassment Model...")

tokenizer_sh = AutoTokenizer.from_pretrained(tokenizer_sh_path, trust_remote_code=True)
print(f'loaded Sexual Harassment tokenizer from {tokenizer_sh_path}')

config_sh = AutoConfig.from_pretrained(model_sh_path)
model_sh = AutoModelForSequenceClassification.from_pretrained(model_sh_path, config=config_sh, trust_remote_code=True)
print(f'loaded Sexual Harassment model & config from {model_sh_path}')
# print("Tokenizer Special Map:", tokenizer_sh.special_tokens_map)
# print("Model config:", model_sh.config)
print("🎉 Loading Model Success...")

def load_model_hs():
    model_hs.to(device)
    model_hs.eval()

def load_model_sh():
    model_sh.to(device)
    model_sh.eval()

load_model_hs()
load_model_sh()