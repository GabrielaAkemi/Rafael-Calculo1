
# 🧮 Calculadora Simbólica com Python (SymPy)

Este projeto é uma **ferramenta interativa em Python** para realizar cálculos simbólicos, estudo de sinais, limites, derivadas pela definição e análise de continuidade de funções.  
Foi desenvolvido utilizando a biblioteca [SymPy](https://www.sympy.org/), permitindo que usuários resolvam inequações e analisem funções de forma **simples e automatizada**.  

---

## 💡 Objetivo do Projeto

O objetivo principal é fornecer uma **ferramenta educativa e prática** para estudantes e profissionais de matemática, engenharia e áreas afins, oferecendo funcionalidades como:

- 🔹 **Estudo de sinal de expressões**
- 🔹 **Cálculo de limites**
- 🔹 **Derivadas pela definição**
- 🔹 **Verificação de continuidade de funções**
- 🔹 **Resolução de inequações**

O projeto funciona via **terminal interativo**, permitindo que o usuário digite expressões matemáticas e obtenha resultados simbólicos imediatos.

---

## 🧩 Tecnologias Utilizadas

| Categoria | Tecnologias |
|-----------|-------------|
| **Linguagem** | Python 3.x |
| **Bibliotecas** | SymPy |
| **Parser de Expressões** | `sympy.parsing.sympy_parser` |
| **Ambiente de Execução** | Terminal / Prompt de Comando |
| **Plataforma** | Multiplataforma (Windows, macOS, Linux) |

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. **Entre na pasta do projeto:**

   ```bash
   cd calculadora-simbolica
   ```

3. **Instale a biblioteca SymPy (se ainda não tiver):**

   ```bash
   pip install sympy
   ```

4. **Execute o programa:**

   ```bash
   python main.py
   ```

5. **Siga o menu interativo** para escolher as opções de estudo de sinal, limite, derivada ou continuidade.

---

## 📋 Funcionalidades

1. **Estudo de Sinal**
   Analisa os intervalos em que uma expressão é positiva, negativa, zero ou indefinida.

2. **Cálculo de Limite**
   Calcula limites de expressões simbólicas em pontos específicos.

3. **Derivada pela Definição**
   Calcula a derivada usando o limite da definição:
   [
   f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}
   ]

4. **Verificação de Continuidade**
   Analisa se uma função é contínua em um ponto, comparando limites laterais e valor da função.

5. **Resolução de Inequações**
   Resolve inequações do tipo `<`, `>`, `<=`, `>=` e retorna o conjunto solução.

---

## 👩‍💻 Como Usar

Ao executar o programa, você verá o seguinte **menu interativo**:

```
--- Menu de Cálculos ---
1. Estudar Sinal de Expressão
2. Calcular Limite
3. Calcular Derivada pela Definição
4. Verificar Continuidade
5. Sair
```

O usuário deve digitar o número da opção desejada e, em seguida, inserir a expressão ou função conforme solicitado.
Para funções de pedaços, utilize `sp.Piecewise((expr1, cond1), (expr2, cond2))`.

---

##  Exemplos de Uso

```python
# Estudo de sinal
expr = (x-1)/(x-2)
estudar_sinal(expr)

# Cálculo de limite
expr = (x**2 - 4)/(x-2)
calcular_limite(expr, 2)

# Derivada pela definição
funcao = x**2
calcular_limite_com_h(funcao)

# Verificação de continuidade
funcao = sp.Piecewise((2*x, x <= 1), (1, True))
verificar_continuidade(funcao, 1)
```

---

> *“A matemática é a linguagem com a qual Deus escreveu o universo.”* 🌌
> — Galileo Galilei

Quer que eu faça essa versão visual?
```
