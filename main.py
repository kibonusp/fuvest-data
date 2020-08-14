import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pdfkit

categorias = ["Geral", "AC", "EP", "PPI"]

categoriasDados = dict()

def printaDados(categoria, conhecimento, fase2_1, fase2_2, redacao, final):
    conhecimentoString = "A média da categoria " + categoria + " em Conhecimentos Gerais foi {}".format(round(np.mean(conhecimento), 2))
    fase21String = "A média da categoria " + categoria + " no 1º dia da 2ª fase foi {}".format(round(np.mean(fase2_1), 2))
    fase22String = "A média da categoria " + categoria + " no 2º dia da 2ª fase foi {}".format(round(np.mean(fase2_2), 2))
    redacaoString = "A média da categoria " + categoria + " em Redação foi {}".format(round(np.mean(redacao), 2))
    finalString = "A média da categoria " + categoria + " na Nota Final foi {}".format(round(np.mean(final),2))
    categoriasDados[categoria] = [conhecimentoString, fase21String, fase22String, redacaoString, finalString]

def criandoGraficosGeral(categoria, conhecimento, fase2_1, fase2_2, redacao, final):
    # Gráfico de Conhecimentos Gerais
    conheciFigura = plt.figure()
    conheciGrafico = conheciFigura.add_subplot(111)
    conheciGrafico.hist(conhecimento, bins=20)
    conheciGrafico.set_xlabel("Notas")
    conheciGrafico.set_ylabel("Quantidade")
    conheciGrafico.set_title("Notas de Conhecimento Geral")
    plt.savefig("./Geral/GeralConhecimento.jpg")
    plt.cla()

    # Gráfico do dia 1 da fase 2
    fase21Figura = plt.figure()
    fase21Grafico = fase21Figura.add_subplot(111)
    fase21Grafico.hist(fase2_1, bins=20)
    fase21Grafico.set_xlabel("Notas")
    fase21Grafico.set_ylabel("Quantidade")
    fase21Grafico.set_title("Notas no 1º dia da 2ª fase")
    plt.savefig("./Geral/GeralFase21.jpg")
    plt.cla()

    # Gráfico do dia 2 da fase 2ª fase
    fase22Figura = plt.figure()
    fase22Grafico = fase22Figura.add_subplot(111)
    fase22Grafico.hist(fase2_2, bins=20)
    fase22Grafico.set_xlabel("Notas")
    fase22Grafico.set_ylabel("Quantidade")
    fase22Grafico.set_title("Notas no 2º dia da 2ª fase")
    plt.savefig("./Geral/GeralFase22.jpg")
    plt.cla()

    # Gráfico da Redação
    redacaoFigura = plt.figure()
    redacaoGrafico = redacaoFigura.add_subplot(111)
    redacaoGrafico.hist(redacao, bins=20)
    redacaoGrafico.set_xlabel("Notas")
    redacaoGrafico.set_ylabel("Quantidade")
    redacaoGrafico.set_title("Notas da Redação")
    plt.savefig("./Geral/GeralRedacao.jpg")
    plt.cla()

    # Gráfico da Nota Final
    finalFigura = plt.figure()
    finalGrafico = finalFigura.add_subplot(111)
    finalGrafico.hist(final, bins=50)
    finalGrafico.set_xlabel("Notas")
    finalGrafico.set_ylabel("Quantidade")
    finalGrafico.set_title("Notas Finais")
    plt.savefig("./Geral/GeralFinal.jpg")
    plt.cla()

def criandoGraficos(categoria, conhecimento, fase2_1, fase2_2, redacao, final):
    if categoria == "Geral":
        criandoGraficosGeral(categoria, conhecimento, fase2_1, fase2_2, redacao, final)
    else:
        # Gráfico de Conhecimentos Gerais
        conheciFigura = plt.figure()
        conheciGrafico = conheciFigura.add_subplot(111)
        conheciGrafico.hist(conhecimento, bins=20)
        conheciGrafico.set_xlabel("Notas")
        conheciGrafico.set_ylabel("Quantidade")
        conheciGrafico.set_title("Notas de Conhecimento Geral na modalidade de {}".format(categoria))
        plt.savefig("./{}/{}Conhecimento.jpg".format(categoria, categoria.lower()))
        plt.cla()

        # Gráfico do dia 1 da fase 2
        fase21Figura = plt.figure()
        fase21Grafico = fase21Figura.add_subplot(111)
        fase21Grafico.hist(fase2_1, bins=20)
        fase21Grafico.set_xlabel("Notas")
        fase21Grafico.set_ylabel("Quantidade")
        fase21Grafico.set_title("Notas no 1º dia da 2ª fase na modalidade de {}".format(categoria))
        plt.savefig("./{}/{}Fase21.jpg".format(categoria, categoria.lower()))
        plt.cla()

        # Gráfico do dia 2 da fase 2ª fase
        fase22Figura = plt.figure()
        fase22Grafico = fase22Figura.add_subplot(111)
        fase22Grafico.hist(fase2_2, bins=20)
        fase22Grafico.set_xlabel("Notas")
        fase22Grafico.set_ylabel("Quantidade")
        fase22Grafico.set_title("Notas no 2º dia da 2ª fase na modalidade de {}".format(categoria))
        plt.savefig("./{}/{}Fase22.jpg".format(categoria, categoria.lower()))
        plt.cla()

        # Gráfico da Redação
        redacaoFigura = plt.figure()
        redacaoGrafico = redacaoFigura.add_subplot(111)
        redacaoGrafico.hist(redacao, bins=20)
        redacaoGrafico.set_xlabel("Notas")
        redacaoGrafico.set_ylabel("Quantidade")
        redacaoGrafico.set_title("Notas da Redação na modalidade de {}".format(categoria))
        plt.savefig("./{}/{}Redacao.jpg".format(categoria, categoria.lower()))
        plt.cla()

        # Gráfico da Nota Final
        finalFigura = plt.figure()
        finalGrafico = finalFigura.add_subplot(111)
        finalGrafico.hist(final, bins=50)
        finalGrafico.set_xlabel("Notas")
        finalGrafico.set_ylabel("Quantidade")
        finalGrafico.set_title("Notas Finais na modalidade de {}".format(categoria))
        plt.savefig("./{}/{}Final.jpg".format(categoria, categoria.lower()))
        plt.cla()

        plt.close()
        

def criaDados(categorias, Geral, ac, ep, ppi):
    for categoria in categorias:
        if not os.path.isdir(categoria):
            os.makedirs(categoria)
        if categoria == "Geral":
            conhecimentoGeral = Geral["Conhecimentos Gerais"].values.tolist()
            fase2_1Geral = Geral["2ª fase - 1º dia"].values.tolist()
            fase2_2Geral =  Geral["2ª fase - 2º dia"].values.tolist()
            redacaoGeral = Geral["Redação"].values.tolist()
            finalGeral = Geral["Nota Final"].values.tolist()
            printaDados(categoria, conhecimentoGeral, fase2_1Geral, fase2_2Geral, redacaoGeral, finalGeral)
            criandoGraficos(categoria, conhecimentoGeral, fase2_1Geral, fase2_2Geral, redacaoGeral, finalGeral)
        elif categoria == "AC":
            conhecimentoAC = ac["Conhecimentos Gerais"].values.tolist()
            fase2_1AC = ac["2ª fase - 1º dia"].values.tolist()
            fase2_2AC =  ac["2ª fase - 2º dia"].values.tolist()
            redacaoAC = ac["Redação"].values.tolist()
            finalAC = ac["Nota Final"].values.tolist()
            printaDados(categoria, conhecimentoAC, fase2_1AC, fase2_2AC, redacaoAC, finalAC)
            criandoGraficos(categoria, conhecimentoAC, fase2_1AC, fase2_2AC, redacaoAC, finalAC)
        elif categoria == "EP":
            conhecimentoEP = ep["Conhecimentos Gerais"].values.tolist()
            fase2_1EP = ep["2ª fase - 1º dia"].values.tolist()
            fase2_2EP =  ep["2ª fase - 2º dia"].values.tolist()
            redacaoEP = ep["Redação"].values.tolist()
            finalEP = ep["Nota Final"].values.tolist()
            printaDados(categoria, conhecimentoEP, fase2_1EP, fase2_2EP, redacaoEP, finalEP)
            criandoGraficos(categoria, conhecimentoEP, fase2_1EP, fase2_2EP, redacaoEP, finalEP)
        elif categoria == "PPI":
            conhecimentoPPI = ppi["Conhecimentos Gerais"].values.tolist()
            fase2_1PPI = ppi["2ª fase - 1º dia"].values.tolist()
            fase2_2PPI =  ppi["2ª fase - 2º dia"].values.tolist()
            redacaoPPI = ppi["Redação"].values.tolist()
            finalPPI = ppi["Nota Final"].values.tolist()
            printaDados(categoria, conhecimentoPPI, fase2_1PPI, fase2_2PPI, redacaoPPI, finalPPI)
            criandoGraficos(categoria, conhecimentoPPI, fase2_1PPI, fase2_2PPI, redacaoPPI, finalPPI)

def criaChamadaGrafico (chamadakeys, chamadavalues):
    chamadaFigura = plt.figure()
    chamadaGrafico = chamadaFigura.add_subplot(111)
    chamadaGrafico.pie(chamadavalues, labels=chamadakeys, autopct="%1.2f%%")
    chamadaGrafico.set_title("Porcentagem de ingressos em cada chamada")
    plt.savefig("chamadas.jpg")
    plt.cla()

def comentarioHTML (comentarios):
    comentarioList = []
    '''
    <p>Comentario1</p>
    <p>Comentario2</p>
    <p>Comentario3</p>
    '''
    comentarios = [comentario for comentario in comentarios if str(comentario) != 'nan']
    for comentario in comentarios:
        if comentario:
            comentarioList.append("<p>{}</p>".format(comentario))
    comentarioString = "\n".join(comentarioList)
    return comentarioString

# Planilha 2020: https://docs.google.com/spreadsheets/d/e/2PACX-1vS7-ibfSlLbqw3L6lhcXCIOK1KA2TJhIoCQfM5RXJmzvs2EGPHm3GvWdgYSf7cc3a0jqIZizvjtie1o/pub?gid=1644314308&single=true&output=csv
arquivoCSV = input("Digite o link da planilha: ")
Geral = pd.read_csv(arquivoCSV)
ac = Geral[(Geral.Modalidade == "AC")]
ep = Geral[Geral.Modalidade == "EP"]
ppi = Geral[Geral.Modalidade == "PPI"]
comentarios = Geral["Comentário"].tolist()
comentsHTMlFormat = comentarioHTML(comentarios)
chamadas = Geral.pivot_table(index=["Chamada"], aggfunc="size")
chamadakeys = chamadas.keys().tolist()
chamadavalues = chamadas.values.tolist()
criaDados(categorias, Geral, ac, ep, ppi)
criaChamadaGrafico(chamadakeys, chamadavalues)

html_str = '''<!DOCTYPE html>
<html>
    <head>
        <title>Dados acerca da Fuvest 2020</title>
        <meta charset="utf-8">
    </head>
    <body>
        <p style="font-size: 50px; font-weight: bold; font-family: Lato; text-align: center;">Dados acerca da Fuvest 2020</p>
        <h1 align="center">Dados informativos acerca das aprovações da Fuvest 2020</h1>
        <center>
            <h2>Geral</h2>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <h2>AC</h2>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <h2>EP</h2>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <h2>PPI</h2>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
            <p>{}</p>
        </center>
        </br>
        <h1 align="center">Ocupação do curso por chamada</h1>
            <center><img src="chamadas.jpg" width=500 height=500></center>
        <h1 align="center">Ampla Concorrência</h1>
            <center>
                <img src="AC/acConhecimento.jpg" alt="Histograma com as notas de Conhecimento Geral">
                <img src="AC/acFase21.jpg" alt="Histograma com as notas do primeiro dia da segunda fase">
                <br>
                <img src="AC/acFase22.jpg" alt="Histograma com as notas do segundo dia da segunda fase">
                <img src="AC/acRedacao.jpg" alt="Histograma com as notas da redação">
                <br>
                <img src="AC/acFinal.jpg" alt="Histograma com as notas finais">
                <br>
            </center>
        <h1 align="center">Escola Pública</h1>
            <center>
                <img src="EP/epConhecimento.jpg" alt="Histograma com as notas de Conhecimento Geral" class="center">
                <img src="EP/epFase21.jpg" alt="Histograma com as notas do primeiro dia da segunda fase" class="center">
                <br>
                <img src="EP/epFase22.jpg" alt="Histograma com as notas do segundo dia da segunda fase" class="center">
                <img src="EP/epRedacao.jpg" alt="Histograma com as notas da redação" class="center">
                <br>
                <img src="EP/epFinal.jpg" alt="Histograma com as notas finais" class="center">
            </center>
        <h1 align="center">Pretos, Pardos e Indígenas</h1>
            <center>
                <img src="PPI/ppiConhecimento.jpg" alt="Histograma com as notas de Conhecimento Geral" class="center">
                <img src="PPI/ppiFase21.jpg" alt="Histograma com as notas do primeiro dia da segunda fase" class="center">
                <br>
                <img src="PPI/ppiFase22.jpg" alt="Histograma com as notas do segundo dia da segunda fase" class="center">
                <img src="PPI/ppiRedacao.jpg" alt="Histograma com as notas da redação" class="center">
                <br>
                <img src="PPI/ppiFinal.jpg" alt="Histograma com as notas finais" class="center">
            </center>
        <h1 align="center">Mensagens dos Veteranos</h1>
            <center>
                {}
            </center>
    </body>
</html>'''.format(categoriasDados["Geral"][0], categoriasDados["Geral"][1], categoriasDados["Geral"][2], categoriasDados["Geral"][3],
categoriasDados["Geral"][4], categoriasDados["AC"][0], categoriasDados["AC"][1], categoriasDados["AC"][2], categoriasDados["AC"][3],
categoriasDados["AC"][4], categoriasDados["EP"][0], categoriasDados["EP"][1], categoriasDados["EP"][2], categoriasDados["EP"][3],
categoriasDados["EP"][4], categoriasDados["PPI"][0], categoriasDados["PPI"][1], categoriasDados["PPI"][2], categoriasDados["PPI"][3],
categoriasDados["PPI"][4], comentsHTMlFormat
)
html_file= open("index.html","w")
html_file.write(html_str)
html_file.close()

# Criando pdf
pdfkit.from_file("index.html", "dados.pdf")