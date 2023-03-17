print("Hello there.")
print("I want to say a word for no reason.")
while True:
    thought = input("Can you think of a word? (Y/N) ").lower()
    if thought == "Y":
        print("Excellent!")
        word = input("What word did you think of? ")
        print("Cool! Let me try say it. " + word + "!")
        break
    if thought == "N":
        print("Oh. Ok.")
        print("Bye, then.")
        break
    else:
        print("Sorry, I do not understand what you said.")