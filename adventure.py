def play_again():
    print("\nDo you want to play again? (yes or no") 

    answer = input(">").lower()

    if "yes" in answer:
        start()
    
    else:
        exit()
        
def game_over(reason):
    print("\n" + reason)
    print("Game over")

    play_again()
def escape():
    print("You run for what seems to be hours. Others fall behind, or trip over the cobblestone path")
    print("You dare not look back. You don't know what you are running from but thee atmosphere and looks on peopls faces is enough to make you panic")
    print("You successfully make it to the nearest town. The guards outside usher the people that are left in")
    print("You are safe... for now.")

def outside():
    print("\n You walk outside and take a closer look at the people")
    print("A lot of them are covered in blood, but it doesn't seem to be their own")
    print("A frail old man passing by yells at you to run")
    print("In your hesitation you suddenyl feel a sharp pang in your chest")
    print("You look down to see long claws ripping through your ribs")
    print("You collapse, trying to cover the whole that was you chest")
    print("Before your last breathe you witnesswhat was chasing the village")
    print("They have the complexion and build of the dark elves...")
    print("But how? You've only ever read about them in books... how?")
    print("You died.")

def inside():
    print("\nYou take a peek out the closest window")
    print("You see many people running all in the same dangeous")
    print("Are they running away, or towards something?")
    print("Leading the horde of people is a tall muscular woman")
    print("She's covered in blood and wounds, her face plastered with a terrified expression")
    print("Do you:")
    print("1 - Go back to drinking ale and minding your own business")
    print("2 - Ask someone outside what is going on")

    answer = input(">")

    if answer == "1":
        game_over("The sky suddenly turns dark and the sound of screeching monsters grows louder")
        game_over("The bar becomes overrun with human-like creatures who have long claws and the sharpest teeth you have ever seen. They don't seem to speak the common tongue. One walks towards you slowly. Your last memory is seeing his long claws penetrate your abdomen")
        game_over("You bleed out on the floor to the sounds of your village being murdered. You died.")

    elif answer == "2":
        print("You walk over to the door with an anxious shake in each step. You open it and watch the horrified crowd run")
        print("You find the closest person and ask 'What's happening why is everyone running?'")
        print("The young boy replies. There's no time you have to run. They're coming. They'll kill us all. RUN.")
        print("and with that the boy frantically joins the crowd and leaves")
        print("Do you:")
        print("1 - Join the crowd and run with them")
        print("2 - Walk in the opposite direction in the crowd to see where this commotion is coming from")

        answer = input(">")
        if answer == "1":
            print("You join the panicked crowd and run at their pace, trying to keep up")
            escape()
        
        elif answer == "2":
            print("You begin walking towards where the bloodied people are coming from, going against every fibre of your body")
            print("You see them. The dark elves. The fictional race, or so you thought.")
            print("A slender and beautiful dark elf walks sensually in your direction. You lock eyes with her ruby red eyes.")
            print("Her silver hair catches the breeze, she tucks a lock behind her ear. Her long claws catch your attention. Dark elves don't have claws like that, do they?")
            print("You blink once and she leaps towards you with the force of a tiger hunting its prey")
            print("Your world fades away. The last thing you hear is her sweet laugh as she walks away from your corpse.")
        
        else:
            game_over("Try typing an actual response")

    else:
        game_over("There's only 2 numbers to try, type again")

def start_room():
    print("\nYou are sitting at your local bar, listening to the pleasant strums of the bards lap harp")

    print("All of a sudden commotion erupts from outside")

    print("Do you look out the window, or go outside?")

    answer = input(">").lower()

    if "wind" in answer:
        inside()

    elif "out" in answer:
        outside()

    else:
        game_over("There's only two options... try again.")



start_room()



