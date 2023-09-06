def gerar_chave():
    # Gere uma chave simples (deve ter o mesmo comprimento que o texto)
    chave = "minhachave"
    return chave

def cifrar(texto, chave):
    texto_cifrado = ""
    for i in range(len(texto)):
        char_original = texto[i]
        char_chave = chave[i % len(chave)]  # Repetir a chave se for mais curta que o texto
        resultado = ord(char_original) ^ ord(char_chave)  # Operação XOR
        texto_cifrado += chr(resultado)
    return texto_cifrado

def decifrar(texto_cifrado, chave):
    texto_decifrado = ""
    for i in range(len(texto_cifrado)):
        char_cifrado = texto_cifrado[i]
        char_chave = chave[i % len(chave)]  # Repetir a chave se for mais curta que o texto
        resultado = ord(char_cifrado) ^ ord(char_chave)  # Operação XOR
        texto_decifrado += chr(resultado)
    return texto_decifrado

def main():
    print("Cifrador XOR (ou exclusivo)")

    chave = gerar_chave()
    print("Chave gerada:", chave)

    texto_original = input("Digite o texto a ser cifrado: ")

    texto_cifrado = cifrar(texto_original, chave)
    print("Texto cifrado:", texto_cifrado)

    texto_decifrado = decifrar(texto_cifrado, chave)
    print("Texto decifrado:", texto_decifrado)

if __name__ == "__main__":
    main()