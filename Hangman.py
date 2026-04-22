import random
class Hangman:
    def __init__(self):
        self.words = {
            "python": ["Programming language", "Snake name", "Used in AI"],
            "computer": ["Electronic device", "Processes data", "Has CPU"],
            "science": ["Study of world", "Experiments", "Physics branch"],
            "developer": ["Writes code", "Builds apps", "IT job"],
            "keyboard": ["Typing device", "Has keys", "Input device"]
        }

        self.word = random.choice(list(self.words.keys()))
        self.hints = self.words[self.word]

        self.guessed_letters = []
        self.wrong_letters = []   # NEW: track wrong guesses
        self.attempts = 6
        self.hint_index = 0

        self.stages = [
            """
               -----
               |   |
               O   |
              /|\\  |
              / \\  |
                    |
            ---------
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
              /    |
                    |
            ---------
            """,
            """
               -----
               |   |
               O   |
              /|\\  |
                    |
                    |
            ---------
            """,
            """
               -----
               |   |
               O   |
              /|   |
                    |
                    |
            ---------
            """,
            """
               -----
               |   |
               O   |
               |   |
                    |
                    |
            ---------
            """,
            """
               -----
               |   |
               O   |
                    |
                    |
                    |
            ---------
            """,
            """
               -----
               |   |
                   |
                    |
                    |
                    |
            ---------
            """
        ]

    def display_hangman(self):
        print(self.stages[self.attempts])

    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord:", display)

    def show_hint(self):
        if self.hint_index < len(self.hints):
            print(f"💡 Hint {self.hint_index + 1}: {self.hints[self.hint_index]}")
            self.hint_index += 1

    def guess_letter(self, letter):
        if letter in self.guessed_letters or letter in self.wrong_letters:
            print("⚠ Already guessed this letter!")
            return

        if letter in self.word:
            print(f"✅ Correct guess: '{letter}'")
            self.guessed_letters.append(letter)
        else:
            print(f"❌ Wrong guess: '{letter}'")   # shows wrong letter
            self.wrong_letters.append(letter)
            self.attempts -= 1
            self.show_hint()

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        return self.attempts <= 0

    def play(self):
        print("🎮 Hangman (Advanced Version)")

        self.show_hint()

        while True:
            self.display_hangman()
            self.display_word()

            print("Attempts left:", self.attempts)
            print("Correct letters:", self.guessed_letters)
            print("Wrong letters:", self.wrong_letters)

            guess = input("Enter letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input!")
                continue

            self.guess_letter(guess)

            if self.is_won():
                print(f"\n🎉 You Won! Word: {self.word}")
                break

            if self.is_lost():
                self.display_hangman()
                print(f"\n💀 You Lost! Word: {self.word}")
                break


# Run game
game = Hangman()
game.play()