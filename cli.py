
import argparse
import os

from bot.client import BinanceFuturesClient
from bot.orders import create_order_payload
from bot.validators import validate_side, validate_order_type
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--order-type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    side = validate_side(args.side)
    order_type = validate_order_type(args.order_type)

    if order_type == "LIMIT" and args.price is None:
        raise ValueError("price required for LIMIT orders")

    client = BinanceFuturesClient(
        os.getenv("BINANCE_API_KEY"),
        os.getenv("BINANCE_API_SECRET")
    )

    payload = create_order_payload(
        args.symbol, side, order_type, args.quantity, args.price
    )

    print("Order Request:", payload)

    try:
        response = client.place_order(**payload)
        print("SUCCESS")
        print(response)
    except Exception as exc:
        print("FAILED:", exc)

if __name__ == "__main__":
    main()
