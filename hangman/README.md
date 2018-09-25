Welcome to Instrument Hangman!

hangman.py will be able to run in your Python debugging environment as long as all the text files are in the same location as hangman.py.

This game will print out a number of underscores which represent letters that make up a word. Your goal is to fill in these blanks by guessing letters until you have an entire word spelled out. Your only initial clues about the word are the number of letters it has and that it is the name of a musical instrument. The game will randomly select one of 25 possible common western musical instruments.

You can guess upper or lower case letters by typing one character and pressing "Enter". If your letter is in the word, that letter will be shown in its correct position(s) in the word. If it is not in the word, part of the "Treble Man" will show on the noose. You can continue guessing letters one at a time until the entire word is spelled or until the entire Treble Man is hanging to his death. The instrument name will be revealed to you either way.

You can also go for the entire word at any point. Just type the entire word and press "Enter". If your guess is incorrect, however, you will lose the game and see the death of Treble Man.

You may also quit your attempt at a word by typing "quit" and you will be asked if you would like to continue playing.

You will not be penalized for guessing letters you have already guessed or for typos such as symbols or numerous characters. The only way to mess up in this way is to type the same number of characters as are contained in the word, as this will be considered a guess at the entire word.

At the end of every game, you will be asked if you would like to keep playing with prompt "(y/n)" indicating to type either 'y' or 'n', 'yes' or 'no', 'ya' or 'nah', 'heck yes!' or 'not really', etc. It looks for either letter with 'n' taking priority. If you continue, a new word will be chosen from HMwords.txt. You can play up to 25 games until the program automatically terminates.
