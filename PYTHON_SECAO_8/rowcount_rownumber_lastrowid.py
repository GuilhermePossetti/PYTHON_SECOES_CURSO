"""
# rowcount, rownumber e lastrowid

Esses atributos são usados com o `cursor` para obter informações sobre as operações realizadas no banco de dados.

## 1. rowcount

O `rowcount` mostra **quantas linhas foram afetadas** pela última operação.

### Exemplo:

```python
cursor.execute('DELETE FROM alunos WHERE id = 1')

print(cursor.rowcount)
```

Se o aluno com `id = 1` foi apagado, o resultado será:

```text
1
```

Isso significa que **1 linha foi afetada**.

Outro exemplo:

```python
cursor.execute('UPDATE alunos SET nome = "João" WHERE id = 2')

print(cursor.rowcount)
```

Resultado:

```text
1
```

Significa que **1 registro foi alterado**.

### Resumindo:

`rowcount` = **quantidade de linhas afetadas pela operação.**

---

## 2. rownumber

O `rownumber` indica **a posição atual da linha no resultado da consulta**.

Por exemplo, quando fazemos uma consulta:

```python
cursor.execute('SELECT * FROM alunos')
```

O cursor vai percorrer os resultados.

Podemos usar métodos como:

```python
cursor.fetchone()
```

para pegar uma linha por vez.

O `rownumber` pode indicar em qual posição do resultado o cursor está.

### Resumindo:

`rownumber` = **posição atual da linha no resultado.**

⚠️ Observação: o `rownumber` não está disponível em todos os bancos ou drivers. Por exemplo, o cursor padrão do SQLite não possui esse atributo.

---

## 3. lastrowid

O `lastrowid` mostra o **ID da última linha que foi inserida**.

Isso é muito útil quando a tabela possui um ID que é gerado automaticamente.

### Exemplo:

```python
cursor.execute(
    'INSERT INTO alunos (nome) VALUES ("Guilherme")'
)

print(cursor.lastrowid)
```

Imagine que antes o último aluno tinha o ID `4`.

Ao inserir Guilherme, o banco gera automaticamente:

```text
id = 5
```

Então:

```python
print(cursor.lastrowid)
```

vai mostrar:

```text
5
```

Ou seja, o `lastrowid` informa qual foi o **ID gerado para o último registro inserido**.

---

# Resumo

```text
rowcount  → quantidade de linhas afetadas
rownumber → posição atual da linha no resultado
lastrowid → ID da última linha inserida
```

### Uma forma fácil de lembrar:

* `rowcount` → **quantas?**
* `rownumber` → **qual posição?**
* `lastrowid` → **qual foi o último ID?**

"""