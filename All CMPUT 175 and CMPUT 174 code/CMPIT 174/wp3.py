# Word Puzzle Version 3
# This is a game in which the user is prompted to enter the miising letter of a
# random word
# The user has a total of four guesses
# The game then provides feedback according to the user guess. 


import random
import uagame

def main():
    Words_list = ['apple','banana','watermelon','kiwi','pineapple','mango']
    answer = random.choice(Words_list) 
    chosenword_list= list(answer)
    
    puzzle = '_'*len(answer)  #current state of puzzle 
    
    string_coords = [0, 0]
    
    #x=0
    #y=0
    
    window = create_window()
    
    instructions = ['I am tinking of a secerct word.',
                            'Try and guess the word. You can guess one letter',
                            'at a time. Each time you guess I will show you',
                            'which letters have been correctly guessed and which',
                            'letters are still missing. You will have 4 guesses to',
                            'guess all the letter. Good luck!']  
    
    
    display_instructions(window, instructions, string_coords)
    
    num_guesses = 4
    
    is_win = play_game(window, puzzle, answer, num_guesses, string_coords)
    
    display_result(window, is_win, answer, string_coords)
    
        #display_result(window, is_win, answer, string_coords)
    
    end_game(window, string_coords)


def create_window():
  # Create a window

  # return: a new uagame.Window object
    
    screen_width = 600
    screen_height = 600
    title = 'Word Puzzle'
    window = uagame.Window(title, screen_width, screen_height)
    return window


def display_instructions(window, instructions, string_coords):

  # Display the instructions for the game

  # - window is the uagame.Window object to draw to;

  # -instructions is a list of strings containing the game's instructions;
    
                        
    text_size = 24
    text_color = 'white'
    window.set_font_size(text_size)
    window.set_font_color(text_color)    
       
    for line in instructions:
        window.draw_string(line, string_coords[0], string_coords[1])
        font_height = window.get_font_height()
        string_coords[1] = string_coords[1] + font_height
        
   


     




def play_game(window, puzzle, answer, num_guesses, string_coords):

  # Prompts the player for guesses and processes them until the player has solved the puzzle or run out of guesses.

  # - window is the uagame.Window object to draw to;

  # - puzzle is a list representing the puzzles current state;

  # - answer is a string or list containing the answer;

  #return: a boolean indicating if the word was found or not.
    
    #text_size = 24 
    #text_color = 'white'
    #window.set_font_size(text_size)
    #window.set_font_color(text_color) 
    
    puzzle_list =list(puzzle)
    #puzzle_string= 'The answer so far is: '
    #font_height = window.get_font_height()
    #string_coords[1] = string_coords[1] + font_height    
    #window.draw_string(puzzle_string + (' '.join(puzzle_list)), string_coords[0], string_coords[1])    
    
    while num_guesses >=1:    
        
        display_puzzle_string(window, puzzle_list, string_coords)
        
        guess = get_guess(window, num_guesses, string_coords)
        
        if guess not in list(answer) or guess in puzzle_list:
            num_guesses= num_guesses-1        
    
        puzzle_list = update_puzzle_string(puzzle_list, answer, guess, num_guesses)
    
        
    
        is_win = is_word_found(puzzle_list, answer) 
        
        if is_win == True:
            break
        
    
    return is_win
    
     
            


def get_guess(window, num_guesses, string_coords):
 
  # Prompt the user for a guess and indicate the number of guesses remaining

  # - window is the uagame.Window object to draw to;

  # - num_guesses is the int number of guesses remaining;

  # return: a string with the player's guess;
    
    font_height = window.get_font_height()
            
    first_guess_string = 'Guess a letter ('
    guess_remainingstring = ' remaining guesses):'
    guess = window.input_string(first_guess_string+ str(num_guesses) + guess_remainingstring, string_coords[0], string_coords[1])
    string_coords[1] = string_coords[1] + font_height
    
     
    return guess
    




def update_puzzle_string(puzzle_list, answer, guess, num_guesses):

  # Given a new guessed letter, updates the state of our puzzle. Only updates letters if they haven't been guessed before.

  # - puzzle is a list representing the puzzles current state;

  # - answer is a string or list containing the answer;

  # - guess is a string containing the players most recent guessed letter;

  # return : A boolean indicating if an update was performed;
    
    
    #if guess in list(answer):
        #puzzle = puzzle.append(guess)
        
        
    #if guess != list(answer) or guess in list(puzzle):
        #num_guesses= num_guesses-1
    
    for i in range(0, len(answer)):
        if  guess == answer[i]:
            puzzle_list[i] = answer[i]
            #print(puzzle_list[i])
                        
          
    return puzzle_list

def display_puzzle_string(window, puzzle_list, string_coords):

  # Display the current state of the puzzle to the screen (Letters which have been guessed will be revealed).

  # - window is the uagame.Window object to draw to;

  # - puzzle is a list representing the puzzles current state;
    puzzle_string= 'The answer so far is:'
    font_height = window.get_font_height()
        
    window.draw_string(puzzle_string + (' '.join(puzzle_list)), string_coords[0], string_coords[1])
    string_coords[1] = string_coords[1] + font_height


def is_word_found(puzzle_list, answer):

  # Determines if the player has guessed all the letters in the puzzle or not;

  # - puzzle is a list representing the puzzles current state;

  #return: a boolean indicating if all the letters have been guessed;
    
    is_win = 0
    if puzzle_list == list(answer):
        is_win = True
        
    return is_win



def display_result(window, is_win, answer, string_coords):

  # Display whether the player was successful or unsuccessful

  # - window is the uagame.Window object to draw to;

  # - is_win is a bool which is true if the player guessed the word (the return object of play_game function());

  # - answer is a string or list containing the answer;
    if is_win == True:         
        font_height = window.get_font_height()
        #string_coords[1] = string_coords[1] + font_height       
        window.draw_string('Good Job! You found the word '+ answer+'!',string_coords[0], string_coords[1])
    else:
        font_height = window.get_font_height()
        #string_coords[1] = string_coords[1] + font_height        
        window.draw_string('Not quite, the correct word was '+ answer+'. Better luck next time',string_coords[0], string_coords[1])


def end_game(window, string_coords):
    
    # Prompts the player to end the game and close the window;
    # - window is the uagame.Window object to draw to;
    
    font_height = window.get_font_height()
    string_coords[1] = string_coords[1] + font_height     
    window.input_string('Press enter to end the game.',string_coords[0], string_coords[1])
    window.close()    

main()