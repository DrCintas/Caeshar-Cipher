"""
Caeshar Cipher:
It is a cipher type where each letter in the plaintext is shifted by a number of places down the alphabet
"""

def encryption(text, shift):
	cipher = ""
	s = int(shift)
	for i in range(len(text)):
		char = text[i]
		if (ord(char) == 32):
			cipher += char
		elif (char.isupper()):
			cipher += chr((ord(char) + s-65) % 26 + 65)
		else:
			cipher += chr((ord(char) + s-97) % 26 + 97)
	return cipher

def decryption(text, shift):
	plain = ""
	s = int(shift)
	for i in range(len(text)):
		char = text[i]
		if (ord(char) == 32):
			plain += char
		elif (char.isupper()):
			plain += chr((ord(char) - s-65) % 26 + 65)
		else:
			plain += chr((ord(char) - s-97) % 26 + 97)
	return plain

text = input("Enter a string to encrypt/decrypt: \n")
option = input("Do you want to Encrypt or Decrypt? Please answer E or D: \n")
shift = input("How many times do you want the text shifted? (From 1 to 26) \n")
if ((option == "E") and (text) and (int(shift)>0) and (int(shift)<27)):
	print("\nThis is your text encrypted: ", encryption(text, shift))
elif ((option == "D") and (text) and (int(shift)>0) and (int(shift)<27)):
	print("\nThis is your text encrypted: ", decryption(text,shift))
else:
	print("Something went wrong, try again.")
