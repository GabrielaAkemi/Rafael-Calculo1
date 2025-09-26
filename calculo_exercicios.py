import sympy as sp
from sympy.abc import x, h
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

def resolver_inequacao(expr, rel):
    """
    Resolve uma inequação e retorna o conjunto solução.
    
    Args:
        expr (sympy.Expr): A expressão da inequação (e.g., (2-x)/(3-x)).
        rel (str): O sinal da relação ('<', '>', '<=', '>=').

    Returns:
        Um conjunto de solução.
    """
    try:
        if rel == '<':
            sol = sp.solveset(expr < 0, x, domain=sp.Reals)
        elif rel == '>':
            sol = sp.solveset(expr > 0, x, domain=sp.Reals)
        elif rel == '<=':
            sol = sp.solveset(expr <= 0, x, domain=sp.Reals)
        elif rel == '>=':
            sol = sp.solveset(expr >= 0, x, domain=sp.Reals)
        else:
            return "Sinal de inequação não reconhecido."
        return sol
    except Exception as e:
        return f"Erro ao resolver a inequação: {e}"

def estudar_sinal(expr):
    """
    Realiza o estudo do sinal de uma expressão.
    
    Args:
        expr (sympy.Expr): A expressão para estudar o sinal.
        
    Returns:
        Uma string com a análise detalhada do estudo de sinal.
    """
    try:
        sol_pos = sp.solveset(expr > 0, x, domain=sp.Reals)
        sol_neg = sp.solveset(expr < 0, x, domain=sp.Reals)
        sol_zero = sp.solveset(sp.Eq(expr, 0), x, domain=sp.Reals)
        
        pontos_indef = sp.singularities(expr, x)
        
        resultado = f"Estudo do sinal da expressão: {sp.sstr(expr)}\n"
        resultado += f"A expressão é POSITIVA para x ∈ {sol_pos}\n"
        resultado += f"A expressão é NEGATIVA para x ∈ {sol_neg}\n"
        resultado += f"A expressão é ZERO para x = {sol_zero}\n"
        if pontos_indef:
            resultado += f"A expressão é INDEFINIDA para x = {pontos_indef}\n"
        
        return resultado
    except Exception as e:
        return f"Erro ao realizar o estudo de sinal: {e}"

def calcular_limite(expr, ponto):
    """
    Calcula o limite de uma expressão quando x se aproxima de um ponto.
    
    Args:
        expr (sympy.Expr): A expressão do limite.
        ponto (float or int): O ponto para o qual x se aproxima.
    
    Returns:
        O valor do limite.
    """
    try:
        limite = sp.limit(expr, x, ponto)
        return limite
    except Exception as e:
        return f"Erro ao calcular o limite: {e}"

def calcular_limite_com_h(funcao):
    """
    Calcula o limite da definição da derivada: lim(h->0) (f(x+h)-f(x))/h
    
    Args:
        funcao (sympy.Expr): A função f(x) para a qual a derivada é calculada.
    
    Returns:
        A derivada da função.
    """
    try:
        expr_limite = (funcao.subs(x, x+h) - funcao) / h
        limite = sp.limit(expr_limite, h, 0)
        return limite
    except Exception as e:
        return f"Erro ao calcular a derivada: {e}"

def verificar_continuidade(funcao, ponto):
    """
    Verifica a continuidade de uma função em um ponto.
    
    Args:
        funcao (sympy.Expr): A expressão da função.
        ponto (float or int): O ponto a ser verificado.
    
    Returns:
        Uma string com a análise da continuidade.
    """
    try:
        lim_direita = sp.limit(funcao, x, ponto, dir='+')
        lim_esquerda = sp.limit(funcao, x, ponto, dir='-')
        valor_funcao = funcao.subs(x, ponto)
        
        resultado = (f"Análise de Continuidade em x = {ponto}:\n"
                     f"Limite pela direita (x -> {ponto}+): {lim_direita}\n"
                     f"Limite pela esquerda (x -> {ponto}-): {lim_esquerda}\n"
                     f"Valor da função no ponto: {valor_funcao}\n")
        
        if lim_direita == lim_esquerda and lim_direita == valor_funcao:
            resultado += "A função é contínua no ponto."
        else:
            resultado += "A função NÃO é contínua no ponto."
        
        return resultado
    except Exception as e:
        return f"Erro ao verificar a continuidade: {e}"

def main():
    """
    Função principal que interage com o usuário via terminal.
    """
    transformations = standard_transformations + (implicit_multiplication_application,)
    
    while True:
        print("\n--- Menu de Cálculos ---")
        print("1. Estudar Sinal de Expressão")
        print("2. Calcular Limite")
        print("3. Calcular Derivada pela Definição")
        print("4. Verificar Continuidade")
        print("5. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            try:
                expr_str = input("Digite a expressão (ex: (x-1)/(x-2)): ")
                expr = parse_expr(expr_str, transformations=transformations)
                solucao = estudar_sinal(expr)
                print(f"Resultado:\n{solucao}")
            except Exception as e:
                print(f"Entrada inválida. Tente novamente. Erro: {e}")
        
        elif escolha == '2':
            try:
                expr_str = input("Digite a expressão do limite (ex: (x**2 - 4) / (x - 2)): ")
                ponto_str = input("Digite o ponto para o qual o limite tende: ")
                expr = parse_expr(expr_str, transformations=transformations)
                ponto = float(ponto_str)
                limite = calcular_limite(expr, ponto)
                print(f"O valor do limite é: {limite}")
            except Exception as e:
                print(f"Entrada inválida. Tente novamente. Erro: {e}")

        elif escolha == '3':
            try:
                funcao_str = input("Digite a função f(x) (ex: x**2): ")
                funcao = parse_expr(funcao_str, transformations=transformations)
                derivada = calcular_limite_com_h(funcao)
                print(f"A derivada de f(x) pela definição é: {derivada}")
            except Exception as e:
                print(f"Entrada inválida. Tente novamente. Erro: {e}")
                
        elif escolha == '4':
            try:
                funcao_str = input("Digite a função (use 'sp.Piecewise' para funções de pedaços, ex: 'sp.Piecewise((2*x, x <= 1), (1, True))'): ")
                ponto_str = input("Digite o ponto para verificar a continuidade: ")
                
                print("Para funções de pedaços, digite a expressão como 'sp.Piecewise((expr1, cond1), (expr2, cond2))'.")
                
                funcao = eval(funcao_str)
                ponto = float(ponto_str)
                
                resultado_cont = verificar_continuidade(funcao, ponto)
                print(resultado_cont)

            except Exception as e:
                print(f"Entrada inválida ou função não suportada. Tente novamente. Erro: {e}")

        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        
        else:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")

if __name__ == '__main__':
    main()
