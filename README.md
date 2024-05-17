# P1-M10

# API de criação de pedidos

Esta é uma API desenvolvida em FastAPI para gerenciar pedidos com a criação de nome, email, e descrição. Ela utiliza um banco de dados local com o ORM Ormar.

## Funcionalidades

- **Pedidos**:
  - Criar novos pedidos (POST: /novo)
  - Atualizar pedidos existentes (PUT: /pedidos/{id})
  - Deletar pedidos (DELETE: /pedidos/{id})
  - Consultar pedidos por ID de usuário (GET: /pedidos/{id})
  - Consultar todos os pedidos (GET: /pedidos)

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Framework web assíncrono de alto desempenho para Python.
- [Ormar](https://collerek.github.io/ormar/): ORM (Object-Relational Mapping) para Python, projetado para funcionar perfeitamente com o FastAPI.
- [uvicorn](https://www.uvicorn.org/): Um servidor web ASGI de alto desempenho, construído sobre o asyncio do Python.
- [Python 3](https://www.python.org/): Linguagem de programação de alto nível amplamente utilizada.

## Estrutura de Pastas:
```
P1-M10
├── docker-compose.yaml
├── README.md
├── insomnia.json
├── app
    ├──.gitignore
    ├── main.py
    ├── models.py
    ├── schemas.py
    ├── init.py
    ├── db.py
    ├── requirements.txt
```

## Como Rodar o Projeto

1. **Instalação das Dependências**: Certifique-se de ter o Python 3 e o pip instalados em seu sistema. Em seguida, crie uma Venv em sua máquina:

```
python3 -m venv env
source env/bin/activate
```


e instale as dependências do projeto executando o seguinte comando no terminal:

   ```
   pip install -r requirements.txt
   ```

2. **Execução do Servidor**: Após instalar as dependências, você pode iniciar o servidor FastAPI executando o seguinte comando na raiz do projeto:

   ```
   python3 main.py
   ```
    Ou execute o seguinte comando para executar o docker-compose para também subir a aplicação:

    ```
    docker-compose up --build
    ```

   Isso iniciará o servidor na porta padrão `8000`. Você pode acessar a documentação da API em [http://localhost:8000/docs](http://localhost:8000/docs).

