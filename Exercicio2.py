class Contato:
    def __init__(self, nome, numero):
         self.nome = nome 
         self.numero = numero

class Agenda:
    def __init__(self, contato = []):
        self.contato = []

    def add_lista(self, item_adicionado):
        self.contato.append(item_adicionado)


def main():
    contatoObj1 = Contato('Julia Sapatona', 1169696969)
    contatoObj2 = Contato('Lucas Nãobinárie', 116666666)
    contatoObj3 = Contato('Luan viadinho', 115454545454)
    contatoObj4 = Contato('Joca Kenga', 116966669)

    agendaObj = Agenda([])
    agendaObj.add_lista(contatoObj1)
    agendaObj.add_lista(contatoObj2)
    agendaObj.add_lista(contatoObj3)
    agendaObj.add_lista(contatoObj4)

    print(f'Nome: {agendaObj.contato[0].nome}, Número: {agendaObj.contato[0].numero}')
    print(f'Nome: {agendaObj.contato[1].nome}, Número: {agendaObj.contato[1].numero}')
    print(f'Nome: {agendaObj.contato[2].nome}, Número: {agendaObj.contato[2].numero}')
    print(f'Nome: {agendaObj.contato[3].nome}, Número: {agendaObj.contato[3].numero}')



if __name__ == '__main__':
    main()


