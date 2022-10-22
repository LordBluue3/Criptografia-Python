from datetime import date

class Code:
    def __init__(self, message, cryptography):
        self.message = message
        self.cryptography = cryptography
        date_now = date.today()
        day = date_now.day
        self.key = day

    def encrypt(self):

        ascii_list = []
        code_cript = []
        for letter in self.message:

            for ascii in range(32, 129):

                # printo todos os caracteres da tabela ASCII
                print(str(ascii) + " - " + chr(ascii))
                # se a letra da tabela ascii for igual ao caracter da mensagem faça
                if(chr(ascii) == letter):
                    #crip recebe cripot + o numero da tabela ascii que representa esse caracter
                    ascii_list.append(str(ascii))

        for number in ascii_list:
            # criptografando cada numero da lista de ascii
            code_cript.append(((int(number) - 32) + self.key) % 94)
        print("Lista de Ascii:", ascii_list)
        # retornando a mensagem criptografada
        return code_cript

    def decrypt(self):
        chars = '[],'
        #limpando os caracteres acima do self.cryptography
        clean = self.cryptography.translate(str.maketrans('', '', chars))
        #transformando os itens do crypytography em uma lista
        cryptography_list = clean.split()

        ascii_descriptt = []
        decrypted_message = ""

        for letter in cryptography_list:
            #descriptografando cada grupo de numeros da lista de criptografia e inserindo em uma lista
            ascii_descriptt.append((((int(letter) + 94 - self.key) % 94) + 32))

        for ascii in ascii_descriptt:
            #Concatenando cada letra da tabela ascii para formar uma palavra ou frase
            decrypted_message = decrypted_message + chr(ascii)

        print(cryptography_list)
        print(ascii_descriptt)

        print(decrypted_message)
        #retornando a mensagem descriptografada
        return decrypted_message
