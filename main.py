import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pdfkit
import sqlite3
import sys

notas = ["Conhecimento", "Fase21", "Fase22", "Redacao", "Final"]
categoriasDados = dict()

def criaChamadaGrafico (chamadakeys, chamadavalues):
    chamadaFigura = plt.figure()
    chamadaGrafico = chamadaFigura.add_subplot(111)
    chamadaGrafico.pie(chamadavalues, labels=chamadakeys, autopct="%1.2f%%")
    chamadaGrafico.set_title("Porcentagem de ingressos em cada chamada")
    plt.savefig("./{}/{}/{}/chamadas.jpg".format(unidade, curso, turma))
    plt.cla()

def comentarioHTML(comentarios):
    comentarioList = []
    comentarios = [comentario for comentario in comentarios if str(comentario) != 'nan']
    for comentario in comentarios:
        if comentario:
            comentarioList.append("<p>{}</p>".format(comentario))
    comentarioString = "\n".join(comentarioList)
    return comentarioString

def criaDados(categorias, notas):
    for categoria, dataframe in categorias.items():
        if not os.path.isdir("./{}/{}/{}/{}".format(unidade, curso, turma, categoria)):
            os.makedirs("./{}/{}/{}/{}".format(unidade, curso, turma, categoria))
        criarCategoria(categoria, dataframe, notas)

def criarCategoria(categoria, dataframe, notas):
    conhecimento = dataframe["Conhecimentos Gerais"].values.tolist()
    fase2_1 = dataframe["2ª fase - 1º dia"].values.tolist()
    fase2_2 =  dataframe["2ª fase - 2º dia"].values.tolist()
    redacao = dataframe["Redação"].values.tolist()
    final = dataframe["Nota Final"].values.tolist()
    datasets = [conhecimento, fase2_1, fase2_2, redacao, final]
    criaMedias(categoria, datasets)
    graficoCategoria (categoria, datasets, notas)

def criaMedias(categoria, datasets):
    conhecimentoString = "A média da categoria " + categoria + " em Conhecimentos Gerais foi {}".format(round(np.mean(datasets[0]), 2))
    fase21String = "A média da categoria " + categoria + " no 1º dia da 2ª fase foi {}".format(round(np.mean(datasets[1]), 2))
    fase22String = "A média da categoria " + categoria + " no 2º dia da 2ª fase foi {}".format(round(np.mean(datasets[2]), 2))
    redacaoString = "A média da categoria " + categoria + " em Redação foi {}".format(round(np.mean(datasets[3]), 2))
    finalString = "A média da categoria " + categoria + " na Nota Final foi {}".format(round(np.mean(datasets[4]),2))
    categoriasDados[categoria] = [conhecimentoString, fase21String, fase22String, redacaoString, finalString]

def graficoIndividual (categoria, dataset, string, nota):
    Figura = plt.figure()
    Grafico = Figura.add_subplot(111)
    Grafico.hist(dataset, bins=20)
    Grafico.set_xlabel("Notas")
    Grafico.set_ylabel("Quantidade")
    Grafico.set_title(string.format(categoria))
    plt.savefig("./{}/{}/{}/{}/{}{}.jpg".format(unidade, curso, turma, categoria, categoria.lower(), nota))
    plt.cla()
    plt.close()

def graficoCategoria (categoria, datasets, notas):
    listaNormal = ["Notas de Conhecimento Geral na modalidade de {}", "Notas no 1º dia da 2ª fase na modalidade de {}",
    "Notas no 2º dia da 2ª fase na modalidade de {}", "Notas da Redação na modalidade de {}", "Notas Finais na modalidade de {}"]
    listaGeral = ["Notas de Conhecimento Geral", "Notas no 1º dia da 2ª fase", "Notas no 2º dia da 2ª fase", "Notas da Redação", "Notas Finais"]
    normais = ["AC", "EP", "PPI"]
    if categoria in normais:
        for count, dataset in enumerate(datasets):
            graficoIndividual(categoria, dataset, listaNormal[count], notas[count])
    else:
        for count, dataset in enumerate(datasets):
            graficoIndividual(categoria, dataset, listaGeral[count], notas[count])

# ---------------------- Execução do Programa ----------------------

conn = sqlite3.connect('fuvest')
cur = conn.cursor()
criacao = input("Você deseja criar um pdf para uma nova turma? ('S' para sim e 'N' para não) ")

if criacao.lower() == 's':
    arquivoCSV = input("Digite o link da planilha: ")
    unidade = input("Qual sua unidade de ensino? (ex: Poli) ")
    curso = input("Qual o seu curso? ")
    turma = int(input("Qual o seu ano de ingresso? "))
    cur.execute("INSERT INTO Turma(ano, link) VALUES (?, ?)", (turma, arquivoCSV))
    cur.execute("SELECT id from Turma where ano = (?)", (turma,))
    turmaTuple = cur.fetchall()
    turma_id = list(turmaTuple[0])[0]
    cur.execute("INSERT INTO Curso(nome, turma_id) VALUES (?, ?)", (curso, turma_id))
    cur.execute("SELECT id from Curso where nome = (?)", (curso,))
    cursoTuple = cur.fetchall()
    curso_id = list(cursoTuple[0])[0]
    cur.execute("INSERT INTO Unidade(nome, curso_id) VALUES (?, ?)", (unidade, curso_id))

elif criacao.lower() == 'n':
    atualSair = input("Você deseja atualizar um pdf ou sair? (escreva 'atualizar' ou 'sair') ")
    if atualSair.lower() == "atualizar":
        encontrado = 1
        atualizarURLpanilha = input("Você deseja atualizar o link da planilha? ('S' para sim e 'N' para não) ")
        
        if atualizarURLpanilha.lower() == 's':
            arquivoCSV = input("Digite o novo link da planilha: ")

        unidade = input("Qual sua unidade de ensino? (ex: Poli) ")
        curso = input("Qual o seu curso? ")
        turma = int(input("Qual o seu ano de ingresso? "))
        cur.execute("SELECT id FROM Unidade WHERE nome=(?)", (unidade,))
        unidadeTuple = cur.fetchall()
        unidadeLista = list(unidadeTuple)
        cur.execute("SELECT id FROM Curso WHERE nome=(?)", (curso,))
        cursoTuple = cur.fetchall()
        cursoLista = list(cursoTuple)
        cur.execute("SELECT id FROM Turma WHERE ano=(?)", (turma,))
        turmaTuple = cur.fetchall()
        turmaLista = list(turmaTuple)
        if len(unidadeLista) == 0:
            print("Unidade não encontrada")
            encontrado = 0
        elif len(cursoLista) == 0:
            print("Curso não encontrado")
            encontrado = 0
        elif len(turmaLista) == 0:
            print("Turma não encontrada")
            encontrado = 0
        if encontrado == 1:
            print("Sua seleção foi encontrada")
            # passar o valor de arquivo csv aqui
            cur.execute("SELECT Turma.link FROM Unidade JOIN Curso JOIN Turma ON Unidade.curso_id = Curso.id AND Curso.turma_id = Turma.id")
            linkTuple = cur.fetchall()
            arquivoCSV = list(linkTuple[0])[0]
        else:
            sys.exit()
    elif atualSair.lower() == "sair":
        sys.exit()
    else:
        print("Digite um comando válido")
        sys.exit()
else:
    print("Digite um comando válido")
    sys.exit()
conn.commit()
str(turma)
if not os.path.isdir("{}/{}/{}".format(unidade, curso, str(turma))):
    os.makedirs("{}/{}/{}".format(unidade, curso, str(turma)))
    
# Leio o arquivo csv
geral = pd.read_csv(arquivoCSV)

# Crio tabelas a partir das modalidades
ac = geral[geral.Modalidade == "AC"]
ep = geral[geral.Modalidade == "EP"]
ppi = geral[geral.Modalidade == "PPI"]
categorias = {"Geral": geral, "AC": ac, "EP": ep, "PPI": ppi}
# Crio uma pizza com a porcentagem de ingressos por chamada
chamadas = geral.pivot_table(index=["Chamada"], aggfunc="size")
chamadakeys = chamadas.keys().tolist()
chamadavalues = chamadas.values.tolist()
criaChamadaGrafico(chamadakeys, chamadavalues)

# Crio uma tabela para os comentários e formato para p tags de HTML
comentarios = geral["Comentário"].tolist()
commentsHTMLFormat = comentarioHTML(comentarios)

#Crio os gráficos
criaDados(categorias, notas)

# Crio a página html
html_str = f'''<!DOCTYPE html>
<html>
    <head>
        <title>Fuvest 2020</title>
        <meta charset="utf-8">
        <link rel= "stylesheet" type="text/css" href= "../../../style.css" />

    </head>
    <body>
        <img id = "logo" src ="../../../LogoUSP.png"/>
        <h1 id= "titulo" ">Fuvest 2020 - {curso} {turma} - {unidade}</h1>
        <h1 class = "subtitulo" >Dados informativos acerca das aprovações da Fuvest 2020</h1>
        
            <h2 class = "categoria" >Geral</h2>
            <p>{categoriasDados["Geral"][0]}</p>
            <p>{categoriasDados["Geral"][1]}</p>
            <p>{categoriasDados["Geral"][2]}</p>
            <p>{categoriasDados["Geral"][3]}</p>
            <p>{categoriasDados["Geral"][4]}</p>
            
            <h2 class = "categoria" >AC</h2>
            <p>{categoriasDados["AC"][0]}</p>
            <p>{categoriasDados["AC"][1]}</p>
            <p>{categoriasDados["AC"][2]}</p>
            <p>{categoriasDados["AC"][3]}</p>
            <p>{categoriasDados["AC"][4]}</p>
            
            <h2 class = "categoria" >EP</h2>
            <p>{categoriasDados["EP"][0]}</p>
            <p>{categoriasDados["EP"][1]}</p>
            <p>{categoriasDados["EP"][2]}</p>
            <p>{categoriasDados["EP"][3]}</p>
            <p>{categoriasDados["EP"][4]}</p>
            
            <h2 class = "categoria" >PPI</h2>
            <p>{categoriasDados["PPI"][0]}</p>
            <p>{categoriasDados["PPI"][1]}</p>
            <p>{categoriasDados["PPI"][2]}</p>
            <p>{categoriasDados["PPI"][3]}</p>
            <p>{categoriasDados["PPI"][4]}</p>
        </br>
        
        <h1 class = "subtitulo" >Ocupação do curso por chamada</h1>
            <img id = "pizza" src="chamadas.jpg">
        
        <h1 class = "subtitulo" >Gráficos por modalidade</h1> 
        <h1 class = "categoria" >Ampla Concorrência</h1>
                <img class = "graficos" src="AC/acConhecimento.jpg" alt="Histograma com as notas de Conhecimento Geral">
                <img class = "graficos" src="AC/acFase21.jpg" alt="Histograma com as notas do primeiro dia da segunda fase">
                <br>
                <img class = "graficos" src="AC/acFase22.jpg" alt="Histograma com as notas do segundo dia da segunda fase">
                <img class = "graficos" src="AC/acRedacao.jpg" alt="Histograma com as notas da redação">
                <br>
                <img class = "graficos" src="AC/acFinal.jpg" alt="Histograma com as notas finais">
                <br>
        
        <h1 class = "categoria" >Escola Pública</h1>
                <img class = "graficos" src="EP/epConhecimento.jpg" alt="Histograma com as notas de Conhecimento Geral" class="center">
                <img class = "graficos" src="EP/epFase21.jpg" alt="Histograma com as notas do primeiro dia da segunda fase" class="center">
                <br>
                <img class = "graficos" src="EP/epFase22.jpg" alt="Histograma com as notas do segundo dia da segunda fase" class="center">
                <img class = "graficos" src="EP/epRedacao.jpg" alt="Histograma com as notas da redação" class="center">
                <br>
                <img class = "graficos" src="EP/epFinal.jpg" alt="Histograma com as notas finais" class="center">
        
        <h1 class = "categoria" >Pretos, Pardos e Indígenas</h1>
                <img class = "graficos" src="PPI/ppiConhecimento.jpg" alt="Histograma com as notas de Conhecimento Geral" class="center">
                <img class = "graficos" src="PPI/ppiFase21.jpg" alt="Histograma com as notas do primeiro dia da segunda fase" class="center">
                <br>
                <img class = "graficos" src="PPI/ppiFase22.jpg" alt="Histograma com as notas do segundo dia da segunda fase" class="center">
                <img class = "graficos" src="PPI/ppiRedacao.jpg" alt="Histograma com as notas da redação" class="center">
                <br>
                <img class = "graficos" src="PPI/ppiFinal.jpg" alt="Histograma com as notas finais" class="center">
        
        <h1 class = "subtitulo" >Mensagens dos Veteranos</h1>
                {commentsHTMLFormat}
            
    </body>
</html>'''

html_file= open("{}/{}/{}/index.html".format(unidade, curso, turma),"w")
html_file.write(html_str)
html_file.close()

# Converto a página html para pdf
pdfkit.from_file("./{}/{}/{}/index.html".format(unidade, curso, turma), "./{}/{}/{}/dados.pdf".format(unidade, curso, turma))