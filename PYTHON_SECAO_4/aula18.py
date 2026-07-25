
"""
Dictionary Comprehension e Set Comprehension
"""

produto = {
    'Nome': 'CANETA AZUL',
    'Preço': 2.5,
    'Categoria': 'ESCRITÓRIO',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str)
    else valor
    for chave, valor in produto.items()
}
print(dc)