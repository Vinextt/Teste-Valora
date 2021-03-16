from time import sleep #Importação de biblioteca
reiniciar = '0' #Variavél passando valor padrão para iniciar o programa
while reiniciar != '2': #Estrutura de repetição
    print('{:=^40}'.format(' Teste Valora ')) #Título do programa
    print('{:*^40}'.format('\n Operações Disponíveis: ' '\n [ 1 ] Tempo de Buffer' '\n [ 2 ] Verificar Vídeo' '\n [ 3 ] Envio de Email' '\n [ 4 ] Check de Arquivos')) #Menu de escolhas    
    menu = str(input("\nQual Operação? ")) #usuário deve escolher uma opção do menu

    if menu == '1':
        from ValoraTempoBuffer import *
        
    elif menu == '2':
        from ValoraVideo import *

    elif menu == '3':
        from ValoraEmail import *

    elif menu == '4':
        from ValoraNetwork import *

    #Reiniciar ou finalizar
    reini = 0 #Variável
    while reini != 2: #Estrutura de repetição
        reiniciar = str(input('\nDeseja realizar outra operação? [ 1 ] Sim [ 2 ] Não : ')) #Usuário deve escolher uma opção do menu
        if reiniciar == '1': #Condição
            sleep(1) #Temporizador
            print('\n Reiniciando... \n ') #Mostra na tela
            sleep(1) #Temporizador
            reini = 2 #Variável
        elif reiniciar == '2': #Condição
            reini = '2' #Variável
            sleep(1) #Temporizador
            print('\nAté logo!\n') #Mostra na tela
            sleep(1) #Temporizador
            import sys #Importação de biblioteca
            sys.exit() #Finaliza o programa
        else: #Condição
            print('\nOpção Inválida') #Mostra na tela
            reini = 1 #Variável
