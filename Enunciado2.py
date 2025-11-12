"""
private int search(String pat, String txt) {
   int M = pat.length();
   int N = txt.length();
   long patHash = hash(pat, M);

   for (int i = 0; i <= N - M; i++) {
      long txtHash = hash(txt.subtring(i, i+M), M);
      if (patHash == txtHash)
         return i; // ocorrência? colisão?
   }
   return N; // nenhuma ocorrência
}

//Notação: o padrão tem M caracteres, o texto tem N caracteres, o alfabeto tem R caracteres  (0 … R−1) 
//              Q é o módulo para o cálculo do Hash.
//              Qual o valor de Q?  Escolha Q igual a um primo grande para minimizar a chance de colisões.
//                       Por exemplo: o maior primo que possa ser representado com um int

private long hash(String s, int M) {
   long h = 0;
   for (int j = 0; j < M; j++)
      h = (h * R + s.charAt(j)) % Q;
   return h;
}
"""

def hash(s, M):
    h = 0
    R = 256
    Q = 2147483647
    for j in range(M):
        h = ((h * R + ord(s[j])) % Q)

    return h


def search(pat, txt):
    M = len(pat)
    N = len(txt)
    patHash = hash(pat, M)

    for i in range(N-M):
        txtHash = hash(txt[i:(i+M)], M)
        if patHash == txtHash:
            return i
    
    return N

s1 = 'ABCDCBDCBDAADFCBDABDCBADF'
s2 = 'ADF'

resposta = search(s2, s1)

print(f"Primeira ocorrência: {resposta}")
