"""
A regra LEGB é como o python a usa para resolver nomes
Modificar o comportamento do python com 'global' e 'nonlocal'
vanames, freevars e cellvars

nota: quando eu usar a palavra "nome" sempre estarei me referindo
indentificadores de algo como: variável, função, classe, imports, etc...

Conhecimento python requerido: variáveis, função e estruturas de dados

LEGB = local/enclosing/global/built-in

O python segue uma ordem especifica e unidirecional para busca por nomes
a ordem sempre vai do escopo mais interno para o mais externo

Certo: local -> enclosing -> global -> built-in -> Xnameerror
Errado: built-in -> global -> enclosing -> Xlocal

De nenhum escopo externo é possivel usar algo de escopo interno

FREEVARS são as variaves da função externa que estão sendo usadas dentro
da função interna. A gente detecta isso pela função interna, porque ela é quem
depende desses nomes. Eles entram em co_freevars

CELLVARS são as variáveis declaradas na função atual (externa) que
precisam ser capturados porque são usados por funções internas. A gente detecta isso pela
função externam, porque ela é quem fornece essas variáveis pro closure. Eles aparecem em co_cellvars

VARNAMES são as variáveis locais de verdade, exclusivas da função. Elas estão em co_varnames e não 
fazem parte de nenhum closure, só exitem ali dentro mesmo
"""