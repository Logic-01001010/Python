def MakingCodeBook():
    decbook={'5':'a', '2':'b', '#':'d', '8':'e', '1':'f', '3':'g', '4':'h', '6':'i', '0':'l', '9':'m', '*':'n',
         '%':'o', '=':'p', '(':'r', ')':'s', ';':'t', '?':'u', '@':'v', ':':'y', '7':' '} # Decryption
    encbook={} # Encryption

    for k in decbook:
        value = decbook[k]
        encbook[value]=k

    return decbook, encbook

def MakingEncrypt(msg, Encbook):
    for c in msg:
        if c in Encbook:
            msg = msg.replace(c, Encbook[c])
    return msg

def MakingDecrypt(msg, Decbook):
    for c in msg:
        if c in Decbook:
            msg = msg.replace(c, Decbook[c])
    return msg


if __name__ == '__main__':

    Dec, Enc = MakingCodeBook()

    print("1. Encrypt Text")
    print("2. Decrypt Text")

    choice = input("$> ")

    if choice == '1':
        msg = input("$> ")
        print(MakingDecrypt(msg, Enc))

    elif choice == '2':
        msg = input("$> ")
        print(MakingDecrypt(msg, Dec))