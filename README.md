### Introdução
Api construída com intuito de resgatar os 10 hits mais famosos de um artista utilizando a API Genius.

### Tecnologias utilizadas nesse projeto:
- Python
- Flask
- DynamoDB
- Redis

### Requesitos para o funcionamento da API:
- Faz-se necessário ter instalado o redis na sua máquina e o mesmo está em execução.
- Ter uma conta AWS.
- Preencher os seguintes campos com suas credenciais da AWS:
``` sh
ACCESS_KEY_ID=
ACCESS_SECRET_KEY=
```
Obs: Os campos se encontram no .env.

- Para realizar a instalação das bibliotecas utilizadas, digite:
``` sh
pip install -r requeriments.txt
```
- Após a realziação das etapas passadas, basta utilizar o comando abaixo para começar a consumir a API.
``` sh
flask run
```

### Como utilizar/consumir
- Existe apenas uma rotae a mesma utiliza o métoodo POST. A seguir um exemplo da rota:
``` sh
http://127.0.0.1:5000/api/v1/captura/artista
```
- O body da requisição deve ser enviado como um form-data e possuir os seguintes parâmetros:
``` sh
{
  "nome_artista": nome_do_artista
}
``` 
- Para a não utilização do cache, deve-se enviar como QueryString na url como no exemplo a seguir:
``` sh
http://127.0.0.1:5000/api/v1/captura/artista?cache=False
``` 
