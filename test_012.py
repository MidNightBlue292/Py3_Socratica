def leitura(x, y):
    try:
        c = 0
        while c < len(x):
            print(x[c], y[c])
            c += 1
    except:
        pass
    finally:
        print(f'Tem {c} letras')
    return c


letras_p = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
letras_g = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

quant = leitura(letras_p, letras_g)
