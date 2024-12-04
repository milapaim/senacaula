def calcular_juro_composto(principal, taxa, tempo):
    """
    Calcula o montante final com juros compostos.

    Args:
        principal (float): Valor inicial investido.
        taxa (float): Taxa de juros (em decimal, ex: 0.05 para 5%).
        tempo (int): Tempo em períodos (meses, anos, etc.).

    Returns:
        float: Montante final.
    """
    montante = principal * (1 + taxa) ** tempo
    return montante

# Exemplo de uso:
valor_inicial = 1000  # Valor inicial investido
taxa_juros = 0.05     # Taxa de 5% ao ano
tempo_anos = 5        # Período de 5 anos

montante_final = calcular_juro_composto(valor_inicial, taxa_juros, tempo_anos)
print(f"O montante final é: R${montante_final:.2f}")
