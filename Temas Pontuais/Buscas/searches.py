class Searches():
    def binary_search(self, lists, searched_num):
        '''
        Implementação de busca binária.
        Entrada: Lista
        Saída: Valor buscado
        '''

        lists = sorted(lists)

        for searched in range(len(lists)):
            if len(lists) == 1:
                if searched_num == lists[searched]:
                    return print('Number found. Position: {}'.format(lists[searched]))
                return print('Number not found')

            # if searched_num == lists[0]:
            #     return lists.index()
            # else


if __name__ == '__main__':
    buscas = Searches()
    lista1 = [56]
    lista2 = [56, 7, 12, 9, 80, 22, 54, 16, 478, 148, 48, 15, 87, 88]
    buscas.binary_search(lista1, 56)
