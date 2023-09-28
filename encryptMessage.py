def encrypt_message(message,cipherKey,alphabet):
    encryped_message = ""
    uppercase_message = ""
    uppercase_message = message.upper()
    #positions of letters in alphabets
    for current_char in uppercase_message:
        position  = alphabet.find(current_char)
        new_position = position + int(cipherKey)

        if current_char in alphabet:
            encryped_message = encryped_message + alphabet[new_position]
        else:
            encryped_message = encryped_message + current_char
    return encryped_message