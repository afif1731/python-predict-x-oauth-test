# How to Run Bcakend

### Create folder name `model`
```bash
mkdir model
```

### Put your model inside the folder you just created, and then create a `.env` file
```bash
HOST="localhost"
PORT="5000"

MODEL_NAME="your_model.pth"

SERVER_URI=${HOST}:${PORT}
```

### Create Python Environment (Recommended for Development)
```bash
py -3.9 -m venv .venv
```

### Activate Virtual environment (Windows)
```bash
.venv/Scripts/activate
```

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run Server
```bash
python .\main.py
```
