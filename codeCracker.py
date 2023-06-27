def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = ord(char) + shift
            if char.islower():
                if shifted_char > ord("z"):
                    shifted_char -= 26
                result += chr(shifted_char)
            elif char.isupper():
                if shifted_char > ord("Z"):
                    shifted_char -= 26
                result += chr(shifted_char)
        else:
            result += char
    return result


text = input("Digite o texto a ser decifrado: ")
shift = int(input("Digite o deslocamento: "))

print(caesar_cipher(text, shift))
