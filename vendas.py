from modules.produtos import Produto
# from modules.clientes import Cliente

class Vendas(Produto):
    """Construtor da classe Vendas. Essa classe é herdeira da classe Cliente e Produto, pois esta
            herdando os atributos delas.
        Args:
           id_venda (string): Criando um item unico para identificar as vendas
           quantidade (string): necessario para controle de estoque
            
    """
    vendas = []
    
    # Definindo a função de cadastrar produtos
    def cadastro_produto(self):
        return super().cadastro_produto()
   
      
    # Criando a função cadastro de vendas
    def cadastro(self):
        # Criando uma lista para armazenar os cadastros
        vendas = []
        
        # Criando os inputs
        for i in range(1):
            id_venda = input("Insira o ID do venda: ")
            quantidade = int(input("Insira a quantidade: "))
         
            
        variavel = Produto()  #chamando a classe Produto  
        
        total_estoque = variavel.get_estoque() - quantidade
        print("Venda cadastrada com sucesso! O estoque atual é:  ", total_estoque)
             
        
        # Acrescentando os cadastros na lista
        vendas.append(id_venda)
        vendas.append(quantidade)
        print("Vendas realizadas! ID:  ", id_venda, "Quantidade: ", quantidade, "Total em estoque: ",total_estoque)
