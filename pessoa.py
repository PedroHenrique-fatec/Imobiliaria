# Classe Pessoa()
class Pessoa():
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
    def atualizar_pessoa(self, novo_nome = None, novo_telefone = None, novo_email = None, novo_endereco = None):
        if novo_nome is not None:
            self.nome = novo_nome
        if novo_telefone is not None:
            self.telefone = novo_telefone
        if novo_email is not None:
            self.email = novo_email
        if novo_endereco is not None:
            self.endereco = novo_endereco
            
# Classe Cliente(), herança da classe Pessoa()
class Cliente(Pessoa):
    def __init__(self, id_cliente, nome, cpf, telefone, email, endereco, tipo_cliente):
        super().__init__(nome, telefone, email, endereco)
        self.id_cliente = id_cliente
        self.cpf = cpf
        self.tipo_cliente = tipo_cliente
    
    def atualizar_cliente(self, novo_id = None, novo_cpf = None, novo_tipo_cliente= None):
        super().atualizar_pessoa()
        if novo_id is not None:
            print(f"Não é possível alterar o ID")
        if novo_cpf is not None:
            print(f"Não é possível mudar o CPF")
        if novo_tipo_cliente is not None:
            self.tipo_cliente = novo_tipo_cliente
    
    def exibir_informacoes(self):
        print(f"O nome do cliente é {self.nome}, seu CPF é: {self.cpf} e ele é do tipo: {self.tipo_cliente}")
        
    def comprar_imovel(self, imovel):
        print(f"O cliente: {self.nome} comprou o imóvel {imovel.id_imovel} que se localiza no endereco {imovel.endereco}")
        
# Classe Funcionario, herança da classe Pessoa()
class Funcionario(Pessoa):
    def __init__(self, id_funcionario, nome, telefone, email, endereco, cargo):
        super().__init__(nome, telefone, email, endereco)
        self.id_funcionario = id_funcionario
        self.cargo = cargo
        
    def atualizar_funcionario(self, novo_id_funcionario = None, novo_cargo = None):
        super().atualizar_pessoa()
        if novo_id_funcionario is not None:
            print("Não é possivel alterar o id do funcionario")
        if novo_cargo is not None:
            self.cargo = novo_cargo
            
    def vender_imovel(self, cliente, imovel):
        print(f"O funcionario {self.nome} de identificação {self.id_funcionario}, vendeu o imovel {imovel.id_imovel} para o cliente {cliente.nome}")
        imovel.atualizar_status = "vendido"