from transformers import BertTokenizer, BertForSequenceClassification
from dotenv import load_dotenv
import torch
import os

load_dotenv()

MODEL_NAME = os.getenv('MODEL_NAME')

model_path = "./model/" + str(MODEL_NAME)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = BertTokenizer.from_pretrained('crypter70/IndoBERT-Sentiment-Analysis')
model = BertForSequenceClassification.from_pretrained('crypter70/IndoBERT-Sentiment-Analysis', num_labels=3)

model_label = {
    0: 'bukan',
    1: 'yes',
    2: 'unknown'
}

def load_model_from_checkpoint():
    print(f"🔍 Loading checkpoint from: {model_path}")
    checkpoint = torch.load(model_path, map_location=device)

    if "model_state_dict" in checkpoint:
        # case: full checkpoint
        model.load_state_dict(checkpoint["model_state_dict"])
        print("✅ Loaded model_state_dict from checkpoint.")
    else:
        raise ValueError("❌ Unsupported .pth format. Expected a key named 'model_state_dict'.")

    model.to(device)
    model.eval()

load_model_from_checkpoint()
