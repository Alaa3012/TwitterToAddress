import os
from dotenv import load_dotenv
load_dotenv()
import csv
import time

import json

from moralis import evm_api

api_key = os.getenv('API_KEY')

def getOwner(params) : 
    result = evm_api.nft.get_nft_metadata(
        api_key=api_key,
        params=params,
    )
    return result