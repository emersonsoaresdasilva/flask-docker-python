<h1><img src = "https://i.imgur.com/LU5JMsE.png" width="20%"/></h1>

<strong>Docker</strong> é um conjunto de produtos de plataforma como serviço que usam virtualização de nível de sistema operacional para entregar software em pacotes chamados contêineres. 

Os contêineres são isolados uns dos outros e agrupam seus próprios softwares, bibliotecas e arquivos de configuração.

### Ferramentas utilizadas:
- Python. 🐍
- Flask. 🌶️
- Docker. 🐋

### Brincar com Docker:

- Cadastre-se: https://labs.play-with-docker.com/ ⤵
- Crie uma nova instância
- Em sua instância: <code>git clone https://github.com/emersonsoaresdasilva/flask-docker-python.git</code>
- <code>docker image build -t flask .</code>
- <code>docker run -p 5007:5000 -d flask</code>
- <code>docker ps</code> ✔

### Executar aplicação local:
<code>python -m venv venv</code> ⤵

<code>venv\Scripts\activate</code>

<code>pip install -r requirements.txt</code>

<code>python app.py</code> ✔

### Requisitos para utilizar os scripts:
- [x] Ter o Python 3 instalado na máquina.
- [x] Saber lidar com venv e instalar as dependencias a partir do requirements.txt