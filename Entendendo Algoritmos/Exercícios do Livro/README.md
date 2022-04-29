# Exercícios do Livro!
## Capítulo 01
### Busca Binária

#### 1.1 Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?

R: Como a busca binária tem o custo de O(log 2 (n)), então ao calcularmos, conseguimos o resultado do log de 128 na base 2 sendo 7!

Portanto temos no máximo 7 etapas para realizar todo o processo de busca.

#### 1.2 Suponha que você duplique o tamanho da lista. Qual seria o número máximo de etapas agora?

R: Como o valor apenas duplicou e a base do log é 2, a quantidade de tentativas aumentará em apenas 1!

### Notação Big O

#### 1.3 Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica.

R: O(n)

#### 1.4 Você tem um número de telefone e deseja encontrar o dono dele em uma agenda telefônica. (Dica: Deve procurar pela agenda inteira!)

R: O(n)

#### 1.5 Você quer ler o número de cada pessoa da agenda telefônica.
 
R: O(n)

#### 1.6 Você quer ler os números apenas dos nomes que começam com A.

R: O(n)

## Capítulo 02
### Array e Lista

#### 2.1 Suponha que você esteja criando um aplicativo para acompanhar as suas finanças. Todos os dias você anotará tudo o que gastou e onde gastou. No final do mês, você deverá revisar os seus gastos e resumir o quanto gastou. Logo, você terá um monte de inserções e poucas leituras. Você deverá usar um array ou uma lista para implementar este aplicativo?

R: Uma lista, como terá mais inserções do que leituras em si, o ideal é utilizar uma lista do que um array.

#### 2.2 Suponha que você esteja criando um aplicativo para anotar os pedidos dos clientes em um restaurante. Seu aplicativo precisa de uma lista de pedidos. Os garçons adicionam os pedidos a essa lista e os chefes retiram os pedidos da lista. Funciona como uma fila. Os garçons colocam os pedidos no nal da fila e os chefes retiram os pedidos do começo dela para cozinhá-los. Você usaria um array ou uma lista encadeada para implementar essa lista?

R: Lista encadeada! Como cada pedido será inserido no final e então pego no começo, ele precisará passar por cada elemento da fila para poder realizar essa inserção e remoção.

#### 2.3 Vamos analisar um experimento. Imagine que o Facebook guarda uma lista de usuários. Quando alguém tenta acessar o Facebook, uma busca é feita pelo nome de usuário. Se o nome da pessoa está na lista, ela pode continuar o acesso. As pessoas acessam o Facebook com muita frequência, então existem muitas buscas nessa lista. Presuma que o Facebook usa a pesquisa binária para procurar um nome na lista. A pesquisa binária requer acesso aleatório – você precisa ser capaz de acessar o meio da lista de nomes instantaneamente. Sabendo disso, você implementaria essa lista como um array ou uma lista encadeada?

R: Com um array, como ela é feita através da busca binária, então não precisamos percorrer cada elemento da lista.

#### As pessoas se inscrevem no Facebook com muita frequência também. Suponha que você decida usar um array para armazenar a lista de usuários. Quais as desvantagens de um array em relação às inserções? Em particular, imagine que você está usando a pesquisa binária para buscar os logins. O que acontece quando você adiciona novos usuários em um array?

R: Com um array é necessário estar sempre aumentando o tamanho da lista para as inserções, haveria a necessidade de criar um array dinâmico ou renovando o tamanho dele. Ao adicionar novos usuários o array não irá permitir, já utilizando a lista ele apenas aumentará seu tamanho.

#### Na verdade, o Facebook não usa nem arrays nem listas encadeadas para armazenar informações. Vamos considerar uma estrutura de dados híbrida: um array de listas encadeadas. Você tem um array com 26 slots. Cada slot aponta para uma lista encadeada. Por exemplo, o primeiro slot do array aponta para uma lista encadeada que contém os usuários que começam com a letra A. O segundo slot aponta para a lista encadeada que contém os usuários que começam com a letra B, e assim por diante.

R: É mais lento que um array por ter que acessar os elementos da lista após encontrar a letra que queremos, porém é mais rápido que uma lista, já que já teremos a letra pela qual queremos buscar inicialmente.
