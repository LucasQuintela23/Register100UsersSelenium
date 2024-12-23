# Cadastro de 100 usuários com Selenium

Este projeto realiza o cadastro automatizado de 100 usuários utilizando o framework Selenium e uma base de dados em Excel. Abaixo estão as instruções para configurar o ambiente e executar o projeto.

---

## **Pré-requisitos**

Certifique-se de ter os seguintes itens instalados no seu sistema:
- [Python 3.7 ou superior](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)

---
### **Bibliotecas utilizadas no Projeto** 
- **Selenium:** Para automação de navegador. 
- **Pandas:** Para manipulação e leitura de dados em Excel. 
- **Openpyxl:** Para manipulação de arquivos Excel. 
- **Numpy:** Para cálculos numéricos, caso necessário. 
## **Passo a Passo para Configurar o Ambiente** 

### **1. Clonar o Repositório**
Faça o clone deste repositório em seu computador e navegue até a pasta do projeto: 

```bash
git clone https://github.com/LucasQuintela23/Register100UsersSelenium.git
cd Register100UsersSelenium 
```





### 2. Criar e Ativar um Ambiente Virtual

#### No Windows:
```
python -m .venv venv

.venv\Scripts\activate
```

#### No macOS/Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```
pip install -r requirements.txt
```
### 4. Uso do Projeto

Execute o arquivo 100cadastros.ipynb para iniciar os testes.

Obs: Caso queria gerar um arquivo novo de base de dados, basta deletar o arquivo usuarios.xlsx, logo em seguida execute o arquivo GeradorEmail.py para ter uma nova base de dados.