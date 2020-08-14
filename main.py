import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

categorias = ["Tudo", "AC", "EP", "PPI"]

def printaDados(categoria, conhecimento, fase2_1, fase2_2, redacao, final):
    print("A média da categoria", categoria, "em Conhecimentos Gerais foi".format(round(np.mean(conhecimento), 2)))
    print("A média da categoria", categoria, "no 1º dia da 2ª fase foi {}".format(round(np.mean(fase2_1), 2)))
    print("A média da categoria", categoria, "no 2º dia da 2ª fase foi {}".format(round(np.mean(fase2_2), 2)))
    print("A média da categoria", categoria, "em Redação foi {}".format(round(np.mean(redacao), 2)))
    print("A média da categoria", categoria, "na Nota Final foi {}".format(round(np.mean(final),2)))

def criandoGraficosTudo(categoria, conhecimento, fase2_1, fase2_2, redacao, final):
    # Gráfico de Conhecimentos Gerais
    conheciFigura = plt.figure()
    conheciGrafico = conheciFigura.add_subplot(111)
    conheciGrafico.hist(conhecimento, bins=20)
    conheciGrafico.set_xlabel("Notas")
    conheciGrafico.set_ylabel("Quantidade")
    conheciGrafico.set_title("Notas de Conhecimento Geral")
    plt.savefig("./Tudo/tudoConhecimento.jpg")
    plt.cla()

    # Gráfico do dia 1 da fase 2
    fase21Figura = plt.figure()
    fase21Grafico = fase21Figura.add_subplot(111)
    fase21Grafico.hist(fase2_1, bins=20)
    fase21Grafico.set_xlabel("Notas")
    fase21Grafico.set_ylabel("Quantidade")
    fase21Grafico.set_title("Notas no 1º dia da 2ª fase")
    plt.savefig("./Tudo/tudoFase21.jpg")
    plt.cla()

    # Gráfico do dia 2 da fase 2ª fase
    fase22Figura = plt.figure()
    fase22Grafico = fase22Figura.add_subplot(111)
    fase22Grafico.hist(fase2_2, bins=20)
    fase22Grafico.set_xlabel("Notas")
    fase22Grafico.set_ylabel("Quantidade")
    fase22Grafico.set_title("Notas no 2º dia da 2ª fase")
    plt.savefig("./Tudo/tudoFase22.jpg")
    plt.cla()

    # Gráfico da Redação
    redacaoFigura = plt.figure()
    redacaoGrafico = redacaoFigura.add_subplot(111)
    redacaoGrafico.hist(redacao, bins=20)
    redacaoGrafico.set_xlabel("Notas")
    redacaoGrafico.set_ylabel("Quantidade")
    redacaoGrafico.set_title("Notas da Redação")
    plt.savefig("./Tudo/tudoRedacao.jpg")
    plt.cla()

    # Gráfico da Nota Final
    finalFigura = plt.figure()
    finalGrafico = finalFigura.add_subplot(111)
    finalGrafico.hist(final, bins=50)
    finalGrafico.set_xlabel("Notas")
    finalGrafico.set_ylabel("Quantidade")
    finalGrafico.set_title("Notas Finais")
    plt.savefig("./Tudo/tudoFinal.jpg")
    plt.cla()

def criandoGraficos(categoria, conhecimento, fase2_1, fase2_2, redacao, final):
    if categoria == "Tudo":
        criandoGraficosTudo(categoria, conhecimento, fase2_1, fase2_2, redacao, final)
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
        

def criaDados(categorias, tudo, ac, ep, ppi):
    for categoria in categorias:
        print("-------------------------------------------------------------------------------------------")
        if not os.path.isdir(categoria):
            os.makedirs(categoria)
        if categoria == "Tudo":
            conhecimentoTudo = tudo["Conhecimentos Gerais"].values.tolist()
            fase2_1Tudo = tudo["2ª fase - 1º dia"].values.tolist()
            fase2_2Tudo =  tudo["2ª fase - 2º dia"].values.tolist()
            redacaoTudo = tudo["Redação"].values.tolist()
            finalTudo = tudo["Nota Final"].values.tolist()
            printaDados(categoria, conhecimentoTudo, fase2_1Tudo, fase2_2Tudo, redacaoTudo, finalTudo)
            criandoGraficos(categoria, conhecimentoTudo, fase2_1Tudo, fase2_2Tudo, redacaoTudo, finalTudo)
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
        

# Planilha 2020: https://docs.google.com/spreadsheets/d/e/2PACX-1vQ-M1Qo-XJiDiNczwz7AY0vEhSlBvRqMEmPPBfMsks27GYqqIquaTneYklLOzyzwgI_2uIjLNuwhhdx/pub?gid=0&single=true&output=csv
arquivoCSV = input("Digite o link da planilha: ")
tudo = pd.read_csv(arquivoCSV)
ac = tudo[(tudo.Modalidade == "AC")]
ep = tudo[tudo.Modalidade == "EP"]
ppi = tudo[tudo.Modalidade == "PPI"]
chamadas = tudo.pivot_table(index=["Chamada"], aggfunc="size")
chamadakeys = chamadas.keys().tolist()
chamadavalues = chamadas.values.tolist()
criaDados(categorias, tudo, ac, ep, ppi)
criaChamadaGrafico(chamadakeys, chamadavalues)