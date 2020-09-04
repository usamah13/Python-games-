import string

def encrypt(word_to_encrypt,key):
	allAlphabets = string.ascii_uppercase
	#print(allAlphabets)
	encryptedAlphabets = allAlphabets[key:] + allAlphabets[:key]
	#print(encryptedAlphabets)
	encryptedMappings = str.maketrans(allAlphabets, encryptedAlphabets)
	print(encryptedMappings)
	return word_to_encrypt.translate(encryptedMappings)

def decrypt(word_to_decrypt,key):
	allAlphabets = string.ascii_uppercase
	key = key * -1
	encryptedAlphabets = allAlphabets[key:] + allAlphabets[:key]
	encryptedMappings = str.maketrans(allAlphabets, encryptedAlphabets)
	return word_to_decrypt.translate(encryptedMappings)


def main():
	print("Welcome to Encryption Decryption Program")
	loop = "Y"
	while loop != "N" and loop != "n":
		userInput = input("Enter mode,code,key separated by commas>")
		mode = userInput.split(",")[0]
		code = userInput.split(",")[1]
		key = userInput.split(",")[2]

		if mode == "d":
			print(decrypt(code,int(key)))
		elif mode == "e":
			print(encrypt(code,int(key)))
		else:
			print("Wrong mode")
		loop = input("Do you wish to continue Y/N>")


main()