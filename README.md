A client-server chat room with an option to play Hangman.
Instruction:
- How to start: from the root folder, start server.py, then start client.py. At this point, client and
begin sending messages and server will listen.
- How to quit: Server and client can unilaterally quit by entering ‘q/’. Shutdown messages will be
shown on both sides.
- How to start game: Client can start playing Hangman by entering ‘HANGMAN’. Server will start
the game with a random word and the number of tries allowed. After the client wins or loses the
game, enter ‘Q’ to quit or press any key to play a new round.
- Game instructions: enter one guess (one letter at a time). Both upper and lower case are
accepted. If you enter more than one letter at a time, or enter a previously used letter, server
will prompt a message for another input. Only valid input will decrease remaining guess. If you
run out of guess, you will lose.
