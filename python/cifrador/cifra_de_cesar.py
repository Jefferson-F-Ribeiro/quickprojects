def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    
    for char in texto:
        if char.isalpha():
            if char.isupper():
                ascii_offset = ord('A')
            else:
                ascii_offset = ord('a')

            novo_char = chr((ord(char) - ascii_offset + deslocamento) % 26 + ascii_offset)
            resultado += novo_char
        else:
            resultado += char
    
    return resultado

def decifra_cesar(texto_cifrado, deslocamento):
    return cifra_de_cesar(texto_cifrado, -deslocamento)

def main():
    print("Bem-vindo à Cifra de César!")
    texto_original = input("Digite o texto a ser cifrado: ")
    deslocamento = int(input("Digite o valor de deslocamento (chave): "))
    
    texto_cifrado = cifra_de_cesar(texto_original, deslocamento)
    texto_decifrado = decifra_cesar(texto_cifrado, deslocamento)
    
    print("\nTexto cifrado:", texto_cifrado)
    print("Texto decifrado:", texto_decifrado)

if __name__ == "__main__":
    main()