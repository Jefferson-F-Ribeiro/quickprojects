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

texto_original = "Testando o cifrador"
deslocamento = 3
texto_cifrado = cifra_de_cesar(texto_original, deslocamento)
print("Texto original:", texto_original)
print("Texto cifrado:", texto_cifrado)