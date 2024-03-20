import os
import requests
import logging

# Create a custom logger
logger = logging.getLogger(__name__)
# Create a file handler
#handler = logging.FileHandler('app.log')
# Add the handler to the logger
#logger.addHandler(handler)

def get_company_info(company_stock_ticker: str, question: str): 
    api_key = "0slxspiAvFd9w6xrvw1RTcAP1wnd13QH"        
    url = "https://hackathon-ai-search-pf.canadaeast.inference.ml.azure.com/score"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
        'azureml-model-deployment': 'hackathon-ai-search-pf-1'
    }       
    payload = {
        'client': company_stock_ticker,
        'question': question
    }

    logger.info(f"Getting company information at {url}")
    response = requests.post(url, json=payload, headers=headers)

    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        chunks = [item['chunk'] for item in data['documents']]
        logger.info(f"Company info for {company_stock_ticker} found: {chunks}")
        #data = response.json()
        #logger.info(f"Company info for {company_stock_ticker} found: {data}")
        combined_chunks = ' '.join(chunks)
        return combined_chunks
    else:
        logger.info(f"Company info for {company_stock_ticker} not found") 
        return None 