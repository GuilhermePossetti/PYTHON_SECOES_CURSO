"""
JSON - JavaScript Object Notation (extensão .json)
É uma estrutura de dados que permite a serialização de objetos em texto simples
para facilitar a trasmissão de dados através da rede, APIs web ou outros meios
de comunicação O JSON suporta os seguintes tipos de dados:
Números: podem ser inteiros ou com ponto flutuante, com 42 ou 3.14
Strings: são cadeias de caracteres, como "Olé, mundo!" ou "123456"

As str devem ser envolvidad por aspas duplas

Booleanos: são os valores verdadeiros (true) ou falso (false)
Arrays: são listas ordenadas de valores, como [1, 2, 3] ou ["Oi", "Bom dia"]
Objetos: são conjuntos de pares nome/valor -> {"nome": "João", "idade": 30}
null: é um valor especial que representa ausência de valor

Ao converter de Python para JSON:

# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null
"""