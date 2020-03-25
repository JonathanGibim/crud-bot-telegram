import services
from sqlite3 import IntegrityError
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '748b2c88db1eead6f189b8c5ab7bf050cc05'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/comandos/', methods=['GET'])
def listar_comandos():
    comandos = services.listar()
    return render_template('listar.html', comandos=comandos)


@app.route('/cadastrar/', methods=['GET', 'POST'])
def cadastrar_comando():
    if request.method == 'GET':
        return render_template('formulario.html', titulo='Cadastro', botao='Cadastrar')

    if request.method == 'POST':
        try:
            dados_form = request.form.to_dict()
            if dados_form['script'] == '':
                dados_form['script'] = None
            criado = services.criar(**dados_form)
            flash(f'Comando {criado.id_comando} cadastrado com sucesso!', 'success')
            return redirect('/comandos/')
        except IntegrityError:
            flash(f'Oops! Já existe um comando com o nome {dados_form["comando"]}.', 'danger')
            return render_template('formulario.html', comando=dados_form['comando'], saida=dados_form['saida'],
                                   ativo=dados_form['ativo'], script=dados_form['script'],
                                   titulo='Cadastro', botao='Cadastrar')


@app.route('/comandos/<int:id_comando>/', methods=['GET', 'POST'])
def editar_comando(id_comando):
    if request.method == 'GET':
        comando = services.localizar(id_comando)
        return render_template('formulario.html', comando=comando.comando,
                               saida=comando.saida, ativo=comando.ativo, script=comando.script, titulo='Edição',
                               botao='Alterar')

    if request.method == 'POST':
        try:
            dados_form = request.form.to_dict()
            if dados_form['script'] == '':
                dados_form['script'] = None
            atualizado = services.atualizar(id_comando, **dados_form)
            flash(f'Comando {atualizado.id_comando} alterado com sucesso!', 'success')
            return redirect('/comandos/')
        except IntegrityError:
            flash(f'Oops! Já existe um comando com o nome {dados_form["comando"]}.', 'danger')
            return render_template('formulario.html', comando=dados_form['comando'], saida=dados_form['saida'],
                                   ativo=dados_form['ativo'], script=dados_form['script'],
                                   titulo='Edição', botao='Alterar')


@app.route('/comandos/<int:id_comando>/', methods=['DELETE'])
def deletar_comando(id_comando):
    deletado = services.deletar(id_comando)
    flash(f'Comando {deletado.id_comando} excluido com sucesso!', 'success')
    return redirect('/comandos/', 200)


if __name__ == '__main__':
    app.run(debug=True)
