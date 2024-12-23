# Register 100 Users Selenium 

# Configuração do Ambiente para o Projeto

Este projeto consiste em um cadastro automatizado de 100 usuários utilizando o framework Selenium e uma base de dados em Excel já criada. Abaixo estão as instruções para configurar o ambiente virtual e instalar as dependências.

## Pré-requisitos

Certifique-se de ter instalado:
- [Python 3.7+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)

---

## Passo a Passo para Configurar o Ambiente

### 1. Clonar o Repositório
Primeiro, faça o clone deste repositório no seu computador:

git clone https://github.com/LucasQuintela23/Register100UsersSelenium.git

cd Register100UsersSelenium




### 2. Criar e Ativar um Ambiente Virtual

#### No Windows:

python -m .venv venv

.venv\Scripts\activate


#### No macOS/Linux:

python3 -m venv venv
source venv/bin/activate

### 3. Instalar Dependências

pip install -r requirements.txt

### 4. Uso do Projeto

Execute o arquivo 100cadastros.ipynb para iniciar os testes.

Obs: Caso queria gerar um arquivo novo de base de dados, basta deletar o arquivo usuarios.xlsx, logo em seguida execute o arquivo GeradorEmail.py para ter uma nova base de dados.