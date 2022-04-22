import re
def contaLinha(fname): #contador de linhas do arquivo
    def _make_gen(reader):
        while True:
            b = reader(2 ** 16)
            if not b: break
            yield b
    with open(fname, "rb") as f:
        count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))
    return count

def verificaLinha(Regex_parada,String_ArquivoNome,int_linha):
#vai verificar se há erros até o regex de parada(begin)
    Meu_arquivo = open(String_ArquivoNome)
    arquivo = Meu_arquivo.readline()
    while Regex_parada.search(arquivo) == None:
        if variavelEtapa1(arquivo, listaPcerto):
            variavelEtapa2(arquivo, listaErrado)

        arquivo = Meu_arquivo.readline()
        int_linha += 1
    return listaErrado, int_linha

def variavelEtapa1(arquivo,possivelCerto):
# método para verificar se é uma variável ou não, vai se for parecido com uma variável correta entao entra na lista
    arq = variavel1.search(arquivo)
    if arq != None:
        possivelCerto.append(arquivo)
        return True
    return False

def variavelEtapa2(linha,lista):
#vai verificar qual variável é de fato correta, correndo pela lista criada na etapa anterior
    arq = variavel2.search(linha)
    if arq == None:
        lista.append(linha)

listaPcerto = []
listaErrado = []
txt = open("hello.txt")
linhaTxt = contaLinha("hello.txt")
inicio = re.compile(r'declare')
fim = re.compile(r'begin')
variavel1 = re.compile(r'v_[s|S|d|D|c|C]') #regex de ver se é variável
variavel2 = re.compile(r'v_[s|S|d|D|c|C](.*) char[$|(]|varchar$|number$') #regex de ver a variável tá correta

def erro_s():
    if len(listaErrado)>1:
        return " erros"
    return " erro"

#vai percorrer o arquivo linha a linha procurando pelo regex de partida(declare)
for linha in range(linhaTxt):
    minhaLinha = txt.readline()
    if minhaLinha != None:
        erros = verificaLinha(fim, "hello.txt",linha)
        if len(erros[0]) > 0:
            raise Exception("você tem " + str(len(listaErrado)) + erro_s()+" na linha "+str(erros[1]))
        break