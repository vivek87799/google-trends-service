#!/usr/bin/env python3

from pathlib import Path
import logging
import pandas as pd
from pytrends.request import TrendReq
from typing import List

from config import Parameters
from helper_functions import log

Path(Parameters.LOG_FILE_PATH).mkdir(parents=True, exist_ok=True)    
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(Parameters.LOG_FILE_NAME, Parameters.LOG_FILE_MODE)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

class GoogleTrendsService:
    """
    A class to connect to the Google Trends API 

    ...

    Attributes
    ----------
    hl : str
        host language
    tz : int
        time zone
    age : int
        age of the person

    Methods
    -------
    build_payload(hl, tz):
        Sets the search interest
    get_data():
        Gets the queried data as pandas dataframe
    """

    @log
    def __init__(self, hl: str=Parameters.LANGUAGE, tz=Parameters.TIME_ZONE) -> None:
        """
        Initializes the connection to pytrends API
        """
        self.pytrends_connection = TrendReq(hl=hl, tz=tz)
    
    @log
    def build_payload(self, kw_list: List[str], timeframe: str) -> None:
        """
        Sets the search interest

        Attributes
        ----------
        kw_list : str
            list of keyword to be queried upon
        timeframe : str
            time frame between which the data is queried upon
        """
        self.pytrends_connection.build_payload(kw_list=kw_list, timeframe=timeframe)
    
    @log
    def get_data(self) -> pd.DataFrame:
        """
        Retrives the query set using the build_payload as pandas dataframe
        """
        return self.pytrends_connection.interest_over_time()
    
    @log
    def run_manager(self) -> None:
        """
        Runs the service to retirive the data for the requested period
        """
        self.pytrends_connection.build_payload(kw_list=Parameters.KW_LIST, timeframe=Parameters.TIMEFRAME)
        self.get_data()


if __name__ == "__main__":
    trendsAPI = GoogleTrendsService()
    trendsAPI.run_manager()
