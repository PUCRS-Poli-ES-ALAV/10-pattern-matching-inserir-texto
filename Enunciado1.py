iteracoes = 0
instrucoes = 0

def procura(s1, s2):
    global iteracoes
    global instrucoes
    j = 0
    aux = -1
    instrucoes += 3
    for i in range(len(s1)):
        iteracoes += 1
        instrucoes += 11
        if j == len(s2):
                    instrucoes += 1
                    return aux
        if s2[j] == s1[i] or s1[i-1] == s2[j]:
            instrucoes += 3
            if aux == -1:
                aux = i
                instrucoes += 5
                if s1[i-1] == s2[j]:
                    instrucoes += 5
                    aux = i-1
                    if s2[j] == s1[i]:
                        instrucoes += 2
                        j += 1
            j += 1
        else:
            instrucoes += 2
            j = 0
            aux = -1
    instrucoes += 1
    return aux

s1 = 'ABCDCBDCBDAADFCBDABDCBADF'
s2 = 'ADF'

resposta = procura(s1, s2)
if(resposta == -1):
    print('s2 não foi encontrado em s1!')

print(f"Primeira ocorrência: {resposta}")
print(f"Iterações: {iteracoes}")
print(f"Instruções: {instrucoes}")