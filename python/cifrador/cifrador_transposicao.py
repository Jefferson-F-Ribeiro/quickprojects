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