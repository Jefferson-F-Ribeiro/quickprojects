def cifrar(texto, chave):
    texto_cifrado = ""
    for i in range(len(texto)):
        char_original = texto[i]
        char_chave = chave[i % len(chave)]
        resultado = ord(char_original) ^ ord(char_chave)
        texto_cifrado += chr(resultado + 32)
    return texto_cifrado

def decifrar(texto_cifrado, chave):
    texto_decifrado = ""
    for i in range(len(texto_cifrado)):
        char_cifrado = texto_cifrado[i]
        char_chave = chave[i % len(chave)]
        resultado = (ord(char_cifrado) - 32) ^ ord(char_chave)
        texto_decifrado += chr(resultado)
    return texto_decifrado

def main():
    print("Cifrador XOR (ou exclusivo)")

    chave = input("Digite a chave (somente caracteres imprimíveis): ")
    texto_original = input("Digite o texto a ser cifrado (somente caracteres imprimíveis): ")

    texto_original = ''.join(filter(lambda x: 32 <= ord(x) <= 126, texto_original))

    chave = chave * (len(texto_original) // len(chave)) + chave[:len(texto_original) % len(chave)]

    texto_cifrado = cifrar(texto_original, chave)
    texto_decifrado = decifrar(texto_cifrado, chave)

    print("Texto cifrado:", texto_cifrado)
    print("Texto decifrado:", texto_decifrado)

if __name__ == "__main__":
    main()