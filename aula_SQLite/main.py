import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()


# Criando tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
sql = (f'INSERT INTO {TABLE_NAME}'
        '(name, weight)'
        'VALUES '
        '(:name, :weight)')

# cursor.execute(sql, ['Guilherme', 4])
# cursor.executemany(
#     sql, [['Guilherme', 4], ['Sabrina', 8]]
#     )
cursor.execute(sql, {'name': 'Jão', 'weight': 3})
cursor.executemany(sql, (
    {'name': 'cachorra', 'weight': 8},
    {'name': 'irineu', 'weight': 7},
    {'name': 'cirineu', 'weight': 5},
    {'name': 'amadeu', 'weight': 1},
))

connection.commit()

cursor.close()
connection.close()
 