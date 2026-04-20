## 🚀 Binance Quote Service (FastAPI)
Микросервис на Python, который предоставляет актуальные котировки криптовалют в реальном времени, используя интеграцию с Binance API.
## 🛠 Стек технологий

* Язык: Python 3.10+
* Фреймворк: FastAPI (Asynchronous Server Gateway Interface)
* Валидация данных: Pydantic v2
* HTTP Клиент: HTTPX (Асинхронные запросы)
* Сервер: Uvicorn

## 🚀 Запуск проекта

   1. Клонируйте репозиторий:
   
   git clone <url_вашего_репозитория>
   cd FastAPI-quote-service-with-caching
   
   2. Создайте и активируйте виртуальное окружение:
   
   python -m venv venv
   source venv/bin/activate  # для Mac/Linux
   venv\Scripts\activate     # для Windows
   
   3. Установите зависимости:
   
   pip install -r requirements.txt
   
   4. Настройте переменные окружения:
   Создайте файл .env в корне проекта и добавьте ваш API ключ:
   
   BINANCE_API_KEY=ваш_ключ_здесь
   
   5. Запустите сервер:
   
   uvicorn app.main:app --reload
   
   
## 📈 Тестирование (API Documentation)
После запуска перейдите в интерактивную документацию Swagger:
👉 http://127.0.0.1:8000/docs
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
