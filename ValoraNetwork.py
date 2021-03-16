from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
import requests

options = webdriver.ChromeOptions() #Carregando opções do webdriver
options.add_argument("start-maximized") #Maximixando o webdriver

try:
    Chrome = webdriver.Chrome(chrome_options=options)
    Chrome.get('https://hml-axa.sommacloud.com:8443/PortalHomolog/Base/Login/LoginPortal.aspx')#Endereço aonde o vídeo está hospedado
    Var = requests.get('https://hml-axa.sommacloud.com:8443/PortalHomolog/Base/Login/LoginPortal.aspx') 
    print('\n','='*29, '\n  Aba Network ok; Status ', Var.status_code, '\n', '='*29)
except Exception:
    print('\n','='*75, '\n  Validação da aba Network falhou, verifique sua conexão e tente novamente.','\n', '='*75)
    capturar3 = pyautogui.screenshot()#Evidência de erro
    capturar3.save('ERRO - Network.png')#Salvando o print
Chrome.quit()
sleep(3)
