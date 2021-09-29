import logging
import requests
import pytest
import pandas as pd

log = logging.getLogger(__name__)



def get_dataframe(stream,file):
    if stream.lower() == 'input':
        file_name = f"data/{file.lower()}_input.csv"
        try:
            df = pd.read_csv(file_name)
            log.info("INPUT data fetched.")
            return df
        except:
            log.error(f"File Not Found for {stream}")
            assert False
        
    elif stream.lower() == 'memory':
        file_name = f"data/{file}_memory.txt"
        url = ""
        try:
            with open(file_name) as f:
                url = f.readline().strip()
            
            req = requests.get(url)

            with open(f"data/temp_{file}_memory.txt","w") as f:
                f.write(req.text)
            df = pd.read_csv(f"data/temp_{file}_memory.txt")
            log.info("MEMORY data fetched.")
            return df
        except:
            log.error(f"Unable to feth data for {stream}")
            assert False
        

    elif stream.lower() == 'output':
        file_name = f"data/{file.lower()}_output.csv"
        try:
            df = pd.read_csv(file_name)
            log.info("OUTPUT data fetched.")
            return df
        except:
            log.error(f"File Not Found for {stream}")
            assert False

@pytest.fixture
def context():
    return {}




