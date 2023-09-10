def criar_tabela_substituicao(chave):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tabela_substituicao = {}

    chave = chave.upper()
    chave = ''.join(sorted(set(chave), key=chave.index))  # Remove letras duplicadas e mantém a ordem

    for i in range(len(alfabeto)):
        if i < len(chave):
            tabela_substituicao[alfabeto[i]] = chave[i]
        else:
            letras_nao_utilizadas = [letra for letra in alfabeto if letra not in tabela_substituicao.values()]
            tabela_substituicao[alfabeto[i]] = letras_nao_utilizadas[0]

    return tabela_substituicao

def cifrar_substituicao(texto, chave):
    tabela_substituicao = criar_tabela_substituicao(chave)
    texto_cifrado = ""

    for char in texto:
        if char.isalpha():
            if char.islower():
                novo_char = tabela_substituicao[char.upper()].lower()
            else:
                novo_char = tabela_substituicao[char]
        else:
            novo_char = char
        texto_cifrado += novo_char

    return texto_cifrado

def decifrar_substituicao(texto_cifrado, chave):
    tabela_substituicao = criar_tabela_substituicao(chave)
    tabela_decifrar = {valor: chave for chave, valor in tabela_substituicao.items()}
    texto_decifrado = ""

    for char in texto_cifrado:
        if char.isalpha():
            if char.islower():
                novo_char = tabela_decifrar[char.upper()].lower()
            else:
                novo_char = tabela_decifrar[char]
        else:
            novo_char = char
        texto_decifrado += novo_char

    return texto_decifrado

def main():
    print("Cifrador de Substituição Monoalfabética")

    chave = input("Digite a chave (uma permutação de letras do alfabeto): ").upper()
    texto_original = input("Digite o texto a ser cifrado: ")

    texto_cifrado = cifrar_substituicao(texto_original, chave)
    texto_decifrado = decifrar_substituicao(texto_cifrado, chave)

    print("Texto cifrado:", texto_cifrado)
    print("Texto decifrado:", texto_decifrado)

if __name__ == "__main__":
    main()
