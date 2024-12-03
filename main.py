import MySQLdb
from hashlib import sha256


def conexao_banco_de_dados():
    return MySQLdb.connect(host="localhost", user="leogo", passwd="luaneleo", db="cliente")


# Função para verificar se o usuário existe no banco de dados
def verificar_usuario(nome):
    try:
        conexao = conexao_banco_de_dados()
        cursor = conexao.cursor()
        comando = "SELECT 1 FROM clientes WHERE nome = %s"
        cursor.execute(comando, (nome,))
        resultado = cursor.fetchone()

        return resultado is not None  # Retorna True se o usuário existir, caso contrário False
    except MySQLdb.Error as erro:
        print(f"Erro ao verificar usuário: {erro}")
        return False


# Função para pegar a senha do banco
def pegar_senha(nome):
    try:
        conexao = conexao_banco_de_dados()
        cursor = conexao.cursor()
        comando = "SELECT senha FROM clientes WHERE nome = %s"
        cursor.execute(comando, (nome,))
        resultado = cursor.fetchone()

        return resultado[0] if resultado else None  # Retorna a senha ou None se o usuário não for encontrado
    except MySQLdb.Error as erro:
        print(f"Erro ao pegar senha: {erro}")
        return None


# Função de cadastro de usuário
def cadastrar():
    print("Cadastrar Usuario")
    conexao = conexao_banco_de_dados()
    cursor = conexao.cursor()
    nome = input("Digite seu usuario: ").strip()
    senha = input("Digite sua senha: ").strip()

    # Gerando hash da senha
    hash_senha = sha256(senha.encode()).hexdigest()

    comando = "INSERT INTO clientes (nome, senha) VALUES (%s, %s)"
    valores = (nome, hash_senha)
    cursor.execute(comando, valores)
    conexao.commit()
    print("Cadastrado com sucesso!")
    cursor.close()
    conexao.close()


# Função de login
def login():
    print("Entrar na conta")
    nome = input("Digite seu usuario: ").strip()

    # Verificando se o usuário existe antes de buscar a senha
    if not verificar_usuario(nome):
        print("Usuário não encontrado.")
        return

    senha = input("Digite sua senha: ").strip()
    senha_hash = sha256(senha.encode()).hexdigest()

    # Pegando a senha do banco para comparação
    senha_banco = pegar_senha(nome)

    if senha_banco and senha_hash == senha_banco:
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta.")


cadastrar()
# Exemplo de uso
login()
