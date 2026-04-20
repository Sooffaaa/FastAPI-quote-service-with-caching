from pydantic import BaseModel

class QuoteResponse(BaseModel):
    symbol: str
    price: float
    timestamp: str