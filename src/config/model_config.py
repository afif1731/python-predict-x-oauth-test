from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
import torch
import os

load_dotenv()

MODEL_HS_NAME = os.getenv('MODEL_HS_NAME')
MODEL_SH_NAME = os.getenv('MODEL_SH_NAME')

model_hs_path = "./model/" + str(MODEL_HS_NAME) + "/bert_hs"
tokenizer_hs_path = "./model/" + str(MODEL_HS_NAME) + "/tokenizer_hs"

model_sh_path = "./model/" + str(MODEL_SH_NAME) + "/bert_sh"
tokenizer_sh_path = "./model/" + str(MODEL_SH_NAME) + "/tokenizer_sh"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer_hs = AutoTokenizer.from_pretrained(tokenizer_hs_path)
model_hs = AutoModelForSequenceClassification.from_pretrained(model_hs_path)

tokenizer_sh = AutoTokenizer.from_pretrained(tokenizer_sh_path)
model_sh = AutoModelForSequenceClassification.from_pretrained(model_sh_path)

def load_model_hs():
    print("🕐 Loading Hate Speech Model...")
    model_hs.to(device)
    model_hs.eval()
    print("🎉 Loading Model Success...")

def load_model_sh():
    print("🕐 Loading Sexual Harassment Model...")
    model_sh.to(device)
    model_sh.eval()
    print("🎉 Loading Model Success...")

load_model_hs()
load_model_sh()