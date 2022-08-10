# Portas Lógicas
(Operações bit a bit)

____________________________________________________________________________________________________________________


Trabalho prático da disciplina "Matemática Discreta" do curso de Ciência da Computação da UFV - Universidade Federal de Minas Gerais - Campus Florestal.

Informações são armazenadas nos computadores por meio de bits, 
símbolos com dois valores possíveis, 0 (zero) ou 1 (um). Um bit pode ser usado para
representar um valor-verdade, sendo o 1 usado como verdadeiro (V) e o 0 como falso (F).


Uma sequência de bits de tamanho N possui N símbolos 0 ou 1 em sequência. Uma
operação binária entre duas sequências de bits de mesmo tamanho N aplica um operador
lógico (AND, OR, XOR, NAND ou NOR, por exemplo) a cada bit na mesma posição.

____________________________________________________________________________________________________________________


**Portas Lógicas usadas**

* OR - (OU)
* AND - (E)
* XOR - (OU Exclusivo)
* NAND - (Negação do E)
* NOR - (Negação do OU)
* MOR - (Se, então)

____________________________________________________________________________________________________________________


O programa desenvolvido neste trabalho lê, como entrada, duas
sequências de bits, S1 e S2, de tamanho N, lê uma expressão lógica contendo os
operadores (AND, OR, XOR, NAND, NOR ou MOR) e gera, como saída, o
resultado da aplicação da operação lógica nas sequências S1 e S2.

**Entrada:**
O problema possui quatro linhas de entrada, sendo:
Linha 1: o tamanho N da sequência (máximo de 1000)
Linha 2: a sequência de bits S1
Linha 3: a sequência de bits S2
Linha 4: uma expressão lógica que envolva as sequências S1 e S2 e até duas operações
da lista (AND, OR, XOR, NAND, NOR ou MOR). A prioridade dos operadores deve ser
pela ordem na expressão. Não será utilizado parênteses para mudar a ordem.


**Saída:**
Uma linha com uma sequência de N bits como resultado da expressão lógica. Caso o
tamanho de alguma das sequências S1 e S2 seja diferente de N, deve ser gerado ERRO
como saída. Caso a operação da entrada seja diferente das permitidas, deve ser gerado
ERRO como saída. Caso algum símbolo das sequências S1 ou S2 seja diferente de 0 ou
1, deve ser gerado ERRO como saída.

____________________________________________________________________________________________________________________