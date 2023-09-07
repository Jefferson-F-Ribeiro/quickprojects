def cifrar(texto, chave):
    texto_cifrado = ""
    for i in range(len(texto)):
        char_original = texto[i]
        char_chave = chave[i % len(chave)]  # Repetir a chave se for mais curta que o texto
        resultado = ord(char_original) ^ ord(char_chave)  # Operação XOR
        texto_cifrado += chr(resultado + 32)  # Adicionar 32 para garantir que o resultado seja imprimível
    return texto_cifrado

def decifrar(texto_cifrado, chave):
    texto_decifrado = ""
    for i in range(len(texto_cifrado)):
        char_cifrado = texto_cifrado[i]
        char_chave = chave[i % len(chave)]  # Repetir a chave se for mais curta que o texto cifrado
        resultado = (ord(char_cifrado) - 32) ^ ord(char_chave)  # Subtrair 32 para desfazer a adição na cifragem
        texto_decifrado += chr(resultado)
    return texto_decifrado

def main():
    print("Cifrador XOR (ou exclusivo)")

    chave = "chave123"  # Certifique-se de que a chave consista em caracteres imprimíveis
    print("Chave gerada:", chave)

    texto_original = input("Digite o texto a ser cifrado (somente caracteres imprimíveis): ")

    # Remova caracteres que não sejam imprimíveis
    texto_original = ''.join(filter(lambda x: 32 <= ord(x) <= 126, texto_original))

    # Ajuste o tamanho da chave para corresponder ao texto original
    chave = chave * (len(texto_original) // len(chave)) + chave[:len(texto_original) % len(chave)]

    texto_cifrado = cifrar(texto_original, chave)
    texto_decifrado = decifrar(texto_cifrado, chave)

    print("Texto cifrado:", texto_cifrado)
    print("Texto decifrado:", texto_decifrado)

if __name__ == "__main__":
    main()
