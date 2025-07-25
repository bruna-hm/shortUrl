from flask import Flask, render_template, request, redirect, abort
import os
import sqlite3
from shortPolis.dao import create_tab, cad_url
from shortPolis.views.utils import encurtar_url

app = Flask(__name__)
create_tab()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/encurtar', methods=['POST'])
def encurtar():
    url_longa = request.form.get('url_longa')
    if not url_longa:
        return "URL longa não fornecida", 400
    
    codigo = encurtar_url()
    cad_url(url_longa, codigo)
    
    url_curta = request.host_url + codigo
    return render_template('result.html', url_curta=url_curta)

@app.route('/<codigo>')
def redirecionar(codigo):
    with sqlite3.connect("urls.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT longa FROM urls WHERE curta = ?", (codigo,))
        resultado = cur.fetchone()

    if resultado:
        url_longa = resultado[0]
        return redirect(url_longa)
    else:
        return abort(404, description="Link não encontrado ou expirado")