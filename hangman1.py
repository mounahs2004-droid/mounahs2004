import random

def get_word():
    words=['python','hangman','program','developer','computer','code']
    return random.choice(words)

def play_game():
    word = get_word()
    guessed_letters=[]
    attempts = 6
    hidden_word = ["_"] *len(word)

    print("welcome to Hangman!")
    print("You have",attempts,"attempts to guess the word.")

    while attempts > 0 and "_"in hidden_word:
        print("\nWord:"," ".join(hidden_word))
        print("guessed Letters:",", ".join(guessed_letters))
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Enter only a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("correct!")
            for i in range(len(word)):
                if word[i]==guess:
                    hidden_word[i]=guess
        else:
            print("Wrong guess.")
            attempts-=1
            print("Attempts left:",attempts)
    
    if "_" not in hidden_word:
        print("\n you won! The word was:",word)
    else:
        print("\n You lost. The word was:",word)
    
def main():
    while True:
        play_game()
        again = input("\n play again? (y/n):").lower()
        if again !='y':
            print("Thanks for playing!")
            break

main()
pass