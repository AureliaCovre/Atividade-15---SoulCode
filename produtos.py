
class Produto:
    """Construtor da classe Produto. Classe pai de clientes. """  
    estoque = 100
      
    #Criando a função cadastro de produtos
    def cadastro_produto(self):
        # Lista para armazenar os dados dos produtos
        produtos = []
        
        # Inserindo os produtos
        for i in range(1):
            codigo = input("Insira o código do produto: ")
            nome_produto = input("Insira o nome do produto: ")
                      
            
            # Acrescentando os produtos cadastrados na lista
            produtos.append(codigo)
            produtos.append(nome_produto)
            print("Informações do produto. Codigo:  ", codigo,"/ Nome produto: ", nome_produto, "/ Quantidade em estoque: ", self.estoque)
    
    # estamos guardando a informação do estoque    
    
    def set_estoque(self, estoque):
        try:
            self.estoque = estoque
        except Exception as e:
            print(str(e))
        
    def get_estoque(self):
        return self.estoque  
              
