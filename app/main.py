from fastapi import FastAPI, Depends, HTTPException
from .external_api import FinanceClient
from .schemas import QuoteResponse

app = FastAPI()

async def get_finance_client():
    async with FinanceClient() as client:
        yield client

@app.get("/")
async def read_root():
    return {"message": "Fintech API is running"}

@app.get("/quote/{symbol}", response_model=QuoteResponse)
async def get_quote(symbol: str, client: FinanceClient = Depends(get_finance_client)):
    try:
        return await client.get_quote(symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
