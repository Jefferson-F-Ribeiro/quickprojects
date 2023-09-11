def cifrar_transposicao(texto, chave):
    num_colunas = len(chave)
    num_linhas = len(texto) // num_colunas + int(len(texto) % num_colunas != 0)

    matriz = [[' ' for _ in range(num_colunas)] for _ in range(num_linhas)]

    index = 0
    for i in range(num_linhas):
        for j in range(num_colunas):
            if index < len(texto):
                matriz[i][j] = texto[index]
                index += 1

    texto_cifrado = ""
    for coluna in chave:
        coluna_idx = int(coluna) - 1
        for linha in range(num_linhas):
            texto_cifrado += matriz[linha][coluna_idx]

    return texto_cifrado

def decifrar_transposicao(texto_cifrado, chave):
    num_colunas = len(chave)
    num_linhas = len(texto_cifrado) // num_colunas + int(len(texto_cifrado) % num_colunas != 0)

    coluna_len = [len(texto_cifrado) // num_colunas] * num_colunas
    for i in range(len(texto_cifrado) % num_colunas):
        coluna_len[i] += 1

    matriz = [[' ' for _ in range(num_colunas)] for _ in range(num_linhas)]

    index = 0
    for coluna in chave:
        coluna_idx = int(coluna) - 1
        for linha in range(num_linhas):
            if index < len(texto_cifrado):
                matriz[linha][coluna_idx] = texto_cifrado[index]
                index += 1

    texto_decifrado = ""
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            texto_decifrado += matriz[linha][coluna]

    return texto_decifrado

def main():
    print("Cifrador de Transposição")

    chave = input("Digite a chave de permutação (por exemplo, '2314'): ")
    texto_original = input("Digite o texto a ser cifrado: ")

    texto_cifrado = cifrar_transposicao(texto_original, chave)
    texto_decifrado = decifrar_transposicao(texto_cifrado, chave)

    print("Texto cifrado:", texto_cifrado)
    print("Texto decifrado:", texto_decifrado)

if __name__ == "__main__":
    main()