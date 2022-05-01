# Array!

## O que é?

Array é basicamente uma estrutura limitada pelo tamanho onde cada valor ocupa um espaço determinado nesse array.

Pode ser comparado há um conjunto de blocos onde nenhum valor é mutável e dinâmico, e para fazer uma alteração, remoção ou inserção é necessário adaptar toda essa estrutura para caber o novo valor!

## Prós

Há alguns motivos para se utilizar o array ao invés da lista, entre eles estão:

-O array é bom para quando você já tem um tamanho fixo de um conjunto de dados, assim como você irá especificar qual elemento você gostaria de acessar já que ele tem peso O(1) para acessar o valor conhecido;
-Ao saber o tamanho especifico você poderá utilizar apenas aquela parte da memória alocada, fazendo com que não aja gasto extra de memória no computador;

## Contras

Porém há algumas partes que é melhor utilizar uma lista e não um array, como nos seguintes exemplos:

-Ao não saber exatamente o tamanho do array, é necessário estar alocando mais espaços, e assim aumentando o uso da memória;
-Não é recomendada na hora de adicionar e remover elementos, por não excluir o espaço que havia daquele elemento, apenas o inutilizando.
