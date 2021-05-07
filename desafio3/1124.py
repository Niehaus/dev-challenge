from math import sqrt

def ultimo_caso(l, c, r1, r2):
    if l == 0 and c == 0 and r1 == 0 and r2 == 0:
        return True
    return False

def check_limits(dados):
    for dado in dados:
        if dado < 1 or dado > 100:
            return False
    return True

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist_ponto2ponto(l, c, r1, r2):
    pontoA = Ponto(r1, r1)
    pontoB = Ponto(l - r2, c - r2)
    
    dist_x = (pontoB.x - pontoA.x) ** 2
    dist_y = (pontoB.y - pontoA.y) ** 2

    dist_p2p = sqrt(dist_x + dist_y)

    return dist_p2p


if __name__ == '__main__':
    l, c, r1, r2 = 1, 1, 1, 1
    while(not ultimo_caso(l, c, r1, r2)):
        l, c, r1, r2 = map(int, input().split())
        if ultimo_caso(l, c, r1 , r2): break
        if not check_limits([l, c, r1, r2]): break
        coube = False
        
        diam1 = 2 * r1
        diam2 = 2 * r2
        
        maior_diam = max(diam1, diam2)    
        menor_lado = min(l, c)

        dist_centros = dist_ponto2ponto(l, c, r1, r2)
        soma_raios = r1 + r2

        if (maior_diam <= menor_lado) and (dist_centros >= soma_raios):
            coube = True       

        if coube:
            print("S")
        else:
            print("N")
        
        