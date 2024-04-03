import Lex3 as lex
#Lucas Marques - 120129605

class Syntaxx_Error:
    def __init__(esperado):
        print('Erro, esperava-se {}'.format(esperado))
class Assert_False:
    def __init__(self):
        print('Erro de compilação')


class Exp_Num:
    def __init__(self, n):
        self.tag = 'ExpNum'
        self.n = n
class Exp_Bin:
    def __init__(self, op, e1, e2):
        self.tag = 'ExpBin'
        self.op = op
        self.e1 = e1
        self.e2 = e2
class Exp_Nome:
    def __init__(self, nome, exp):
        self.tag = 'Exp_Nome'
        self.nome = nome
        self.exp = exp
        self.valor = CmdAtribui(nome, exp)
        

def calcula(exp):
    if exp.tag == 'ExpNum':
        return exp.n
    if exp.tag == 'ExpBin':
        v1 = calcula(exp.e1)
        v2 = calcula(exp.e2)
        if exp.op == '+':
            return v1 + v2
        elif exp.op == '-':
            return v1 - v2
        elif exp.op == '*':
            return v1 * v2
        elif exp.op == '/':
            return v1/v2


def CmdAtribui(x, exp):
    calcula(exp)
    x = exp
    return x

def CmdPrint(exp):
    print(exp)

def come(token):
    return token.valor




def parseProg(tokens):
    linha = []
    i = 0
    if tokens[i] != ';':
        linha.append(tokens[i])
        tokens[i].pop
        i+=1
    else:
         return tok

def parseCmd(tokens):
    c = 0
    if (tokens[c].tag == 'NOME'):
        print('entrei', tokens[c])
        x = come(tokens[c]) #come o nome da variável
        c+=1
        #verifica qual o operador, para fazer a operação certa
        if tokens[c].valor == '=':
            #print('entre', tokens[c])
            e1 = tokens[c+1]
            op = tokens[c+2]
            e2 = tokens[c+3]
            exp = Exp_Bin(op, e1, e2)
            return CmdAtribui(x, exp)
        elif tokens[c].valor == '+':
            #print('entre', tokens[c])
            e1 = tokens[c+1]
            op = tokens[c+2]
            e2 = tokens[c+3]
            exp = Exp_Bin(op, e1, e2)
            return calcula(exp)
        elif tokens[c].valor == '-':
            #print('entre', tokens[c])
            e1 = tokens[c+1]
            op = tokens[c+2]
            e2 = tokens[c+3]
            exp = Exp_Bin(op, e1, e2)
            return calcula(exp)
        elif tokens[c].valor == '*':
            #print('entre', tokens[c])
            e1 = tokens[c+1]
            op = tokens[c+2]
            e2 = tokens[c+3]
            exp = Exp_Bin(op, e1, e2)
            return calcula(exp)
        else:
            Syntaxx_Error('OPERADOR')
    elif (tokens[c].valor == 'print'):
        #print('entre', tokens[c])
        come(tokens[c]) #come o token print
        c+=1
        exp = ''
        if tokens[c] == '(': #verifica se abriu parenteses
            #print('entre', tokens[c])
            come(tokens[c]) #come o abre parenteses
            c+=1
            while tokens[c].valor != ')':
                exp += come(tokens[c])
                CmdPrint(parseCmd(exp))
        else:
            Syntaxx_Error('(')
    else:
        Assert_False



#cria lista com todos os tokens do programa
tokens = lex.main()
contador = tokens.count(';')
tok = []
for i in range(contador):
    tok.append(parseProg)
parseCmd(tok)