def encryption(b,f):
    cipher = ""
    print(b)
    for i in b:
        if i.isalpha():
            Alphabet = ord(i) + f
            if Alphabet > ord("z"):
                Alphabet -= 26
        Letter = chr(Alphabet)
        cipher += Letter
    print(cipher)

    p = input("would you like to do another (yes or no): ")

    if p == "yes":
        main()
    elif p == "no":
        exit()
        
        
            
        
def decryption(c,g):
    decryptiontext = ""

    for i in c:
        if i.isalpha():
            Alphabet = ord(i) - g
            if Alphabet <ord("Z"):
                Alphabet += 26
        Letter = chr(Alphabet)
        decryptiontext += Letter
    print(decryptiontext)

    p = input("would you like to do another (yes or no): ")
    
    if p == "yes":
        main()
    elif p == "no":
        exit()

def main():
    a = input("would to like to [e]ncrypt or [d]ecrypt: ")
    e = input("enter plain text: ")
    d = int(input("please enter a shift number : "))
    encrypt = "encrypt"
    decrypt = "decrypt"
    if (a == "e"):
    	
    	encryption(e,d)
        
    elif (a == "d"):
    	
     	decryption(e,d)
main()