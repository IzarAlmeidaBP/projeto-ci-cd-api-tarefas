# Projeto: API de Tarefas com Pipeline CI/CD

Este repositório contém o código-fonte de uma API de tarefas simples, desenvolvida em Python com Flask, como parte do projeto da disciplina "Elaborar um pipeline CI-CD para Cloud Computing" da UNIFACISA.

O objetivo principal é demonstrar a configuração e execução de um pipeline de Integração Contínua (CI) utilizando GitHub Actions.

## Como Executar o Projeto Localmente

Para executar a aplicação em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/seu-usuario/projeto-ci-cd-api-tarefas.git](https://github.com/seu-usuario/projeto-ci-cd-api-tarefas.git)
    cd projeto-ci-cd-api-tarefas
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    # Crie o ambiente
    python -m venv venv
    # Ative o ambiente (Linux/macOS)
    source venv/bin/activate
    # Ou (Windows)
    # venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**

    ```bash
    python app.py
    ```

5.  Acesse a API em `http://127.0.0.1:5000` no seu navegador ou ferramenta de API.

## Pipeline de CI/CD

Este projeto utiliza GitHub Actions para automação. O pipeline é acionado a cada `push` ou `pull request` para a branch `main` e executa as seguintes etapas:

- Checkout do código
- Configuração do ambiente Python
- Instalação de dependências
- Execução de testes unitários
