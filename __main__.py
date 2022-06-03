from modules.vendas import Vendas
from modules.produtos import Produto
from modules.funcionarios import Funcionarios
from modules.clientes import Cliente
from datetime import timedelta, date
import time
import os #utilizado antes do menu(linha12) para limpar o terminal

if __name__ == '__main__':
    try:
        while True:
            os.system('cls')
            selecao = input("1. Cadastro de Cliente\n"
                        "2. Cadastro de Funcionarios\n"  
                        "3. Cadastro de Vendas\n"  
                        "Ou Digite qualquer outro valor para sair...  ")
            if selecao == '1':
                cadastro = Cliente() #chamando a classe Cliente
                cadastro.cadastro()  #chamando a função cadastro de cliente
                time.sleep(3)  # Ajustando o tempo para rodar o terminal
            if selecao == '2':
                cadastro = Funcionarios()   #chamando a classe Funcionarios
                cadastro.cadastro_funcionario()   #chamando a função cadastro de funcionarios
                time.sleep(3)       
            if selecao == '3':
                cadastro = Vendas()   #chamando a classe Vendas
                cadastro.cadastro()   #chamando a função cadastro de cliente
                cadastro.cadastro_produto()  #chamando a função cadastro de produto
                time.sleep(3) 
            else:
                break       
    except Exception as e:
        print(str(e))   
