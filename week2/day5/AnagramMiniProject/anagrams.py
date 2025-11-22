from anagram_checker import AnagramChecker

def main():
    # Step 1: Create an instance of AnagramChecker with your word list file
    checker = AnagramChecker("wordlist.txt")  # Replace with your actual word list filename

    while True:
        # Step 2 & 3: Create a menu loop and get user input
        print("\nAnagram Checker Menu:")
        print("1. Check a word for anagrams")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ").strip()  #.strip() removes any extra spaces before or after the input to avoid errors


        if choice == '1':
            word = input("Enter a word to check: ").strip()     #.strip() removes any extra spaces before or after the input to avoid errors


            # Step 3: Validate the word
            if not checker.is_valid_word(word):    #uses the is_valid_word method to check if the entered word exists in the word list
                print(f"'{word}' is not a valid word in the word list.")
                continue

            # Step 4: Find anagrams
            anagrams = checker.get_anagrams(word)  # this line finds all anagrams of the word using the get_anagrams method

            # Display results
            print(f"\nWord: {word}")    # these 2 lines print the word the user entered and confirm it is valid
            print(f"Valid word: Yes")

            if anagrams:
                print(f"Anagrams found: {', '.join(anagrams)}") #If there are anagrams, it prints them separated by commas
            else:
                print("No anagrams found.")

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":   #checks if the script is being run directly (not imported as a module)
    main()
    

