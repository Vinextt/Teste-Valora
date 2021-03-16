
Configurando o ambiente:

Realizar o download do Chrome Web Driver atualizado: (O Chrome da máquina precisa estar atualizado também:)
https://chromedriver.chromium.org/downloads

[UBUNTU] abrir o terminal e instalar as seguintes extenções:
sudo apt install python3-pip
sudo apt-get install python-selenium
sudo apt-get install python-requests

[WINDOWS] abrir o CMD e instalar as seguintes extenções:
pip install --upgrade pip
pip install selenium
pip install requests

------------------------------------------------------------------------------------------------------------

Após a instalação das extenções, execute o arquivo "main.py";

Opção 1 = ValoraTempoBuffer, verifica se o site da valora.cc carrega em menos de 1.5s e informa na tela se a validação foi feita de acordo com o tempo previsto.
caso queira executar esse teste separadamente, execute o arquivo "ValoraTempoBuffer.py".

Opção 2 = ValoraVideo, acessa a url aonde o vídeo está hospedado, informa na tela que o foi carregado corretamente e cria duas evidências 
"InicioVideo.png" e "FinalVideo.png", caso não encontre o vídeo é informado na tela e cria a evidência "ERRO - Video.png"; caso queira executar esse teste separadamente, execute o arquivo "ValoraVideo.py".

Opção 3 = ValoraEmail
caso queira executar esse teste separadamente, execute o arquivo "ValoraEmail.py".!!!

Opção 4 = ValoraNetwork
caso queira executar esse teste separadamente, execute o arquivo "ValoraNetwork.py".