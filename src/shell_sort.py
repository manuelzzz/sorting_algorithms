def shell_sort(listaA):
    contagemAux = len(listaA)//2
    while contagemAux > 0:
      for posicaoInicial in range(contagemAux):
        gap_insertion_sort(listaA, posicaoInicial, contagemAux)

      contagemAux = contagemAux // 2

def gap_insertion_sort(listaN, inicio, espaco):
    for i in range(inicio + espaco, len(listaN), espaco):

        valorAtual = listaN[i]
        posicao = i

        while posicao>=espaco and listaN[posicao-espaco] > valorAtual:
            listaN[posicao] = listaN[posicao - espaco]
            posicao = posicao - espaco

        listaN[posicao] = valorAtual