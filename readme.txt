Configurando o ambiente para Python e Selenium:

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

Opção 1 = ValoraTempoBuffer; Verifica se o site da valora.cc carrega em menos de 1.5s e informa na tela se a validação foi feita de acordo com o tempo previsto.
caso queira executar esse teste separadamente, execute o arquivo "ValoraTempoBuffer.py".

Opção 2 = ValoraVideo; Acessa a url aonde o vídeo está hospedado, informa na tela que o foi carregado corretamente e cria duas evidências 
"InicioVideo.png" e "FinalVideo.png", caso não encontre o vídeo é informado na tela e cria a evidência "ERRO - Video.png"; caso queira executar esse teste separadamente, execute o arquivo "ValoraVideo.py".

Opção 3 = ValoraEmail; Acessa o formulário e preenche as informações, aguarda o retorno em tela para validar se o e-mail foi enviado, em caso de sucesso é criado a evidência "EmailEnviado.png" caso o contrário 
é criada a evidência "ERRO - Email";
caso queira executar esse teste separadamente, execute o arquivo "ValoraEmail.py".

Opção 4 = ValoraNetwork; Verifica os requests realizado na página na da Valora e em caso de sucesso é informado na tela que o status é 200 OK e em caso de erro é informado que não foi possível validar e cria
a evidência "ERRO - Network"
caso queira executar esse teste separadamente, execute o arquivo "ValoraNetwork.py".

----------------------------------------------------------------------------------------------------------

Postman:

Abra o Postman > File > Import > File > Selecione a collection "Teste Valora.postman_collection.json";

[POST] Inserir: Insere um funcionário na base com as infos; Nome; Salário; Idade;

[GET] Update: Realiza atualizações no cadastro com base no ID informado no endpoint. Ex: http://dummy.restapiexample.com/api/v1/update/COLOQUEAQUIID

[GET] Consulta: Informa se o cadastro com base no ID informado no endpoint se está ativo. Ex: http://dummy.restapiexample.com/api/v1/employee/COLOQUEAQUIID

[DELETE ]Delete: Remove o cadastro da base com base no ID informado no endponint. Ex: http://dummy.restapiexample.com/api/v1/delete/COLOQUEAQUIID