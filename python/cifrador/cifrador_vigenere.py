def cifrar_vigenere(texto, chave):
    texto_cifrado = ""
    chave = chave.upper()
    index = 0

    for char in texto:
        if char.isalpha():
            if char.islower():
                novo_char = chr(((ord(char) - ord('a') + (ord(chave[index % len(chave)]) - ord('A'))) % 26) + ord('a'))
            else:
                novo_char = chr(((ord(char) - ord('A') + (ord(chave[index % len(chave)]) - ord('A'))) % 26) + ord('A'))
            index += 1
        else:
            novo_char = char
        texto_cifrado += novo_char

    return texto_cifrado

def decifrar_vigenere(texto_cifrado, chave):
    texto_decifrado = ""
    chave = chave.upper()
    index = 0

    for char in texto_cifrado:
        if char.isalpha():
            if char.islower():
                novo_char = chr(((ord(char) - ord('a') - (ord(chave[index % len(chave)]) - ord('A'))) % 26) + ord('a'))
            else:
                novo_char = chr(((ord(char) - ord('A') - (ord(chave[index % len(chave)]) - ord('A'))) % 26) + ord('A'))
            index += 1
        else:
            novo_char = char
        texto_decifrado += novo_char

    return texto_decifrado

def main():
    print("Cifrador de Vigenère")

    chave = input("Digite a chave (somente caracteres alfabéticos): ").upper()
    texto_original = input("Digite o texto a ser cifrado: ")

    texto_cifrado = cifrar_vigenere(texto_original, chave)
    texto_decifrado = decifrar_vigenere(texto_cifrado, chave)

    print("Texto cifrado:", texto_cifrado)
    print("Texto decifrado:", texto_decifrado)

if __name__ == "__main__":
    main()