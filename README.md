# Sistema de Imobiliária

Este é um sistema simples de gerenciamento de imóveis, clientes e funcionários, desenvolvido em Python utilizando os conceitos de Programação Orientada a Objetos (POO). O sistema permite cadastrar e gerenciar informações de imóveis, clientes e funcionários, além de permitir que os funcionários vendam imóveis para os clientes.

## Funcionalidades

- **Cadastrar Imóveis**: Permite adicionar novos imóveis ao sistema, informando ID, endereço, área, valor e status.
- **Cadastrar Clientes**: Permite adicionar novos clientes, informando ID, nome, CPF, telefone, email e endereço.
- **Cadastrar Funcionários**: Permite adicionar novos funcionários, informando ID, nome, telefone, email, endereço e cargo.
- **Vender Imóveis**: Os funcionários podem realizar a venda de imóveis para os clientes.

## Estrutura do Código

O sistema é composto pelas seguintes classes:

1. **Imovel**: Representa um imóvel, com atributos como ID, endereço, área, valor e status. Possui métodos para atualizar o status e exibir informações do imóvel.

2. **Pessoa**: Classe base que contém atributos comuns a pessoas, como nome, telefone, email e endereço. Possui métodos para atualizar as informações da pessoa.

3. **Cliente**: Herda da classe `Pessoa` e adiciona atributos específicos como ID do cliente, CPF e tipo de cliente. Possui métodos para atualizar informações e comprar imóveis.

4. **Funcionario**: Herda da classe `Pessoa` e adiciona atributos específicos como ID do funcionário e cargo. Possui métodos para atualizar informações e vender imóveis.

5. **SistemaCadastro**: Classe que gerencia as instâncias de imóveis, clientes e funcionários, permitindo cadastrar novos registros.

## Como Usar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
