import random
import string
import pandas as pd

# Função para gerar e-mails aleatórios
def gerar_email():
    dominios = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    prefixo = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    dominio = random.choice(dominios)
    return f"{prefixo}@{dominio}"

# Função para gerar senhas aleatórias
def gerar_senha(tamanho=10):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(caracteres, k=tamanho))

# Gerar 100 e-mails e senhas
emails = [gerar_email() for _ in range(100)]
senhas = [gerar_senha() for _ in range(100)]

# Criar um DataFrame com os dados
dados = pd.DataFrame({
    "email": emails,
    "senha": senhas
})

# Salvar em um arquivo Excel
dados.to_excel("usuarios.xlsx", index=False)

print("100 e-mails e senhas gerados e salvos no arquivo 'usuarios.xlsx'.")
