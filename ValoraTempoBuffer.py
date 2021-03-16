from selenium.webdriver import Chrome #Importação de biblioteca
from time import sleep #Importação de biblioteca
from datetime import datetime #Importação de biblioteca

try:
    Chrome = Chrome() #Definindo o webdriver
    Chrome.get('https://valora.cc/') #Get da URL

    h1 = datetime.now() #Obtendo o horário do start do carregamento
    print (h1.hour,':', h1.minute , ':', h1.second) #Horário do start do carregamento
    Chrome.quit() #Fechando o webdriver

    h2 = datetime.now() #Obtendo o horário do termino do carregamento
    print (h2.hour,':', h2.minute , ':', h2.second) #Horário do termino do carregamento


    dif = h2.second - h1.second #Calculando o tempo de carregamento
    print('O buffer durou:', dif, 'segundos') #Resultado do tempo de carregamento


    if dif <= 1.5:
        print('O Tempo de carregamento ocorreu como previsto') #Se o tempo for menor ou igual a 1.5s, esse será a mensagem.
    else:
        print(':( o tempo de carregamento levou mais tempo do que queríamos') #Se o tempo for maior ou igual a 1.5s, esse será a mensagem.
    sleep(2) #Timer para olhar o resultado

except Exception:
    print('\n','='*94, '\n  Não foi possível verificar o tempo de carregamento, verifique sua conexão e tente novamente.','\n', '='*94)
    Chrome.quit()  
