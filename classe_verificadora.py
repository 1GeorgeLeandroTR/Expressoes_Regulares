import re
class MinhaVariavel:
    def __init__(self):
        self.dicionario_variavel= {}
    def get_valor(self,valor):
        return self.dicionario_variavel.get(valor)

    def add_valor(self,string_chave,object_valor):
        self.dicionario_variavel[string_chave] = object_valor

class Validador:
    def __init__(self,string_file,string_inicio,string_fim):
        self.listaPcerto = []
        self.listaErrado = []
        self.linhasErradas = []
        self.string_file = string_file
        self.linhaTxt = self.contaLinha(string_file)
        self.MinhaVariavelDeClasse = MinhaVariavel()
        self.inicio = re.compile(string_inicio)
        self.fim = re.compile(string_fim)

    def add_regex(self,string_nome_regex, object_valor_regex):
        self.MinhaVariavelDeClasse.add_valor(string_nome_regex, object_valor_regex)

    def get_regex(self,string_nome_regex):
        var_classe = self.MinhaVariavelDeClasse
        var_regex = var_classe.get_valor(string_nome_regex)
        return re.compile(var_regex)

    def contaLinha(self,fname): #contador de linhas do arquivo
        def _make_gen(reader):
            while True:
                b = reader(2 ** 16)
                if not b: break
                yield b
        with open(fname, "rb") as f:
            count = sum(buf.count(b"\n") for buf in _make_gen(f.raw.read))
        return count

    def verificaLinha(self,Regex_parada,String_ArquivoNome,int_linha, callback_verificacao=None):
    #vai verificar se há erros até o regex de parada(begin)
        Meu_arquivo = open(String_ArquivoNome)
        arquivo = Meu_arquivo.readlines()
        primeiro = int_linha
        while Regex_parada.search(arquivo[int_linha]) == None:
            if int_linha == primeiro:
                int_linha +=1
            callback_verificacao(arquivo[int_linha],self.listaErrado,int_linha,self.linhasErradas)#Aqui você usa a função de validação que você quiser, usando a linha como parâmetro
            int_linha += 1
        return self.listaErrado, int_linha

    def erro_s(self):
        str_erros = str(self.linhasErradas).replace('[','').replace(']','')
        if len(self.listaErrado)>1:
            return str(len(self.listaErrado))+" erros, eles estão nas linhas "+str_erros
        return "1 erro na linha "+str_erros

    def executa_verificacao(self,minhaCallback):
        #vai percorrer o arquivo linha a linha procurando pelo regex de partida(declare)
        #a minhaCallback é a função que você irá usar para realizar a validação
        arquivo = open(self.string_file)
        for linha in range(self.linhaTxt):
            minhaLinha = arquivo.readline()
            if minhaLinha != None:
                erros = self.verificaLinha(self.fim, self.string_file,linha,minhaCallback)
                break
        if len(erros[0]) > 0:
            raise Exception("você tem "+self.erro_s())

##EXEMPLO DE USO
teste = Validador(string_file="hello.txt",string_fim=r'begin',string_inicio=r'declare')
teste.add_regex("variavel",r'v_[s|S|d|D|c|C](.*) char[$|(]|varchar$|number$')

def minhaCallBack1(arquivo, listaDeErro, numeroLinha, listaLinha):
    if arquivo == "\n":
        return

    if teste.get_regex("variavel").search(arquivo) == None:
        listaDeErro.append(arquivo)
        listaLinha.append(numeroLinha+1)
        print("esse tá errado: "+ str(arquivo))

teste.executa_verificacao(minhaCallBack1)