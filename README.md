# Root-finding algorithm - Bisection method

ENGLISH

A root-finding algorithm is an algorithm for finding zeroes, also called "roots", of continuous functions.

The simplest root-finding algorithm is the bisection method.
The bisection method uses the intermediate value theorem, which says that if a function is continuous between two points, and those points evaluated in the function return values of opposite signs, then there is at least one point such that the function is zero when evaluated in him.
The iterative process uses an algorithm that divides the range into two equal-sized pieces by defining a midpoint,

𝑝𝑛 = 𝑎𝑛 − 𝑏𝑛

and evaluates which of the two halves contains the root by doing a multiplication operation between the midpoint and the points a and b,

𝑓(𝑎𝑛) ∗ 𝑓(𝑝𝑛) < 0 𝑜𝑢 𝑓(𝑏𝑛) ∗ 𝑓(𝑝𝑛) < 0

one of the results will result in a negative number showing that there is a root in that smaller interval, and then from this new interval the process is repeated until the stopping criterion is reached, in this case it was used:

|𝑏𝑛 − 𝑎𝑛| < max error

In the code presented in the annex, it is possible to interpret the following algorithm:
• Import math library
• Start counter globally
• Bisection function definition that receives a function f, points a and b and a maximum tolerated error value
- Verification if the points a and b evaluated in the function are of opposite signs, if not, the function returns null.
- Points a and b are passed to variables a_n and b_n so that the initial points of the iteration points are not mixed.
- The iterative process starts by assigning the midpoint to the variable p_n and evaluating the stopping criterion. If this is the case a global f_x variable is created to store the value of the root found evaluated in the function, then the loop is broken and the midpoint value of that interval is returned.
- If the stopping criterion is not satisfied, the next step is to update the counter reflecting that one more iteration has been performed, and then check if the root is halfway between b_n and p_n or between a_n and p_n.
- After the iterative process, there is a function (print_resultados) that simplifies the print process, receiving the values: example number n, value of the root found, value of the root evaluated in the function f_x and the counter, and printing each information clearly.
- Below you can see the definitions of the functions of each example and the call to the bisection function of each one of them, followed by the call to the print_resultados function.

PORTUGUESE

O método da bissecção utiliza o teorema do valor intermediário, que diz que se uma função é contínua entre dois pontos, e esses pontos avaliados na função retornam valores de sinais opostos, então, existe ao menos um ponto tal que a função é zero quando avaliada nele.
O processo interativo usa um algoritmo que divide o intervalo em duas partes de mesmo tamanho definindo um ponto médio,

𝑝𝑛 = 𝑎𝑛 − 𝑏𝑛

e avalia qual das duas metades contém a raiz fazendo uma operação de multiplicação entre o ponto médio e os pontos a e b,

𝑓(𝑎𝑛) ∗ 𝑓(𝑝𝑛) < 0 𝑜𝑢 𝑓(𝑏𝑛) ∗ 𝑓(𝑝𝑛) < 0

um dos resultados resultará em um número negativo evidenciando que há uma raiznaquele intervalo menor, e então a partir desse novo intervalo o processo é repetidoaté que o critério de parada seja atingido, nesse caso foi utilizado:

|𝑏𝑛 − 𝑎𝑛| < 𝑒𝑟𝑟𝑜 𝑡𝑜𝑙𝑒𝑟𝑎𝑑𝑜

No código apresentado no anexo é possível se interpretar o seguinte algoritmo:
- Import biblioteca math
- Iniciar contador a nível global
- Definição função bissecção que recebe uma função f, pontos a e b e um valor de erro máximo tolerado
- Verificação se os pontos a e b avaliados na função são de sinais opostos, se não, a função retorna nulo.
- Os pontos a e b são passados para variáveis a_n e b_n para que não se misturem os pontos iniciais dos pontos da iteração.
- O processo iterativo começa atribuindo o ponto médio a variável p_n e avaliando o critério de parada. Caso esse seja o caso uma variável f_x global é criada para armazenar o valor da raiz encontrada avaliada na função, então o loop é quebrado e é retornado o valor do ponto médio desse intervalo.
- Caso o critério de parada não seja satisfeito, o próximo passo é atualizar o contador refletindo que mais uma iteração foi realizada, e então verificar se a raiz está na metade entre b_n e p_n ou entre a_n e p_n.
- Após o processo iterativo tem-se uma função (print_resultados) que simplifica o processo de prints, recebendo os valores: número do exemplo n, valor da raiz encontrada, valor da raiz avaliada na função f_x e o contador, e fazendo o print de cada informação de forma clara.
- A seguir é possível ver as definições das funções de cada exemplo e a chamada a função bissecção de cada uma delas, seguido da chamada a função print_resultados.
