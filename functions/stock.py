import os
import requests
import logging

# Create a custom logger
logger = logging.getLogger(__name__)
# Create a file handler
#handler = logging.FileHandler('app.log')
# Add the handler to the logger
#logger.addHandler(handler)

def get_stock_info(stock_ticker: str):         
    source_url = os.getenv("STOCK_API_URL")    
    url = f"{source_url}/{stock_ticker}"  

    logger.info(f"Getting stock information at {url}")

    response = requests.get(url)   
    if response.status_code == 200:        
        data = response.json()
        logger.info(f"Stock info for {stock_ticker} found: {data}") 

        #msg = (f"application: {application}, host: {host}, jvm: {jvm}, ip: {ip}, port: {port}")   
        msg = data       
        return msg
    else:
        logger.info(f"Stock info for {stock_ticker} not found") 
        return None   