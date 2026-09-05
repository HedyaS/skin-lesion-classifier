from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CLASSES = ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]

@app.get("/")
def read_root():
    return {"status": "Skin lesion classifier API is running"}

@app.post("/predict")
async def predict(file: UploadFile):
    # placeholder — real model inference gets wired in once training is done
    return {
        "prediction": "nv",
        "confidence": 0.87,
        "all_probs": {c: round(1 / 7, 3) for c in CLASSES},
    }