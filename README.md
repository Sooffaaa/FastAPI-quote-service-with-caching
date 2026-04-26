## 🚀 Binance Quote Service (FastAPI)
Приложение принимает название монеты (например, BTC или ETH), стучится на биржу Binance, забирает актуальный ценник и отдает его пользователю в чистом и красивом виде.
## 🛠 Стек технологий

*  FastAPI (Asynchronous Server Gateway Interface), Pydantic v2, HTTPX (Асинхронные запросы) + Binance API

## 📈 Тестирование (API Documentation)
## Какие символы вводить?
Сервис автоматически добавляет постфикс USDT. Вы можете вводить любые тикеры, торгующиеся на Binance.
Примеры для ввода в поле symbol:

* BTC (Bitcoin)
* ETH (Ethereum)
* SOL (Solana)
* BNB (Binance Coin)
* XRP (Ripple)

## Пример запроса:
GET /quote/BTC

## Пример успешного ответа:
{
  "symbol": "BTCUSDT",
  "price": 64250.50,
  "timestamp": "now"
}
