class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque 

class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Pedido:
    def __init__(self, item = [], mtd_pag = 1):
        self.item = []

    def add_lista(self, item_adicionado):
        self.item.append(item_adicionado)
       
def main():

    mtd = int(input('1 - para dinheiro, 2 - para cheque, 3 - cartão '))
    if mtd == 1:
        print("Método dinehiro foi selecionado")
    elif mtd == 2:
        print('Método cheque foi selecionado')
    elif mtd == 3:
        print('Método dinheiro foi selecionado')
    else: print('Método inexistente')

    produtoObj1 = Produto('Mate Leão', 11.50, 23)
    produtoObj2 = Produto('Coca Cola', 5.25, 120)
    produtoObj3 = Produto('Pipoca', 5.40, 63)
    produtoObj4 = Produto('Erva tereré', 16.50, 38)

    itemObj1 = Item(produtoObj1, 6)
    itemObj2 = Item(produtoObj2, 4)

    pedidoObj1 = Pedido([], mtd)
    pedidoObj1.add_lista(itemObj1)
    pedidoObj1.add_lista(itemObj2)

    pedidoObj1.mtd_paga = mtd

    print(pedidoObj1.item[0].produto.nome)

if __name__ == '__main__':
    main()