# fuvest-data
Script para criação de PDF com gráficos acerca dos aprovados de um curso pela Fuvest e com mensagens de veteranos.

### Instalando o repositório
    Para obter o repositório, use o seguinte comando:
    '''git clone https://github.com/kibonusp/fuvest-data.git'''
    Para poder executar o programa, é necessário ter as bibliotecas **pandas**, **numpy**. **matplotlib** e **pdfkit**

    Para instalar a biblioteca pandas, use o seguinte comando:
    '''sudo pip install pandas'''

    Para instalar a biblioteca numpy, use o seguinte comando:
    '''sudo pip install numpy'''

    Para instalar a biblioteca matplotlib, use o seguinte comando:
    '''sudo pip install matplotlib'''

    Para instalar a biblioteca pdfkit, use o seguinte comando:
    '''npm install pdfkit'''

### Obtendo o CSV de um Google Sheets a partir de um Google Forms
    O programa funciona a partir da criação de um Google Forms com as perguntas equivalentes a desse:
<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSehxLmWWNWmVPkploww2h7hCckEc1VyT2lH5xql12aoZbdaJg/viewform?embedded=true" width="640" height="1614" frameborder="0" marginheight="0" marginwidth="0">Carregando…</iframe>

    Ao visualizar as respostas do seu Google Forms, é possível abrir uma planilha do Google Sheets com as respostas do formulário:
    IMAGES/forms.png

    Uma vez dentro da planilha, é preciso pegar a url relativa ao csv dessa planilha.
    IMAGES/planilha1.png
    IMAGES/planilha2.png

### Executando o programa

    Para executar o programa, use o comando:
    '''python3 main.py'''

    O programa irá perguntar se você deseja criar um PDF para uma nova turma ou não.

##### Escolhendo sim
    Caso você tenha escolhido sim, o programa pede a url do googlesheets obtida anteriormente.
    Após isso, perguntará o nome da sua unidade de ensino, do seu curso e o seu ano de ingresso.
    Uma vez preenchidas as perguntas, o programa deverá ter criado uma pasta contendo o PDF, os gráficos e uma página HTML e terminará sua execução.
    Usufrua do que estiver interessado.
    
##### Escolhendo não
    Caso você tenha escolhido não, o programa perguntará se você deseja atualizar os dados ou se deseja sair.
    Caso tenha escolhido atualizar, o PDF, os gráficos e o html serão atualizados dada a condição da planilha no momento.
    Caso contrário, o programa encerrará sua execução.