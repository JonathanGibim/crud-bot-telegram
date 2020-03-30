## 🤖 Projeto

O  projeto é baseado em um único crud para a realização de cadastro de comandos visando agilizar o processo de criação
de um bot no telegram.</br>
Entenda melhor o funcionamento do [BOT](https://github.com/WesleyPestana/bot-telegram-devs) aqui!

## 🤔 Como rodar

- Faça o download desse repositório;
- Instale e ative sua virtualenv: `python -m venv venv`  `venv/scripts/activate` ou `venv/bin/activate`;
- Instale as dependências: `pip install -r requirements.txt`;
- Configure o local de seu banco de dados no caminho: `src/conf/.env`
- Configure o arquivo settings.py referenciando as variaveis de ambiente definidas na etapa anterior;
- Por fim, aproveite: `python app.py`;

## 🚀 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias e bibliotecas:

- [Python](https://docs.python.org/pt-br/3/index.html)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [DotEnv](https://pypi.org/project/python-dotenv/)

## 📝 Observações

É preciso bastante cuidado com o preenchimento do campo Scripts dentro do crud, pois apesar de sua capacidade de uso ser
extremamente vasta, é perigosa!

- Caso ainda não tenha o banco de dados criado, execute: `python _database_.py`. Isso irá criá-lo no mesmo diretório do arquivo executado;

- Assista ao vídeo explicação para cessar outras dúvidas: [Vídeo](https://www.youtube.com/watch?v=40KhPfAmLWo)