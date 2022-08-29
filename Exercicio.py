class Produto:
    def __init__(self, preco, estoque):
        self.preco = preco
        self.estoque = estoque 

    def pedido(self, item ):
        return item