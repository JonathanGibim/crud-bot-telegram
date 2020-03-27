from models import Comando
from database import querys


def listar():
    comandos = []
    comandos_bd = querys.listar()
    for comando_bd in comandos_bd:
        comandos.append(Comando(comando_bd['comando'], comando_bd['descricao'], comando_bd['saida'], comando_bd['ativo'],
                                comando_bd['script'], comando_bd['id_comando']))
    return comandos


def localizar(id_comando):
    comando_bd = querys.localizar(id_comando)
    return Comando(comando_bd['comando'], comando_bd['descricao'], comando_bd['saida'], comando_bd['ativo'],
                   comando_bd['script'], comando_bd['id_comando'])


def criar(comando, descricao, saida, ativo, script):
    novo_comando = Comando(comando, descricao, saida, ativo, script)
    novo_comando.id_comando = querys.criar(novo_comando)
    return novo_comando


def atualizar(id_comando, comando, descricao, saida, ativo, script):
    comando_atualizado = Comando(comando, descricao, saida, ativo, script, id_comando)
    querys.atualizar(comando_atualizado)
    return comando_atualizado


def deletar(id_comando):
    comando = localizar(id_comando)
    querys.deletar(id_comando)
    return comando
