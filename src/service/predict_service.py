import torch
import torch.nn.functional as F
from src.config.model_config import model, tokenizer, device, model_label

async def batch_predict_service(batch_data):
  result = []
  text_list = []

  for data in batch_data:
    text_list.append(data['tweet_text'])
  
  predict_result = await get_predict(text_list)

  for i, data in enumerate(batch_data):
    result.append({
      'tweet_text': data['tweet_text'],
      'user_id': data['user_id'],
      'tweet_id': data['tweet_id'],
      'prediction': model_label[predict_result[i]['label']],
      'confidence': predict_result[i]['confidence']
    })
  
  return result

async def get_predict(texts: list[str]):
  inputs = tokenizer(texts, return_tensors="pt", truncation=True, padding=True).to(device)

  with torch.no_grad():
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=-1)
    pred_classes = torch.argmax(probs, dim=-1)
    confidences = torch.max(probs, dim=-1).values

  results = []
  for i, text in enumerate(texts):
    results.append({
      'text': text,
      'label': pred_classes[i].item(),
      'confidence': confidences[i].item(),
    })

  return results