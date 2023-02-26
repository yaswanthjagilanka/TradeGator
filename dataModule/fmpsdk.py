#!/usr/bin/env python3
import fmpsdk


apikey = "9afdc255a91421213e6ba9ad324ce36b"


symbol: str = "MSFT"
from_date: str = "20215-04-26"
to_date: str = "2020-07-26"
time_series: int = 5
time_delta: str = "5min"


class DataFmpsdk:

    def __init__(self,symbol) -> None:
        self.symbol = symbol

    def script_total_data(self,from_date,to_date,time_delta):
        self.data=fmpsdk.historical_chart(apikey=apikey, symbol=symbol, time_delta=time_delta,)
        pass

    def parse_data(self):
        pass

fmpsdk.historical_price_full(apikey=apikey, symbol=symbol, from_date=from_date, to_date=to_date,time_series=1000)