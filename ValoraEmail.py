from selenium import webdriver  #Importação de biblioteca
from selenium.webdriver.common.keys import Keys #Importação de biblioteca
from time import sleep #Importação de biblioteca
import pyautogui #Importação de biblioteca

options = webdriver.ChromeOptions() #Carregando opções do webdriver
options.add_argument("--kiosk") #Maximixando o webdriver

try:
    Chrome = webdriver.Chrome(chrome_options=options) #Definindo o webdriver
    Chrome.get('https://valora.cc/') #Get da URL
    sleep(2) #Timer

    Nome = Chrome.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input') #Procurando o elemento Nome do formulário
    Nome.send_keys('Carlos Vinicius de Jesus') #Preenchendo o atributo Nome

    NomeEmpresa = Chrome.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input') #Procurando o elemento Nome da Empresa do formulário
    NomeEmpresa.send_keys('Valora') #Preenchendo o atributo Nome da Empresa

    Email = Chrome.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/input') #Procurando o elemento Email do formulário
    Email.send_keys('teste@teste.com') #Preenchendo o atributo Email

    Telefone = Chrome.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/input') #Procurando o elemento Telefone do formulário
    Telefone.send_keys('11999999999') #Preenchendo o atributo Telefone

    Mensagem = Chrome.find_element_by_xpath('//*[@id="app"]/div[4]/div/textarea') #Procurando o elemento Mensagem do formulário
    Mensagem.send_keys('Sou o novo QA da VALORA :)') #Preenchendo o atributo Mensagem

    Enviar = Chrome.find_element_by_xpath('//*[@id="app"]/div[5]/div/a').click() #Procurando o elemento botão Enviar do formulário e clicando

    sleep(3) #Timer
    Envio = Chrome.find_element_by_class_name('t5')
    capturar = pyautogui.screenshot()#Evidência que o email foi enviado
    capturar.save('EmailEnviado.png')#Salvando o print

    print('\n','='*51, '\n  Email enviado com sucesso! Verifique a evidência.','\n', '='*51) #Print informando que o e-mail foi enviado

except Exception:
    capturar2 = pyautogui.screenshot()#Evidência de erro
    capturar2.save('ERRO - Email.png')#Salvando o print
    print('\n','='*75, '\n  Não foi possível enviar o email, verifique sua conexão e tente novamente.','\n', '='*75) #Print informando o erro

sleep(5) #Timer
Chrome.quit() #Fechando o webdriver
