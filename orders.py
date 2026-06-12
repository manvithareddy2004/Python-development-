
def create_order_payload(symbol, side, order_type, quantity, price=None):
    payload = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }
    if order_type == "LIMIT":
        payload["price"] = price
        payload["timeInForce"] = "GTC"
    return payload
