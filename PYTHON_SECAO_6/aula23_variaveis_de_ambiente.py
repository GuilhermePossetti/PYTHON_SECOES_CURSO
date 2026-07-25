"""
Variáveis de ambientes com Python
Para variáveis de ambientes
Windows PS: $env:VARIAVEL="VALOR" | echo $VARIAVEL
Para obter o valor das variáveis de ambiente
os.getenv ou os.environ['VARIAVEL'] = 'valor'
Ou usando python-detenv e o arquivo .env
pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
OBS.: sempre lembre-se de criar um .env-example
"""
import os

print (os.getenv('SENHA'))