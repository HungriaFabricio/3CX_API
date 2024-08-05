# %%
import requests, logging
from datetime import datetime

acess_token = "seu token de acesso aqui"
napikey = "sua api key aqui"
url = f"https://api.nvoip.com.br/v2/balance?napikey={napikey}"

headers = {
    "Authorization" : f"Bearer {acess_token}",
    "Content-Type": "application/json"
}

logger = logging.getLogger(datetime.today().strftime('%d-%m-%Y'))
logging.basicConfig(filename="3cx_saldo.log", level=logging.INFO)
response = requests.get(url, headers)

if response.status_code == 200:
    logger.info("Autenticação bem-sucedida")
    try:
        data = response.json()
        logger.info(data)  
    except ValueError:
        logger.info("Resposta não está em formato JSON")
        logger.info(response.text)  
else:
    logger.info(f"Erro na autenticação: {response.status_code}")
    logger.info(response.text) 

# %%
