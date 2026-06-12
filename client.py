
import logging
from binance.um_futures import UMFutures

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.client = UMFutures(
            key=api_key,
            secret=api_secret,
            base_url="https://testnet.binancefuture.com"
        )
        self.log = logging.getLogger(__name__)

    def place_order(self, **params):
        self.log.info("Request: %s", params)
        response = self.client.new_order(**params)
        self.log.info("Response: %s", response)
        return response
