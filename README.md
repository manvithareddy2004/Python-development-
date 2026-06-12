
# Binance Futures Testnet Trading Bot

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set credentials:
```bash
export BINANCE_API_KEY=your_key
export BINANCE_API_SECRET=your_secret
```

## Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

## Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 120000
```

## Assumptions
- Binance Futures Testnet account is active.
- API keys are valid.
- USDT-M Futures endpoint is used.
