import string

class JefferCipher:
    def __init__(self):
        self.characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + " " + string.punctuation
        self.char_count = len(self.characters)

    def shift_character(self, char, shift):
        if char in self.characters:
            index = self.characters.index(char)
            shifted_index = (index + shift) % self.char_count
            return self.characters[shifted_index]
        return char

    def cipher(self, message, key):
        key_digits = [int(digit) for digit in str(key)]
        ciphered_message = []
        key_length = len(key_digits)

        for i, char in enumerate(message):
            shift = key_digits[i % key_length]
            ciphered_char = self.shift_character(char, shift)
            ciphered_message.append(ciphered_char)

        return ''.join(ciphered_message)

    def decipher(self, message, key):
        key_digits = [int(digit) for digit in str(key)]
        deciphered_message = []
        key_length = len(key_digits)

        for i, char in enumerate(message):
            shift = key_digits[i % key_length]
            deciphered_char = self.shift_character(char, -shift)
            deciphered_message.append(deciphered_char)

        return ''.join(deciphered_message)

if __name__ == "__main__":
    cipher = JefferCipher()

    while True:
            print("\nMenu:")
            print("1. Criptografar")
            print("2. Descriptografar")
            print("3. Imprimir alfabeto")
            print("4. Sair")

            choice = input("Escolha uma opção: ")

            if choice == "1":
                message = input("Digite a mensagem a ser criptografada: ")
                key = int(input("Digite a chave: "))
                ciphered = cipher.cipher(message, key)
                print("Ciphertext:", ciphered)

            elif choice == "2":
                message = input("Digite a mensagem a ser descriptografada: ")
                key = int(input("Digite a chave: "))
                deciphered = cipher.decipher(message, key)
                print("Deciphered:", deciphered)

            elif choice == "3":
                print("Alfabeto:", cipher.characters)

            elif choice == "4":
                print("Saindo do programa.")
                break

            else:
                print("Opção inválida. Tente novamente.")