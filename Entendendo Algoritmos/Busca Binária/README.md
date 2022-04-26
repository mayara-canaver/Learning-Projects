# Busca Binária!
## O que é?

Um algoritmo de busca simples que permite a localização de um determinado elemento em uma lista ordenada.

Ao invés de passar elemento por elemento e assim demorar bastante para encontrar o número escolhido (no pior caso sendo o último), ele simplesmente encontra o meio da lista e vê para qual das duas metades o número possa estar, fazendo isso repetidamente até finalmente encontrá-lo! Caso não encontre, ele retorna um None.

## Custo Computacional

Como ele já tenta localizar o número dividindo a lista no meio e assim por diante, seu custo computacional é bem baixo, de complexidade Big O sendo log 2 (n). 

Sabe o que isso significa? Não? Então vamos lá:

Imagina uma lista de 1000000 elementos (bastante elemento), caso você vá fazer utilizando uma busca comum, no pior caso você terá que percorrer todos os 1000000 de elementos para encontrar esse número (isso se ele estiver na lista). 

Já com a busca binária a quantidade de iterações será no log de 1000000, e esse resultado é 20 no pior dos casos! Entendeu a difernça entre um algoritmo convencional e a busca binária?

## Mão na Massa

Vamos ver como funciona cada parte do algoritmo? 

Primeiro definimos uma lista de números (sendo ela ordenada) e um número alvo para a busca poder encontrá-lo:

```
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero_alvo = 6
```

Agora vamos criar uma função onde passamos por parâmetro essa lista e esse número alvo. Dentro dela podemos criar duas variáveis representando o intervalo em que o elemento possa estar!
Criamos também uma variável de tentativa, que contém a quantidade de iterações que a busca irá fazer:

```
def busca_binaria(lista_numeros, numero_alvo):
      
    inicio_lista = 0
    fim_lista = len(lista_numeros)
    tentativa = 1
```

Em seguida detectamos o elemento central da lista através da soma das variáveis de intervalo e a divisão da mesma. Com isso conseguimos acessar o meio e ver se o elemento que precisamos encontrar está para a direita ou para a esquerda da lista (ou até mesmo se já o encontramos). 

```
while fim_lista > inicio_lista:
    aux = (inicio_lista + fim_lista) // 2
    valor_atual = lista_numeros[aux]
```

Com isso definimos também algumas condições caso o elemento seja encontrado ou não. Caso ele seja, o algoritmo irá retornar a posição em que ele estava da lista. Caso o elemento tenha um valor menor que o valor central, a variável de intervalo final é atualizada com o valor central menos uma unidade. E caso o elemento tenha um valor maior, será atualizado o intervalo inicial com o valor central mais uma unidade.

```
if valor_atual == numero_alvo:
    print(f"Numero do indice: {aux}\nTentativas: {tentativa}")
    return aux
            
elif valor_atual > numero_alvo:
    fim_lista = aux - 1

elif valor_atual < numero_alvo:
    inicio_lista = aux + 1
```

O código completo pode ser encontrado aqui! 
