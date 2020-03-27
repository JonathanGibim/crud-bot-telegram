from contextlib import closing
from database.utils.rows import rows_to_dict, row_to_dict
from database.config import con

sql_listar = "SELECT id_comando, comando, descricao, saida, script, ativo FROM comandos"

sql_localizar = "SELECT id_comando, comando, descricao, saida, script, ativo FROM comandos WHERE id_comando = ?"

sql_criar = "INSERT INTO comandos(comando, descricao, saida, script, ativo) VALUES (?, ?, ?, ?, ?)"

sql_atualizar = "UPDATE comandos SET comando = ?, descricao = ?, saida = ?, script = ?, ativo = ? WHERE id_comando = ?"

sql_remover = "DELETE FROM comandos WHERE id_comando = ?"


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_listar)
        return rows_to_dict(cursor.description, cursor.fetchall())


def localizar(id_comando):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_localizar, (id_comando,))
        return row_to_dict(cursor.description, cursor.fetchone())


def criar(comando):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_criar, (comando.comando, comando.descricao, comando.saida, comando.script, comando.ativo))
        id_comando = cursor.lastrowid
        connection.commit()
        return id_comando


def atualizar(comando_atualizado):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_atualizar, (comando_atualizado.comando, comando_atualizado.descricao,
                                       comando_atualizado.saida, comando_atualizado.script, 
                                       comando_atualizado.ativo, comando_atualizado.id_comando))
        connection.commit()


def deletar(id_comando):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(sql_remover, (id_comando,))
        connection.commit()
