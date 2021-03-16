from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

options = webdriver.ChromeOptions() #Carregando opções do webdriver
options.add_argument("--kiosk") #Maximixando o webdriver

try:
    Chrome = webdriver.Chrome(chrome_options=options)
    Chrome.get('https://valora.cc/video/video.mp4')#Endereço aonde o vídeo está hospedado
    sleep(3) #temporizador para carregar a página
    video = Chrome.find_element_by_xpath("/html/body/video") #Elemento Web que representa o player
    video.click() # foi colocado um click para pausar o vídeo e mostrar o tempo de reprodução
    sleep(0.3) #temporizador para não abrir o player do vídeo em tela cheia
    video.click() #start no vídeo

    capturar = pyautogui.screenshot() #Print com do vídeo rodando
    capturar.save('InicioVideo.png') #Salvando o print

    sleep(61)

    video.click()
    sleep(0.3)
    video.click()

    capturar2 = pyautogui.screenshot()#Evidência que o vídeo carregou até o final
    capturar2.save('FinalVideo.png')#Salvando o print
    print('\n','='*62, '\n  O vídeo foi carregado corretamente, verifique as evidências.','\n', '='*62)

    
except Exception:
    print('\n','='*78, '\n  Não foi possível verificar o vídeo, verifique sua conexão e tente novamente.','\n', '='*78)
    capturar3 = pyautogui.screenshot()#Evidência de erro
    capturar3.save('ERRO - Video.png')#Salvando o print
Chrome.quit()