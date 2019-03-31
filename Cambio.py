# download da biblioteca requests com comando do python pip install requests 

# Importar o metodo get da biblioteca requests

import requests
import json 
import pandas as pd
import decimal

url = "http://data.fixer.io/api/latest?access_key=d541bcc9ba5b3578fa954b76e7d7e33e"    # url é uma variavel
print("Acessando Base de Dados ..")
response = requests.get(url)
print(response)
if response.status_code == 200:
	print("Consegui acessa base de dados ")
	print("Buscando informações das moedas..")
	dados = response.json()                               #dados e uma variavel
	day = dados['date']
	print("Acessando dados do dia %s/%s/%s" % (day[8:], day[5:7],day[0:4]))
	print('Valor de 1 EURO   ', dados['rates']['EUR']) 
	print('Valor de 1 REAL   ', dados['rates']['BRL'])
	print('Valor de 1 DOLAR  ', dados['rates']['USD'])  
	print('Valor de 1 BITCON ', dados['rates']['BTC']) 
	euro_real   = round(dados['rates']['BRL'] / dados['rates']['EUR'],2)
	dollar_real = round(dados['rates']['BRL'] / dados['rates']['USD'],2)
	btc_real    = round(dados['rates']['BRL'] / dados['rates']['BTC'],2)
	print("Conversao de 1 EURO    para REAL ", "%.2f" % euro_real)
	print("Conversao de 1 DOLLAS  para REAL ", "%.2f" % dollar_real)
	print("Conversao de 1 BITCOIN para REAL ", "%.2f" % btc_real)
	df = pd.DataFrame({'Moedas ':['Euro', 'Dollar', 'Bitcoin'], 'Valores':[euro_real,dollar_real, btc_real]})
	df.to_csv("valores.csv", index=False, sep=";")
	print("Gerado arquivo no excel")
else:
	prin("Site com Problemas") 