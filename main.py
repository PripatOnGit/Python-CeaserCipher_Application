from getDoubleAlphabets import getDoubleAlphabet
import getMessage
import getCipherKey
import encryptMessage
import decryptionMessage

def runCeaserCipher():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f"Alphabet: {myAlphabet}")

    #double the alphabet string using getDoubleAlphabet()
    new_alphabet = getDoubleAlphabet(myAlphabet)
    print(f"New_alphabet: {new_alphabet}")

    #get message using getMessage()
    message = getMessage.getMessage()
    print(f"Message to encrypt: {message}")

    #get cipher key between 1-25
    cipherKey = getCipherKey.cipherKey()
    print(f"Cipher Key: {cipherKey}")

    #encrypt the message
    myEncryptedMessage  = encryptMessage.encrypt_message(message, cipherKey, new_alphabet)
    print(myEncryptedMessage)

    myDecryptedMessage = decryptionMessage.decrypted_message(message,cipherKey,myAlphabet)
    print(myDecryptedMessage)


if __name__ == '__main__':
    runCeaserCipher()
else:
    print("file is imported")