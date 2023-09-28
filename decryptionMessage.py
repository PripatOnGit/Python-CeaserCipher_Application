def decrypted_message(str,cipherKey,alphabet):
    decrypted_message = ''
    for ch in str:
        position = alphabet.find(ch)
        new_postion = position - cipherKey
        if ch in alphabet:
            decrypted_message = decrypted_message + alphabet[new_postion]
        else:
            decrypted_message = decrypted_message + ch
    return decrypted_message