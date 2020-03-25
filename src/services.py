from models import Comando
from database import dao


def listar():
    comandos = []
    comandos_bd = dao.listar()
    for comando_bd in comandos_bd:
        comandos.append(Comando(comando_bd['comando'], comando_bd['saida'], comando_bd['ativo'],
                                comando_bd['script'], comando_bd['id_comando']))
    return comandos


def localizar(id_comando):
    comando_bd = dao.localizar(id_comando)
    return Comando(comando_bd['comando'], comando_bd['saida'], comando_bd['ativo'],
                   comando_bd['script'], comando_bd['id_comando'])


def criar(comando, saida, ativo, script):
    novo_comando = Comando(comando, saida, ativo, script)
    novo_comando.id_comando = dao.criar(novo_comando)
    return novo_comando


def atualizar(id_comando, comando, saida, ativo, script):
    comando_atualizado = Comando(comando, saida, ativo, script, id_comando)
    dao.atualizar(comando_atualizado)
    return comando_atualizado


def deletar(id_comando):
    comando = localizar(id_comando)
    dao.deletar(id_comando)
    return comando
