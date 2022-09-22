"""



"""



def main():
	DecodeWord()





#Your code goes here.
def DecodeWord():
	# encodedWord = "WBLARF8TTS"
	# encodedWord = "L8KAOUL"
	# encodedWord = "E8N8N8"
	# encodedWord = "8TRA8DY T8LA"
	# encodedWord = "8TT LHA TILLTA LIMAS"	
	# encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	# encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	# encodedWord = "UUHO"  		#Used for Bonus
	# encodedWord = "EOUUUUOUU" 	#Used for Bonus
	decodedWord = ""
	
	for letter in encodedWord:
		newLetter = ""
		if letter == 'T':
			newLetter = 'L'
			decodedWord += newLetter
		elif letter == 'L':
			newLetter = 'T'
			decodedWord += newLetter
		elif letter == '8':
			newLetter = 'A'
			decodedWord += newLetter
		elif letter == 'B':
			newLetter = 'A'
			decodedWord += newLetter
		elif letter == 'A':
			newLetter = 'E'
			decodedWord += newLetter
		elif letter == 'E':
			newLetter = 'B'
			decodedWord += newLetter
		else:
			decodedWord += letter
	print(decodedWord)









#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
