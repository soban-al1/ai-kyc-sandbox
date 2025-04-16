# AI‑KYC Sandbox 🚀

An end‑to‑end demo that shows how AI can streamline customer onboarding while keeping compliance teams happy.

## ✨ Features
- Upload passport/ID + selfie ➜ instant OCR + face‑match
- Lightweight fraud‑risk model (LogReg) trained on synthetic data
- Rule engine for classic AML red flags (PEP match, high‑risk country, etc.)
- Streamlit front‑end & FastAPI back‑end (both containerised)

## 🏗️ Quick start
```bash
git clone https://github.com/your‑handle/ai‑kyc‑sandbox.git
cd ai‑kyc‑sandbox
docker compose up --build
