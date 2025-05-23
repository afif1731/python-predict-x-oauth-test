import torch
import torch.nn.functional as F
from src.config.model_config import model_hs, model_sh, tokenizer_hs, tokenizer_sh, device

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
      'username': data['username'],
      'tweet_id': data['tweet_id'],
      'sh_prediction': predict_result[i]['sh_label'],
      'sh_confidence': predict_result[i]['sh_confidence'],
      'hs_prediction': predict_result[i]['hs_label'],
      'hs_confidence': predict_result[i]['hs_confidence']
    })
  
  return result

async def get_predict(texts: list[str]):
  inputs_sh = tokenizer_sh(texts, return_tensors="pt", padding=True).to(device)
  inputs_hs = tokenizer_hs(texts, return_tensors="pt", padding=True).to(device)

  with torch.no_grad():
    outputs_sh = model_sh(**inputs_sh)
    probs_sh = F.softmax(outputs_sh.logits, dim=-1)
    pred_classes_sh = torch.argmax(probs_sh, dim=-1)
    confidences_sh = torch.max(probs_sh, dim=-1).values

    outputs_hs = model_hs(**inputs_hs)
    probs_hs = F.softmax(outputs_hs.logits, dim=-1)
    pred_classes_hs = torch.argmax(probs_hs, dim=-1)
    confidences_hs = torch.max(probs_hs, dim=-1).values

  results = []
  for i, text in enumerate(texts):
    results.append({
      'text': text,
      'sh_label': pred_classes_sh[i].item(),
      'sh_confidence': confidences_sh[i].item(),
      'hs_label': pred_classes_hs[i].item(),
      'hs_confidence': confidences_hs[i].item(),
    })

  return results