def busca_binaria(lista_numeros, numero_alvo):
      
    inicio_lista = 0
    fim_lista = len(lista_numeros)
    tentativa = 1

    while fim_lista > inicio_lista:
        aux = (inicio_lista + fim_lista) // 2
        valor_atual = lista_numeros[aux]

        if valor_atual == numero_alvo:
            print(f"Numero do indice: {aux}\nTentativas: {tentativa}")
            return aux
            
        elif valor_atual > numero_alvo:
            fim_lista = aux - 1

        elif valor_atual < numero_alvo:
            inicio_lista = aux + 1

            tentativa += 1

        return print("Numero nao encontrado!\n")


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_alvo = 6

busca_binaria(lista_numeros, numero_alvo)
