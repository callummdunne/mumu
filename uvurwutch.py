import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
word = ""
while word != "-1":
	word = input("Gib word: ")
	speak.Speak(word)

	newword= ""
	for i in word: 
		if i in "AaEeIiOoUu":
			i = "oo"
		newword += i

	print(newword)

	speak.Speak(newword)