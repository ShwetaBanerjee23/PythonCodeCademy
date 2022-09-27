import random

"""
Caesar cipher - encrypts + decrypts messages.
"""


def encrypt(text, n):
    """
    This function encrypts the text by shifting letters
    by a value of n.

    :param text: The text to encrypt.
    :param n: The value to shift each letter by.
    :return: The encrypted text.
    """
    res = ""

    for letter in text:
        encrypted = (ord(letter) - 97 + n) % 26 + 97
        res += (chr(encrypted))

    return res


def decrypt(text, n):
    """
    This function decrypts the text by shifting letters
    back by a value of n.

    :param text: The text to decrypt.
    :param n: The value to shift each letter back by.
    :return: The decrypted text.
    """
    res = ""

    for letter in text:
        decrypted = (ord(letter) - 97 - n) % 26 + 97
        res += (chr(decrypted))

    return res


class Cipher:
    def __init__(self):
        """
        A password is required for a person to decrypt
        this message.
        """
        password = ""
        allowedChars = "abcdefghijklmnopqrstuvwxyz" \
                       "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                       "1234567890" \
                       "!@£$%^&*()_+{}[]:;,.<>/?`~-"

        # Generate a 18 character long password with random characters
        while len(password) < 18:
            rnd = random.randint(0, len(allowedChars) - 1)
            password += allowedChars[rnd]
        self.__password = password

    def main(self):
        stop = ""
        while not stop == "yes":
            # Encrypt or decrypt
            option = ""
            while option.lower() != "encrypt" and option.lower() != "decrypt":
                option = input("Encrypt or decrypt? ")

            # Message to encrypt/decrypt
            text = "123"
            while not text.isalpha():
                print("Can only encode text containing letters.")
                text = input("Message: ")

            # Value to shift the letters by - 0 returns the original text
            n = 26
            while n < 0 or n > 25:
                n = int(input("Encryption value (must be between 0 and 25): "))

            # Encrypt message
            if option.lower() == "encrypt":
                encryptedMessage = encrypt(text, n)
                print("Encrypted message: " + encryptedMessage)
                print("To decrypt this message, a password will be required.\n"
                      "\tYour password is: " + self.__password)

            # Decrypt message
            elif option.lower() == "decrypt":
                cnt = 0
                password = ""

                # 3 tries to get password correct
                while password != self.__password and cnt < 3:
                    print("You have " + str(cnt) + " tries remaining for getting "
                                                   "the password right. After this, "
                                                   "the message will be deleted.")
                    password = input("Password: ")
                    cnt += 1

                # Password incorrect 3 times - delete instance
                if cnt == 3:
                    print("Incorrect password three times. Message deleted.")
                    exit()

                decryptedMessage = decrypt(text, n)
                print("Decrypted message: " + decryptedMessage)

            stop = input("Have you finished encryption and decryption? "
                         "\n\t(typing \"yes\" will delete any encrypted "
                         "messages) ")


if __name__ == "__main__":
    c = Cipher()
    c.main()
