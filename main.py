from fastapi import FastAPI, HTTPException
import pandas as pd
from summary_logic import generate_ai_case_summary

app = FastAPI(
    title="NyayaMitra – AI Case Summary API",
    version="1.0"
)

DATASET_PATH = "data/nyayamitra_final_dataset.csv"

try:
    df = pd.read_csv(DATASET_PATH)
    df.columns = df.columns.str.strip().str.lower()
except Exception as e:
    df = None
    print("Dataset load error:", e)


@app.get("/")
def home():
    return {"message": "NyayaMitra AI Case Summary API is running"}


@app.get("/ai-case-summary/{cnr_number}")
def ai_case_summary(cnr_number: str):

    if df is None:
        raise HTTPException(status_code=500, detail="Dataset not loaded")

    if "cnr_number" not in df.columns:
        raise HTTPException(status_code=500, detail="CNR_NUMBER column missing")

    case_row = df[df["cnr_number"].astype(str).str.strip() == cnr_number.strip()]

    if case_row.empty:
        raise HTTPException(status_code=404, detail="Case not found")

    row = case_row.iloc[0].to_dict()
    summary = generate_ai_case_summary(row)

    return {
        "cnr_number": cnr_number,
        "ai_case_summary": summary
    }

