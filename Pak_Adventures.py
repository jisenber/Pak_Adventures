from sys import exit
medals = []
rooms = ["peanut_butter_room", "snorlax_room", "oil_room", "garlic_room", "chocolate_room"]

def lobby():
	print "\nYou are in the lobby, and you have the following medals:"
	for y in medals:
		print y
	print "\nchoose a room where you have not acquired a medal."
	for i, x in enumerate(rooms):
		print '\t(' + str(i+1) + ') ' + x
	print "\npick which room you'd like to enter (type in the name of the room)"
	choice = raw_input("> ")
	if choice == "peanut" or choice == "peanut butter" or choice == "peanut_butter_room" or choice == "peanut room":
		peanut_butter_room()
	elif choice == "snorlax" or choice == "snorlax_room" or choice == "snorlax room":
		snorlax_room()
	elif choice == "oil" or choice == "oil_room" or choice == "oil room":
		oil_room()
	elif choice == "garlic" or choice == "garlic_room" or choice == "garlic room":
		garlic_room()
	elif (choice == "chocolate" or choice == "chocolate room" or choice == "chocolate_room") and rooms == ["chocolate_room"]:
		print "\nYou paid enough with your medals (and life savings) to enter to coveted chocolate room!"
		chocolate_room()
	elif (choice == "chocolate" or choice == "chocolate room" or choice == "chocolate_room")  and rooms != ["chocolate_room"]:
		print "\nYour poor ass still can't afford this primo chocolate. Get some more medals and come back"
		re_lobby()
	else:
		print "\nsorry, I don't understand that answer, try again"
		re_lobby()
	return medals
	return rooms

def re_lobby():
	print "\nchoose a room where you have not acquired a medal."
	for i, x in enumerate(rooms):
		print '\t(' + str(i+1) + ') ' + x
	print "\npick which room you'd like to enter (type in the name of the room)"
	choice = raw_input("> ")
	if choice == "peanut" or choice == "peanut butter" or choice == "peanut_butter_room" or choice == "peanut room":
		peanut_butter_room()
	elif choice == "snorlax" or choice == "snorlax_room" or choice == "snorlax room":
		snorlax_room()
	elif choice == "oil" or choice == "oil_room" or choice == "oil room":
		oil_room()
	elif choice == "garlic" or choice == "garlic_room" or choice == "garlic room":
		garlic_room()
	elif (choice == "chocolate" or choice == "chocolate room" or choice == "chocolate_room") and rooms == ["chocolate_room"]:
		print "\nYou paid enough with your medals (and life savings) to enter to coveted chocolate room!"
		chocolate_room()
	elif (choice == "chocolate" or choice == "chocolate room" or choice == "chocolate_room")  and rooms != ["chocolate_room"]:
		print "\nYour poor ass still can't afford this primo chocolate. Get some more medals and come back"
	else:
		print "\nsorry, I don't understand that answer, start in the lobby again"
		lobby()
	return medals
	return rooms

def garlic_room():
	print """
	you have entered the garlic room! There is garlic everywhere.
	you see a medal, but the garlic looks so delicious... you have
	two options of what you can do:
	\t(1) eat garlic
	\t(2) take medal"""
	choice = raw_input("> ")
	if choice == "eat" or choice == "garlic" or choice == "eat garlic" or choice == "1":
		print """nomnomnom.. as you eat, the room starts to smell.. keep eating?
		\t(1) yes, the garlic is too delicious!
		\t(2) no"""
		choice2 = raw_input("> ")
		if choice2 == "1" or choice2 == "yes" or choice2 == "yes, the garlic is too delicious!":
			death("Game over. the smell was overpowering and you perished.")
		elif choice2 == "2" or choice2 == "no":
			print """Wise decision. You escaped the smelly room and snagged the medal on your way out!
			Press ENTER to return to the lobby"""
			medals.append("garlic_medal")
			rooms.remove('garlic_room')
			print "you now have acquired the following medals: %s" % medals
			raw_input("> ")
			lobby()
		else:
			print "Sorry I don't understand. Press enter to return to the beginning of the garlic room"
			raw_input("> ")
			garlic_room()
	elif choice == "2" or choice == "no":
		print """Wise decision. You escaped the smelly room and snagged the medal on your way out!
        Press ENTER to return to the lobby"""
		medals.append("garlic_medal")
		rooms.remove('garlic_room')
		print "you now have acquired the following medals: %s" % medals
		raw_input("> ")
		lobby()
	else:
		print "Sorry I don't understand. Press enter to return to the beginning of the garlic room"
		raw_input("> ")
		garlic_room()
	return medals
	return rooms

def oil_room():
	print "\nYou have entered what seems to be an empty room, but then a Texas oil baron approaches"
	print "\ntalk to the Texan?"
	print "1) yes"
	print "2) no"
	choice = raw_input("> ")
	if choice == "yes" or choice == "1":
		print """
		\nThe Texan says: \n\n\t\t\t"sonny boy, I gots a business proposition for ya.
		This room of yours is on a rich natural oil deposit, and it needs to be extracted
		but to do this you need to pick the right tool. please help me choose which tool to use
		and I'll give you a medal for your work\""""
		print "\n press ENTER to help the Texan"
		raw_input("> ")
		print"""
		you have 3 tools:
		1) straw
		2) shovel
		3) rig"""
		print "which tool do you use?"
		choice2 = raw_input("> ")
		if choice2 == "1" or choice2 == "straw" or choice2 == "axe" or choice2 == "pick":
			print """ the Texan said: \n \"A straw? to extract oil? you must not be from oil country sonny
            come back when you have a better idea\""""

			print "press ENTER to return to the lobby"
			raw_input("> ")
			re_lobby()
		elif choice2 == "2" or choice2 == "shovel":
			print"""
			The Texan said: \n\"a shovel will not work to extract a liquid substance. The oil fumes
            must have gotten to your head! come back when you have a better idea\""""

			print "press ENTER to return to the lobby"
			raw_input("> ")
			re_lobby()
		elif choice2 == "3" or choice2 == "rig":
			print """
			YeeHAW!! Look at all that oil! Great job! here is your medal.
			I'm going to go smoke a cigarette."""
			medals.append("oil_medal")
			rooms.remove('oil_room')
			print "you now have acquired the following medals: %s" % medals
			print "\nPress ENTER to return to the lobby"
			raw_input("> ")
			lobby()
		else:
			print "\nsorry, I don't understand that. Try picking a tool again"
			re_oil_room()
	elif choice == "2" or choice == "no":
		print "okay. You stand awkwardly and shuffle back to the lobby"
		print "\nPress ENTER to return to the lobby"
		raw_input("> ")
		re_lobby()
	else:
		print "You said some stuff that made no sense and then retreated to the lobby"
		print "Press ENTER to return to the lobby"
		raw_input("> ")
		re_lobby()
	return medals
	return rooms

def re_oil_room():
	print"""
	you have 3 tools:
	1) straw
	2) shovel
	3) rig"""
	print "which tool do you use?"
	choice2 = raw_input("> ")
	if choice2 == "1" or choice2 == "straw":
		print """
		the Texan said: \n \"A straw? to extract oil? you must not be from oil country sonny
        come back when you have a better idea\""""

		print "press ENTER to return to the lobby"
		raw_input("> ")
		re_lobby()
	elif choice2 == "2" or choice2 == "shovel":
		print"""
		The Texan said: \n\"a shovel will not work to extract a liquid substance. The oil fumes
        must have gotten to your head! come back when you have a better idea\""""

		print "press ENTER to return to the lobby"
		raw_input("> ")
		re_lobby()
	elif choice2 == "3" or choice2 == "rig":
		print "YeeHAW!! Look at all that oil! you done a fine job! here is your medal"
		medals.append("oil_medal")
		rooms.remove('oil_room')
		print "you now have acquired the following medals: %s" % medals
		print "Press ENTER to return to the lobby"
		raw_input("> ")
		lobby()
	else:
		print "sorry, I don't understand that. Try picking a tool again"
		re_oil_room()
	return medals
	return rooms

def peanut_butter_room():
	print "\nyou have entered a room full of peanut butter!"
	print "you will have to dig your way to the medal. What tool should you use?"
	print "\n\t(1) spoon"
	print "\t(2) fork"
	print "\t(3) knife"
	choice = raw_input("> ")

	if choice == "1" or choice == "spoon":
		print "\npak never uses a spoon when sleepwalking. Try again"
		peanut_butter_room()
	elif choice == "3" or choice == "knife":
		print "\npak never uses a knife when sleepwalking. Try again"
		peanut_butter_room()
	elif choice == "2" or choice == "fork":
		print """
		\nPak is adept at using a fork while sleepwalking.
		\nYou obtained the medal you needed!\n"""
		medals.append("peanut medal")
		rooms.remove('peanut_butter_room')
		print "you now have acquired the following medals: %s" % medals
	else:
		print "that doesn't make sense to me. start again from the beginning of the room"
		peanut_butter_room()
	print "now you should go to the lobby. Press ENTER to go to the lobby"
	raw_input()
	lobby()
	return medals
	return rooms

def snorlax_room():
	print"""\n
	("\(-_-)/")
	(( ))
	((...) (...))"""
	print "\n A wild snorlax appeared in tall grass!"
	print"""
	\nWhat do you do?
	1) tackle
	2) hydro pump
	3) items
	4) escape!"""
	choice = raw_input("> ")
	if choice == "1" or choice == "tackle":
		print "It's not very effective!"
		re_snorlax()
	elif choice == "2" or choice == "hydro" or choice == "hydro pump" or choice == "pump":
		print "It's not very effective!"
		re_snorlax()
	elif choice == "4" or choice == "escape" or choice == "escape!":
		print "you escaped successfully!"
		re_lobby()
	elif choice == "items" or choice == "item" or choice == "3":
		print """
		\nwhich item do you choose"
		1) Great Ball
		2) Flute
		3) Potion
		4) Oak's Parcel"""
		choice2 = raw_input("> ")
		if choice2 == "Great Ball" or choice2 == "great ball" or choice2 == "1":
			print "\nWild Snorlax escaped!"
			re_snorlax()
		elif choice2 == "potion" or choice2 == "Potion" or choice2 == "3":
			print "\nNo Pak, potion won't do anything in this situation!"
			re_snorlax()
		elif choice2 == "Oak's Parcel" or choice2 == "oak's parcel" or choice2 == "oaks parcel" or choice2 == "4":
			print "\nCan't use item!"
			re_snorlax()
		elif choice2 == "Flute" or choice2 == "flute" or choice2 == "2":
			print "\nSnorlax is tossing and turning.. Press ENTER to keep playing your beautiful ballad"
			raw_input("> ")
			print """
			\nWild Snorlax got up and walked away, revealing a medal he was sleeping on!
			Press ENTER to take medal"""
			raw_input("> ")
			medals.append("snorlax_medal")
			rooms.remove("snorlax_room")
			print "you now have acquired the following medals: %s" % medals
			print "\npress ENTER to return to lobby"
			raw_input("> ")
			re_lobby()
		else:
			print "\nwhatever you just wrote has no effect on Wild Snorlax"
			re_snorlax()
	else:
		print "whatever you just wrote has no effect on Wild Snorlax"
		re_snorlax()
	return medals
	return rooms

def re_snorlax():
	print"""
	\nWhat do you do?
	1) tackle
	2) hydro pump
	3) items
	4) escape!"""
	choice = raw_input("> ")
	if choice == "1" or choice == "tackle":
		print "It's not very effective!"
		re_snorlax()
	elif choice == "2" or choice == "hydro" or choice == "hydro pump" or choice == "pump":
		print "It's not very effective!"
		re_snorlax()
	elif choice == "4" or choice == "escape" or choice == "escape!":
		print "you escaped successfully!"
		re_lobby()
	elif choice == "items" or choice == "item" or choice == "3":
		print """
		\nwhich item do you choose"
		1) Great Ball
		2) Flute
		3) Potion
		4) Oak's Parcel"""
		choice2 = raw_input("> ")
		if choice2 == "Great Ball" or choice2 == "great ball" or choice2 == "1":
			print "\nWild Snorlax escaped!"
			re_snorlax()
		elif choice2 == "potion" or choice2 == "Potion" or choice2 == "3":
			print "\nNo Pak, potion won't do anything in this situation!"
			re_snorlax()
		elif choice2 == "Oak's Parcel" or choice2 == "oak's parcel" or choice2 == "oaks parcel" or choice2 == "4":
			print "\nCan't use item!"
			re_snorlax()
		elif choice2 == "Flute" or choice2 == "flute" or choice2 == "2":
			print "\nSnorlax is tossing and turning.. Press ENTER to keep playing your beautiful ballad"
			raw_input("> ")
			print """
			\nWild Snorlax got up and walked away, revealing a medal he was sleeping on!
			Press ENTER to take medal"""
			raw_input("> ")
			medals.append("snorlax_medal")
			rooms.remove("snorlax_room")
			print "you now have acquired the following medals: %s" % medals
			print "\npress ENTER to return to lobby"
			raw_input("> ")
			re_lobby()
		else:
			print "\nwhatever you just wrote has no effect on Wild Snorlax"
			re_snorlax()
	else:
		print "\nwhatever you just wrote has no effect on Wild Snorlax"
		re_snorlax()
	return medals
	return rooms

def chocolate_room():
	print "\nCongratulations! you finally obtained enough medals to pay for the delicious chocolate"
	print "\nPress ENTER to eat some chocolate. Just one bite though. It's not like you need it."
	raw_input("> ")
	print "\nAhh... sweet refreshing chocolate. Pak is beginning to wake up! okay just one more bite.. Press ENTER"
	raw_input("> ")
	print "\n That's the stuff! Pak is awake! You win the game!"
	exit()

def re_start():
	print "\nyou can go any direction, where do you go?"
	choice = raw_input("> ")
	if choice == "left":
		peanut_butter_room()
	elif choice == "right":
		garlic_room()
	elif choice == "up":
		snorlax_room()
	elif choice == "down":
		oil_room()
	elif choice == "back":
		print "don't run away you pansy. We're gonna try this again and you will cooperate ya hear?"
		re_start()
	elif choice == "forward" or choice == "straight":
		snorlax_room()
	else:
		print "\nThere isn't room for your clever crap in this game. Now we have to start over"
		re_start()

def start():
	print """\n\tYou are a wild Pak
	You started sleep-walking unexpectedly!
	only delicious chocolate will wake you up
	You must seek the 4 medals that will allow you to pay for the delicious chocolate. \n"""

	print "\tyou can go any direction, where do you go?"
	choice = raw_input("> ")
	if choice == "left":
		peanut_butter_room()
	elif choice == "right":
		garlic_room()
	elif choice == "up":
		snorlax_room()
	elif choice == "down":
		oil_room()
	elif choice == "back":
		print "don't run away you pansy. We're gonna try this again and you will cooperate ya hear?"
		re_start()
	elif choice == "forward" or choice == "straight":
		snorlax_room()
	else:
		print "\nThere isn't room for your clever crap in this game. Now we have to start over"
		re_start()

def death(why):
	print why
	exit()

start()
