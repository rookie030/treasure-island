from random import choice

print(r'''
*  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~____~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('You stand at a fork in the path. Choose your path, "Left" or "Right".').lower()

if direction == "left":
    # Continue the game
    action = input('Good choice! You safely take the left path.'
                   '\nYou enter the forest and find a sparkling river blocking your path. '
                   'Type "wait" to wait for a boat or type "swim" to swim across.').lower()
    if action == "wait":
        colour = input('You arrived at the island safe. '
                       'There is a house with 3 doors.One red, one yellow, and one blue. '
                       'Which colour will you choose?: ').lower()
        if colour == "yellow":
            choice = input('A big and bad monster appeared. Will you choose to "Fight" or "Flee"?').lower()
            if choice == "fight":
                choice2 = input('What will you use? Your "sword" or your "magic"?')
                if choice2 == "magic":
                    magic = input('What magic will you use? "Water", "Fire", "Wind", or "Earth" magic?').lower()
                    if magic == "water":
                        print("The monster got its shampoo and cleaned its fur."
                              "\nAfter cleaning it attacked you with a single swipe. You died. Game over!")
                    elif magic == "fire":
                        print("As you used your fire magic the monster got a marshmallow and grilled the marshmallow using your fire magic."
                              "\nThe monster attacked you and used your remaining fire magic to barbecue you. Game over!")
                    elif magic == "wind":
                        print("The gust of wind magic destroyed the perfectly styled fur of the monster."
                              "\nIt got angrier, grabbed you and ate you. Game Over!")
                    else:
                        print("You used your earth magic. you created a big hole where the monster is standing."
                              "\nThe monster fell to the hole that you created.")
                        print("\nYou saw a treasure chest where the monster came out. You opened it and found out that it has nothing inside.\nBetter luck next time ;)")
                else:
                    print("The monster is immune to physical attacks. It grabbed you and ate you. Game over!")
        elif choice == "flee":
            print("As you tried to flee, the monster caught up and grabbed you. "
                  "\nThe monster ate you. Game over.")
        elif colour == "blue":
            print("You entered the blue door. As you go further, it got colder and colder. "
          "You froze to death. \nGame Over!")
        elif colour == "red":
            print("A burst of flames came gushing out of the door. "
                  "You weren't able to dodge it. You got incinerated. \nGame Over!")
        else:
            print(' You chose a door that didn\'t exist. Game Over!')
    else:
        print("You decided to swim, the river is infested by piranhas. "
              "The piranhas ate you. Game Over!")
else:
    print("You stumbled upon a snapping turtle that bit you in the leg. You bled to death. Game over!")
