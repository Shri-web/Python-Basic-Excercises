def encrypt(text,val):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + val-65) % 26 + 65)

        else:
            result += chr((ord(char) + val - 97) % 26 + 97)

    return result

text = input()
val = int(input())

print(encrypt(text,val))
