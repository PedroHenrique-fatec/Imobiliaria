# Importando as classes Imovel(), Cliente() e Funcionario() dos arquivos externos
from imovel import Imovel
from pessoa import Cliente, Funcionario

# Classe SistemaCadastro, que armazena as instancias criadas a partir das classes.
class SistemaCadastro():
    def __init__(self):
        self.imoveis = []
        self.clientes = []
        self.funcionarios = []
        
    def cadastrar_cliente(self, id_cliente, nome, cpf, telefone, email, endereco, tipo_cliente):
        novo_cliente = Cliente(id_cliente, nome, cpf, telefone, email, endereco, tipo_cliente)
        self.clientes.append(novo_cliente)
        print(f"Cliente {nome} cadastrado com sucesso")
    
    def cadastrar_funcionario(self, id_funcionario, nome, telefone, email, endereco, cargo):
        novo_funcionario = Funcionario(id_funcionario, nome, telefone, email, endereco, cargo)
        self.funcionarios.append(novo_funcionario)
        print(f"Funcionario {nome} cadastrado com sucesso")
        
    def cadastrar_imovel(self, id_imovel, endereco, area, valor, status):
        novo_imovel = Imovel(id_imovel, endereco, area, valor, status)
        self.imoveis.append(novo_imovel)
        print(f"Imóvel {id_imovel} cadastrado com sucesso")