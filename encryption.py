def encryption(b,f):
    cipher = ""
    for i in b:
        if i.isalpha():
            Alphabet = ord(i) + f
            if Alphabet > ord("z"):
                Alphabet -= 26
        Letter = chr(Alphabet)
        cipher += Letter
    final_enc(cipher)
        
            
        
def decryption(c,g):
    decryptiontext = ""

    for i in c:
        if i.isalpha():
            Alphabet = ord(i) - g
            if Alphabet <ord("Z"):
                Alphabet += 26
        Letter = chr(Alphabet)
        decryptiontext += Letter
    final_dec(decryptiontext)

    
        
def topfile_enc(cyrpto_string):
	temp=cyrpto_string
	final_str=[]
	for i in range(len(cyrpto_string)):
	    l=temp[-1]
	    l=int(l)+104
	    final_str.append(chr(l))
	    temp=temp[:-1]
	encryption(final_str,5)
	
def topfile_dec(cyrpto_string):
	temp=cyrpto_string
	final_str=[]
	for i in range(int(len(cyrpto_string)/2)):
		d=temp[-2:]
		j=int(d)+27
		final_str.append(chr(j))
		temp=temp[:-2]
	decryption(final_str,5)
	
	
def final_enc(cyrpto_string):
	temp=cyrpto_string
	final_str=[]
	for i in range(len(cyrpto_string)):
		d=temp[-1]
		final_str.append(ord(d)-27)
		temp=temp[:-1]
	print("".join(str(x) for x in final_str))
	

		
		
def final_dec(cyrpto_string):
	temp=cyrpto_string
	final_str=[]
	for i in range(len(cyrpto_string)):
		d=temp[-1]
		j=ord(d)-104
		final_str.append(j)
		temp=temp[:-1]
	print("".join(str(x) for x in final_str))

def main():
    a = input("would to like to [e]ncrypt or [d]ecrypt: ")
    e = input("enter plain text: ")
    encrypt = "encrypt"
    decrypt = "decrypt"
    if (a == "e"):
    	    topfile_enc(e)
        
    elif (a == "d"):
    		topfile_dec(e)
  
main()