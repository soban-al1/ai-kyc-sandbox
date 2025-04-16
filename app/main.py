
### 4.2 `app/main.py`

```python
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from utils.ocr import extract_text
from utils.face_match import verify_face
from utils.model import load_model, score_risk

app = FastAPI(title="AI‑KYC API")
model = load_model("artifacts/risk_model.pkl")

class KYCResponse(BaseModel):
    id_number: str
    risk_score: float
    decision: str

@app.post("/verify", response_model=KYCResponse)
async def verify(id_doc: UploadFile = File(...), selfie: UploadFile = File(...)):
    text = await extract_text(id_doc)
    face_ok = await verify_face(id_doc, selfie)
    risk = score_risk(model, text, face_ok)
    decision = "APPROVE" if risk < 0.4 else "REVIEW"
    return {"id_number": text.get("id_number", "N/A"),
            "risk_score": risk,
            "decision": decision}
