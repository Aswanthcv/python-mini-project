print("Welcome to my first Game 🎮 (Choose your path and win!)")

name = input("What is your name?: ")
age = int(input("Enter your age: "))

print(f"Hello {name}")

if age<18:
    print("You are not old enough to play")
    exit()
else:
    print("You are old enough to play.")
    def pause():
        input("\nPress Enter to continue...")

    ready = input("Are you ready to play? (y/n): ").lower()
    if ready != "y":
        print("See you later 👋.")
        exit()
    print("\nGame starts! 🎮")
    
    def show_health(health):
        print("Your Health:"," ❤️"*health)

    health=3
    show_health(health)    
    while health > 0:

        left_or_right = input("\nYou wake up in an unknown place. Choose your path 👣 (left/right): ").lower()

        if left_or_right == "left":
            print("Cracking sounds...")
            pause()
            print("You fall but manage to survive.")
            health -= 1
            print("You lost 1 health.")
            show_health(health)


            if health == 0:
                print("GAME OVER 🏳️")

                break

            print("You find yourself back at the starting point.")

        elif left_or_right == "right":
            print("In front of you is an ocean 🌊 with a distant island 🏝️.")
            print("A wooden boat 🚣 is tied to the shore.")

            island_or_stay = input(
                "Do you take the boat or stay here? (island/stay): "
            ).lower()

            if island_or_stay == "stay":
                print("You wait near the water...")
                pause()
                print("A crocodile attacks you! 🐊")
                health -= 1
                print("You lost 1 health. ")
                show_health(health)


                if health == 0:
                    print("GAME OVER 🏳️ ")
                    break

                print("You escape and return to the starting point.")

            elif island_or_stay == "island":
                print("You take the boat and reach the island 🏝️.")
                print("It is quiet... too quiet.")

                forest_or_cave = input(
                    "Two paths ahead: forest 🌳 or cave? (forest/cave): "
                ).lower()

                if forest_or_cave == "cave":
                    print("You step into the dark cave 🕳️...")
                    pause()
                    print("You feel a dark presence around you 👻")

                    cave_choice = input(
                        "Do you try to run back or stay frozen? (run/stay): "
                    ).lower()

                    if cave_choice == "run":
                        print("You run as fast as you can! 🏃‍♂️")
                        health -= 1
                        print("You escaped, but lost 1 health.")
                        show_health(health)

                        if health == 0:
                            print("Your injuries were too severe.")
                            print("GAME OVER 🏳️")
                            break

                        print("You somehow make it back to the starting point.")

                    elif cave_choice == "stay":
                        print("You freeze in fear...")
                        pause()
                        print("The darkness consumes you 👻")
                        print("GAME OVER 🏳️")
                        break

                    else:
                        print("You hesitate too long...")
                        print("The darkness consumes you 👻")
                        print("GAME OVER 🏳️")
                        break



                elif forest_or_cave == "forest":
                    print("Sunlight filters through the trees 🌳🌄.")
                    pause()
                    print("You find a glowing stone 💎.")
                    print(f"You survived with {health} health left.")
                    print("Congratulations! You WON! 🎉🥂")
                    break

                else:
                    print("Invalid choice ❌.")

            else:
                print("Invalid choice ❌.")

        else:
            print("Invalid choice ❌.")

    print("\nThanks for playing. 🤗")
