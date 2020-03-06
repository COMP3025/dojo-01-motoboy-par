import itertools

def recebearquivo(arquivo):
    file = open(arquivo, 'r')
    return file

def calculomaiortemp(peso, entregas):
    pedidos = list(itertools.permutations(entregas))

    melhorPedido = 0
    for pedido in pedidos:
        pesoAtual = 0
        tempoAtual = 0
        for entrega in pedido:
           
            if pesoAtual + int(entrega[1]) > peso:
                 break
            else:
                tempoAtual = tempoAtual + int(entrega[0]) 
                pesoAtual = pesoAtual + int(entrega[1])   
        if tempoAtual > melhorPedido:
            melhorPedido = tempoAtual    
    print(melhorPedido)            


def interpretararquivo(arquivo):
    texto = arquivo.read()
    linhas = texto.split('\n')
    linhas.reverse()
    while True:
        numeroentregas = int (linhas.pop()) 
        if numeroentregas == 0:
            break
        peso = int (linhas.pop())
        entregas = []
        for i in range(numeroentregas):
            entregas.append(linhas.pop().split(' '))
        print('Entregas:',entregas,'\nPeso' ,peso)
        calculomaiortemp(peso, entregas)

interpretararquivo(recebearquivo('motoboy.txt'))



