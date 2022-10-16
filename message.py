import cryptocode


class Code:
    def __init__(self, message, cryptography):
        self.message = message
        self.key = "2196387120638721"
        self.cryptography = cryptography

    def encrypt(self):
        return cryptocode.encrypt(self.message, self.key)

    def decrypt(self):
        return cryptocode.decrypt(self.cryptography, self.key)
