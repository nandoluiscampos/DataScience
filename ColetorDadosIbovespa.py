import pyautogui
import time
import pyperclip
from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd

pyautogui.PAUSE=1
#vai começar
# opção 1 - abrir navegador novo e entrar no chrome
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
# opção 2 abrir nova aba
#pyautogui.hotkey("ctrl" , "t")
#colar endereço site
link = "http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-de-derivativos/contratos-em-aberto/por-tipo-de-participante/"
pyperclip.copy(link)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("Enter")
time.sleep(8)
pyautogui.hotkey("ctrl", "f")
pyautogui.write("MERCADO FUTURO DE IBOVESPA")
time.sleep(2)
# DAR CINCO CLICKS
pyautogui.click(1354, 719, clicks=5)
time.sleep(2)
#copiar os dados
pyautogui.click(699, 561, clicks=2)
pyautogui.hotkey("ctrl","c")
time.sleep(2)
#abrir a calculadora
pyautogui.press("winleft")
time.sleep(2)
pyautogui.write("calculadora")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("ctrl","v")
#pegar o outro dado
pyautogui.click(1066, 561, clicks=1)
time.sleep(1)
pyautogui.click(1066, 561, clicks=2)
pyautogui.hotkey("ctrl","c")
#voltar na calculadora # ARRUMAR O TAB QUANDO TUDO ESTIVER PRONTO
time.sleep(1)
pyautogui.hotkey("alt","tab")
time.sleep(1)
pyautogui.press("-")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
pyautogui.hotkey("ctrl","c")
pyautogui.click(1066, 561, clicks=1)

#Mandar o resultado para o telegram dos estrangeiros
pyautogui.hotkey("ctrl" , "t")
pyautogui.click(963, 84, clicks=1)
time.sleep(5)
pyautogui.click(591, 684, clicks=1)
pyautogui.hotkey("ctrl","v")
texto = f"""
Resultado da posição dos estrangeiros!!
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", 'v')
pyautogui.press("enter")
# baixar a planilha dos indices mundiais
pyautogui.hotkey("ctrl" , "t")
link = "https://br.investing.com/indices/major-indices"
pyperclip.copy(link)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("Enter")
time.sleep(15)
pyautogui.hotkey("ctrl" , "f")
pyautogui.write("baixar dados")
time.sleep(1)
pyautogui.hotkey("ctrl" , "enter")
pyautogui.click(1354, 717, clicks=8)
time.sleep(2)
pyautogui.click(774, 491, clicks=1)
time.sleep(3)
pyautogui.click(1345, 697, clicks=1)
dados = pd.read_csv(r"C:/Users/nando/Downloads/Principais Índices Mundiais.csv")
resultado = dados['Variação'].sum() / 100   # soma do valor
print(resultado )
pyperclip.copy(resultado)
pyautogui.hotkey("ctrl","t")
time.sleep(1)
pyautogui.write("https://web.telegram.org/z/")
time.sleep(1)
pyautogui.hotkey("Enter")
time.sleep(5)
pyautogui.click(591, 684, clicks=1)
time.sleep(1)
pyautogui.hotkey("ctrl","v")
time.sleep(1)
texto = f"""
Porcentagem dos Indices Mundiais!!
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", 'v')
time.sleep(1)
pyautogui.press("enter")
#pegar os dados do us dollar
HEADERS = ({'user-agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})
html_completo = rq.get("https://br.investing.com/currencies/us-dollar-index", headers=HEADERS)
html_formatado = bs(html_completo.content)
#print(html_formatado.prettify())
nome_dolar = html_formatado.find("h1", class_="float_lang_base_1 relativeAttr").text
porcentagem = html_formatado.find("div", class_="top bold inlineblock").text
dados_dolar = nome_dolar + porcentagem
print( dados_dolar)
pyperclip.copy(dados_dolar)
time.sleep(1)
pyautogui.hotkey("ctrl","t")
time.sleep(1)
pyautogui.write("https://web.telegram.org/z/")
time.sleep(1)
pyautogui.hotkey("Enter")
time.sleep(5)
pyautogui.click(591, 684, clicks=1)
time.sleep(1)
pyautogui.hotkey("ctrl","v")
time.sleep(1)
texto = f"""
Variação do Dolar Futuro!!
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", 'v')
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
# mandando os links da noticia e calendario economico
pyautogui.click(591, 684, clicks=1)
pyautogui.write("https://br.investing.com/economic-calendar/")
time.sleep(1)
pyautogui.hotkey("Enter")
pyautogui.click(591, 684, clicks=1)
pyautogui.write("https://br.investing.com/news/")
time.sleep(1)
pyautogui.hotkey("Enter")
time.sleep(1)
# fechar o chrome
pyautogui.hotkey("alt", 'f4')
time.sleep(1)
pyautogui.hotkey("alt", 'f4')






