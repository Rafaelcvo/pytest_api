
# Testes de API com FastAPI

Este repositório contém uma prova de conceito (POC) para testes de API usando FastAPI. Ele inclui exemplos de testes unitários, de integração, de cobertura e de carga, utilizando diversas ferramentas populares.

## Estrutura do Projeto

- `app/`: Contém o código da API FastAPI.
- `tests/`: Contém os testes automatizados para a API.
- `load_tests/`: Scripts para testes de carga usando Locust.

## Ferramentas Utilizadas

- **FastAPI**: Framework para construção de APIs em Python.
- **pytest**: Framework de testes para Python.
- **pytest-cov**: Plugin para medir a cobertura de testes.
- **Postman**: Ferramenta para teste manual e automação de testes de API.
- **Locust**: Ferramenta para testes de carga.

## Configuração do Ambiente

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/testes-api-fastapi.git
    cd testes-api-fastapi
    ```

2. **Crie um ambiente virtual e instale as dependências**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scriptsctivate`
    pip install -r requirements.txt
    ```

3. **Execute a aplicação**:
    ```bash
    uvicorn app.main:app --reload
    ```

## Executando os Testes

### Testes Unitários e de Integração

Para executar os testes unitários e de integração, utilize o `pytest`:
```bash
pytest
```

### Teste de Cobertura

Para verificar a cobertura dos testes, utilize o `pytest-cov`:
```bash
pytest --cov=app tests/
```

Para gerar um relatório de cobertura em HTML:
```bash
pytest --cov-report html --cov=app tests/
```

### Testes de Carga

Para executar os testes de carga, primeiro inicie o Locust:
```bash
locust -f load_tests/locustfile.py
```

Em seguida, abra seu navegador e vá para `http://localhost:8089` para configurar e iniciar os testes de carga.

## Estrutura dos Testes

### Testes Unitários

Os testes unitários estão localizados no diretório `tests/` e testam funcionalidades isoladas da API. Exemplo:
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
```

### Testes de Integração

Os testes de integração verificam a interação entre diferentes componentes da aplicação. Exemplo:
```python
def test_create_item():
    response = client.post("/items/", json={"name": "item1", "price": 10.5})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "item1"
    assert data["price"] == 10.5
```

### Testes de Carga

Os testes de carga estão configurados no arquivo `load_tests/locustfile.py`. Exemplo:
```python
from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000
```

## Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [Locust Documentation](https://locust.io/)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
