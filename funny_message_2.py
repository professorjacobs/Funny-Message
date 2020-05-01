prompt = "\nHey There! Type in a message and I'll Repeat it back to you!"
prompt += "\nEnter 'quit' to leave the program.  \n"

active = True
while active:
		message = input(prompt)

		if message == 'quit':
			print("You think you can escape? nah you're in this for life")
		elif message == 'Quit':
			print("Fancy guy huh? Usin capital letters. You can't escape.")
		elif message == 'QUIT':
			print("You think getting angry is gonna help?")
		else:
			print("\nWhat? You think I work for you? Get outta here I ain't sayin' that")

		add_active = input("\nWould you like to try again? (yes/no)") 
		if add_active = 'please let me out of this thing'
			break