import httpx
import os
from dotenv import load_dotenv
from .schemas import QuoteResponse

load_dotenv()

class FinanceClient:
    def __init__(self):
        self._client = None
        self._api_key = os.getenv("BINANCE_API_KEY")

    async def __aenter__(self):
        headers = {"X-MBX-APIKEY": self._api_key} if self._api_key else {}
        self._client = httpx.AsyncClient(timeout=10.0, headers=headers)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.aclose()

    async def get_quote(self, symbol: str) -> QuoteResponse:
        url = "https://api.binance.com/api/v3/ticker/price"
        params = {"symbol": f"{symbol.upper()}USDT"}
        
        print(f"[DEBUG] Запрос к Binance: {url} | Params: {params}")
        
        response = await self._client.get(url, params=params)
        
        if response.status_code != 200:
            print(f"[ERROR] Binance ответил: {response.status_code} | {response.text}")
            
        response.raise_for_status()
        data = response.json()

        return QuoteResponse(
            symbol=data['symbol'],
            price=float(data['price']),
            timestamp="now"
        )
