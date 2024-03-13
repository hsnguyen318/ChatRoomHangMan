import socket
from hangman import *

# Server configuration
host = 'localhost'
port = 15550

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {host}:{port}")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')

    # Stop chat if message is /q
    if data == '/q':
        print('Client has requested shutdown. Shutdown!')
        break

    # Hangman game feature
    play_flag = 0  # Flag to know when user has won and stop loop.
    if data == 'HANGMAN':
        while play_flag != 1:
            # start game and get a random word/hint combo
            game = Hangman()
            random_word, hint = game.get_word()
            random_word = random_word.upper()

            # get count
            count = game.calc_count(random_word)

            # display first message to start game
            first_display_word = '_' * len(random_word)
            message = f'Game Started. Guesses left: {count}. Word: {first_display_word}. Hint: {hint}.'
            client_socket.send(message.encode('utf-8'))

            # display word after each guess
            display_word = ''
            while display_word != random_word and count > 0:
                guess = client_socket.recv(1024).decode('utf-8')
                # retry_message is what Hangman class returns after each guess. If the guess is invalid,
                # it will return a message. If it's valid, it will return nothing.
                retry_message = game.guess(guess)

                # If it returns something, send the error message to the user
                if retry_message is not None:
                    client_socket.send(retry_message.encode('utf-8'))
                # Else, display the word after this guess or display winning message.
                else:
                    count -= 1
                    display_word = game.display(random_word)
                    current_status = f'{display_word}. Guess left: {count}'
                    # If guess has been guessed (user won), display congratulations message

                    if display_word == random_word:
                        game.clear_guess_list()
                        message = f'Congratulations! You have won! Word is {display_word}. ' \
                                  f'Press any key to play again or Q to Quit.'
                        client_socket.send(message.encode('utf-8'))
                        # Ask user to continue or stop playing
                        choice = client_socket.recv(1024).decode('utf-8')
                        if choice == 'Q':
                            play_flag = 1

                    elif count == 0:
                        game.clear_guess_list()
                        loss_message = f'You have lost. The word is {random_word}. ' \
                                       f'Press any key to play again or Q to Quit. '
                        client_socket.send(loss_message.encode('utf-8'))
                        # Ask user to continue or stop playing
                        lose_choice = client_socket.recv(1024).decode('utf-8')
                        if lose_choice == 'Q':
                            play_flag = 1

                    # else, send word after this turn of guess
                    else:
                        client_socket.send(current_status.encode('utf-8'))
        # Problem is when losing, press Q starts a new game but not stopping. Works in win situation.

    print(f"Client: {data}")

    # Prompt for a reply
    reply = input("Enter reply: ")

    # if no data is entered, keep asking for input (user may accidentally hit enter)
    while not reply:
        # Prompt for a reply
        reply = input("Enter reply: ")

    # Send the reply to the client
    client_socket.send(reply.encode('utf-8'))

    if reply == '/q':
        print('Shutting down!')
        break

# Close the sockets
client_socket.close()
server_socket.close()
