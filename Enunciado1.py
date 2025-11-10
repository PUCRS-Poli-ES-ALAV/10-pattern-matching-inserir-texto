def procura(s1, s2):
    j = 0
    aux = -1
    for i in range(len(s1)):
        if s2[j] == s1[i]:
            if aux == -1:
                aux = i
            j += 1
        else:
            j = 0
            aux = -1
    
    return aux

s1 = 'ABCDCBDCBDACBDABDCBADF'
s2 = 'ADF'

resposta = procura(s1, s2)
if(resposta == -1):
    print('s2 não foi encontrado em s1!')

print(f"Primeira ocorrência: {resposta}")