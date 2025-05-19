import torch

pth_path = "./model/bert_stockbit_classification.pth"
obj = torch.load(pth_path, map_location="cpu")

if isinstance(obj, dict):
    if "state_dict" in obj:
        print("🔍 Ini mungkin checkpoint dari Lightning atau Trainer.")
    elif all(isinstance(v, torch.Tensor) for v in obj.values()):
        print("✅ Ini adalah state_dict (berisi bobot model saja).")
    else:
        print("📦 Ini adalah dict kompleks, bisa jadi state_dict + info tambahan.")
else:
    print("🧠 Ini adalah model lengkap (hasil torch.save(model)).")

for key in obj:
    print(f"{key}: {type(obj[key])}")
