"""
############Consulta e verificação######################

str.capitalize() → Retorna a string com a primeira letra maiúscula e o resto minúsculo.

str.casefold() → Igual ao lower(), mas mais agressivo (útil em comparações).

str.lower() → Converte toda a string para minúsculas.

str.upper() → Converte toda a string para maiúsculas.

str.title() → Retorna a string com cada palavra começando em maiúscula.

str.swapcase() → Inverte maiúsculas e minúsculas.

str.islower() → Retorna True se todos os caracteres forem minúsculos.

str.isupper() → Retorna True se todos os caracteres forem maiúsculos.

str.istitle() → Retorna True se estiver no formato de título.

str.isalpha() → Retorna True se só tiver letras.

str.isalnum() → Retorna True se só tiver letras e números.

str.isdigit() → Retorna True se só tiver dígitos (0-9).

str.isnumeric() → Retorna True se for numérico (inclui outros números, como romanos).

str.isdecimal() → Retorna True se for apenas decimal.

str.isascii() → Retorna True se todos os caracteres forem ASCII.

str.isidentifier() → Verifica se a string pode ser usada como
identificador de variável em Python.

str.isprintable() → Retorna True se todos os caracteres forem imprimíveis.

str.isspace() → Retorna True se só tiver espaços em branco.
"""

"""
#################Busca e localização#######################

str.find(sub) → Retorna o índice da primeira ocorrência de sub (ou -1 se não achar).

str.rfind(sub) → Retorna o índice da última ocorrência de sub.

str.index(sub) → Igual ao find(), mas dá erro se não achar.

str.rindex(sub) → Igual ao rfind(), mas dá erro se não achar.

str.startswith(prefix) → Verifica se começa com prefix.

str.endswith(suffix) → Verifica se termina com suffix.
"""

"""
###############Substituição e modificação################

str.replace(velho, novo) → Substitui ocorrências de velho por novo.

str.strip() → Remove espaços (ou caracteres específicos) do início e do fim.

str.lstrip() → Remove do início.

str.rstrip() → Remove do fim.

str.expandtabs(n) → Substitui \t por espaços (por padrão 8).

str.removeprefix(prefix) → Remove um prefixo, se existir (Python 3.9+).

str.removesuffix(suffix) → Remove um sufixo, se existir (Python 3.9+).
"""

"""
##################Quebra e junção############################

str.split(sep) → Divide a string em lista, pelo separador.

str.rsplit(sep) → Divide a partir da direita.

str.splitlines() → Divide a string em lista, quebrando por linhas.

str.join(iterável) → Junta elementos de um iterável em uma string.

str.partition(sep) → Divide em 3 partes: antes, separador, depois (primeira ocorrência).

str.rpartition(sep) → Igual, mas a partir da última ocorrência.
"""

"""
##################Alinhamento e formatação######################

str.center(largura, fillchar) → Centraliza dentro de um tamanho.

str.ljust(largura, fillchar) → Alinha à esquerda.

str.rjust(largura, fillchar) → Alinha à direita.

str.zfill(largura) → Preenche com zeros à esquerda.

str.format() → Formata a string com placeholders {}.

str.format_map(dict) → Igual ao format, mas usa um dicionário direto.
"""

"""
################Codificação e tradução####################

str.encode(codificação) → Converte para bytes.

str.translate(tabela) → Traduz caracteres conforme uma tabela (str.maketrans).

str.maketrans(x, y, z) → Cria a tabela de tradução para translate().
"""