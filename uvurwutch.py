import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
word = ""
string = input("what do you want the vowels to be replaced with?")
while word != "-1":
	word = input("Gib word: ")
	speak.Speak(word)

	newword= ""
	for i in word: 
		if i in "AaEeIiOoUu":
			i = string
		newword += i

	print(newword)

	speak.Speak(newword)