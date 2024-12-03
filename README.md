
Sistema de login e cadastro com criptografia simples


um sistema onde você consegue se cadastrar e enviar para o banco de dados, mas, a senha vai criptografada. o uso é bem simples, crie um db cliente e coloque suas informações na conexao com banco de dados.


crie a tabela clientes com os dados ID, NOME E SENHA, para que funcione corretamente o codigo.

Criando a tabela: 

CREATE DATABASE cliente;

USE cliente;

CREATE TABLE clientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    senha VARCHAR(256) NOT NULL
);
