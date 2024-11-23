# BATTLESHIPS
     Video Demo:  https://www.youtube.com/watch?v=zfJ3C5_G32k

 Description:

Battleship is a **two player game** which resembles the classic board game which bears its name.

The game starts with an introduction and then the two players may proceed to the game by typing "start", should the know the rules.Should they not, they may type "help" to see some information on how to play the game.

After leaving the main menu by typing "start", players get to choose the difficulty (or level) which translates into the size of the territory in which they are going to place their ships. For simplicity and functionality, it has been designed so, that the levels are between 3 and 7 but this design is subject to change. For example, if players choose difficulty 4, the teritory where they are going to place the ships is going to be a 4x4, two-dimensional array. After that, they choose the number of ships to place in their terittory. The number varies from 3 to 7 and it is so, that the game does not last too long or too briefly.

Then, each player gets the chance to type his name or nickname. This was designed so that the players won't be confused with the terms "player 1" or "player 2" and has one additional usefulness to which we will return soon.

After that, and upon being called by the system with their nicknames, each player "hides" their ship in their sea.Once placed, a ship cannot be moved to a different  place. The placement is done via the indexing of an array (rows and columns from zero to level-1).It has been designed so that every Value or Index Error is caught and the player is reprompted to place their ship. Every time a ship is placed, the player can see where their ships have been put, so it is crucial that the other player look away during that process.

After both players place their ship we proceed to the attacking phase. In this phase, each player one by one, after seeing how many ships of theirs are safe (if one of their ships has been converted to a fire it means that it has been hit),tries to attack an opponent ship by guessing its coordinates. The coordinates again are determined via the indexing of an array.Here as well,it has been designed that every error either Value or Index reprompts the player.The player can see if they hit or missed the opponent ships after the seeing the fire or the sea emoji on their mystery array respectively.The game ends when one player eliminates all the ships from the other player (thus the little fires resembling the ship attacks equal the number of ships in the winning players mystery array).

Then the name/nickname of the winning player is registered in a file named HallOfFame.txt to remind them of their success in the passage of time.

**What does each function do?**

**main()**: basically runs the players through the game from main menu to end.Uses  time.sleep(seconds) to provide time for the players to read the instructions. Pressing control+d (EOF) ends the programm-game early.

**create_sea(level)** : creates an array full of sea wave emojis before the players put their ships

**create_mystery(level)**: creates an array full of question mark emojis. These arrays (one for each player), later, will contain each player guesses
**print_array(matrix,level)**: basically a shortcut to printiing an array

**put_ships(level)**: handles each players placement of ships via prompting rows and columns and catches any Index or Value Errors reprompting the users. Also, makes the player replace a ship if he puts it in the same place

**pass_turn(s)**: handles the passing of a turn, and prepares the terminal for the round.Returns boolean.

**attack(sea,mystery,level)**: handles the attacking phase, displaying if the attacker has the hit the enemy ship via the mystery array with a replaced element.Returns boolean.It also catches any type of Index or Value Error reprompting the player.


**libraries**

**os**: used to clean the terminal via **os.system("clear")** so that one player can't see the other players board and vice versa.

**sys**: to succesfully exit the programm in case of control+d via **sys.exit()**

**time**: to use **time.sleep(seconds)** to stall the running of the game when needed.

None of these libraries require installation (built-in in python module).
To start the programm type **python project.py** (you have to be in project folder first. If you are not, type **cd project**)





