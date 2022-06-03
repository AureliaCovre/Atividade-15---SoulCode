class Funcionarios:
    """Construtor da classe Funcionarios. 
    
        Args:
           
            
    """   
    #Criando a função cadastro de funcionarios
    def cadastro_funcionario(self):
        funcionarios = []
        
        for i in range(1):
                   
            matricula = input("Insira a Matricula: ")
            funcionario = input("Nome do funcionario: ")
            cargo = input("Função: ")
            
            funcionarios.append(matricula)
            funcionarios.append(funcionario)
            funcionarios.append(cargo)
            print("Informações do funcionario. Matricula: ", matricula,"/ Nome Funcionario: ", funcionario,"/ Cargo: ", cargo)   
        
            # # Criando o loop para voltar o menu ao finalizar um cadastro
            # continua = input("Deseja efetuar outro cadastro?  Se sim, digite S ").upper()
            # if continua != "S":
            #     break
                
