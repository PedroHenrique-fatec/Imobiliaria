# Importando a classe SistemaCadastro() de um arquivo externo
from sistema_cadastro import SistemaCadastro

sistema = SistemaCadastro()

sistema.cadastrar_cliente(1, "Lara", "123465789-32", "(12) 99652-1245", "lara.cliente@gmail.com", "Jardim Primavera, Lorena", "comprador")
sistema.cadastrar_funcionario(1, "Roberto", "(12) 77496-5584", "roberto.funcionario@gmail.com", "Nova Estrela, Cachoeira Paulista", "Corretor")
sistema.cadastrar_imovel(1, "Bola de Cristal, Nova York", 25, 450000, "disponivel")

sistema.funcionarios[0].vender_imovel(sistema.clientes[0], sistema.imoveis[0])
