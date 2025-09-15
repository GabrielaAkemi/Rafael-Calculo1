Projeto de Resolução de Exercícios de Cálculo
Este projeto consiste em um script interativo em Python para auxiliar na resolução e estudo de exercícios de Cálculo Diferencial e Integral. O script foi desenvolvido para ajudar a praticar conceitos-chave como inequações, limites, derivadas e continuidade, com base nas listas de exercícios do livro "Um curso de cálculo – Volume 1" de Hamilton Luiz Guidorizi.

Funcionalidades
O script oferece um menu interativo com as seguintes opções de cálculo:

Estudar Sinal de Expressão: Analisa e descreve detalhadamente o estudo de sinal de uma expressão matemática, mostrando onde ela é positiva, negativa, zero ou indefinida.

Calcular Limite: Calcula o limite de uma função quando a variável se aproxima de um determinado ponto.

Calcular Derivada pela Definição: Utiliza a definição formal de derivada (lim_h→0 
h
f(x+h)−f(x)
​
 ) para encontrar a derivada de uma função.

Verificar Continuidade: Analisa a continuidade de uma função em um ponto específico, comparando os limites laterais e o valor da função no ponto.

Sair: Encerra o programa.

Como Usar
Requisitos
Para executar este script, você precisa ter o Python instalado e a biblioteca sympy. Se ainda não a tiver, instale-a via pip:

pip install sympy

Execução
Salve o código do script em um arquivo chamado calculo_exercicios.py.

Abra o terminal ou prompt de comando na mesma pasta onde o arquivo foi salvo.

Execute o script com o comando:

python calculo_exercicios.py

Siga as instruções do menu para escolher a operação desejada e inserir as expressões ou valores necessários.

Exemplos de Entrada
Expressão para Estudo de Sinal/Limite: Use a sintaxe padrão do Python para expressões matemáticas. Por exemplo, (x**2 - 4) / (x - 2). Use x**2 para x 
2
 .

Funções de pedaços (Continuidade): Use a sintaxe da biblioteca sympy. Exemplo: sp.Piecewise((2*x, x <= 1), (1, True)).

Contribuições
Este é um projeto simples para fins de estudo. Se você tiver sugestões para melhorias ou novas funcionalidades, sinta-se à vontade para adaptá-lo.
