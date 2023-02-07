#! usr/bin/env python3

#Programming Assignment 3
#Lexi Rossow
#January 30, 2023
#Pet Walk of Fame

#Lists
#pet names list
names = ["LASSIE", "OLD YELLER", "MORRIS",
         "SCOOBY DOO", "WHITE FANG", "KEANU",
         "BENJI", "GARFIELD"
         ]

#species list
species = ["unknown", "dog", "cat",
           "unknown", "dog", "cat",
           "unknown", "unknown"
           ]

#fame list
fame = ["Series", "Movie", "Commercial",
        "Unknown", "Book", "Unknown",
        "Unknown", "Cartoon"]

#ways to fame list
WAYSTOFAME = "Validate ways to fame are: "
waystofamelist = ["series", "movie", "commerical",
                "book", "cartoon"]

#display lists
print("These are the pets for the Pet Walk of Fame: ")
print(*names, sep="\n")
print()


#user prompt for pet's name
userPetName = input("Please enter a pet's name: ")
print()

#upper or lower case entries validation
upperUserPetName = userPetName.upper()

#Lassie, location 0  
if upperUserPetName == "LASSIE":

    #species
    print(userPetName.title() + "'s species is " + species[0].lower(), end=".\n")
    print()
    userCorrection0 = input("Please enter 'dog' or 'cat' for species: ")
    species.remove(species[0])
    species.insert(0, userCorrection0.lower()) 
    print("Thank you, the new species is saved as " + species[0], end=".\n")
    print()

    #fame
    print(userPetName.title() + "'s fame is from a " + fame[0].lower(), end=".\n")
    print()
    

#Old Yeller, location 1
elif upperUserPetName == "OLD YELLER":
    print(userPetName.title() + "'s species is " + species[1].lower(), end=".\n")
    print(userPetName.title() + "'s fame is from a " + fame[1].lower(), end=".\n")
    

#Morris, location 2
elif upperUserPetName == "MORRIS":
    print(userPetName.title() + "'s species is " + species[2].lower(), end=".\n")
    print(userPetName.title() + "'s fame is from a " + fame[2].lower(), end=".\n")
    

#Scooby Doo, location 3
elif upperUserPetName == "SCOOBY DOO":

    #species
    print(userPetName.title() + "'s species is " + species[3].lower(), end=".\n")
    print()
    userCorrection3 = input("Please enter 'dog' or 'cat' for species: ")
    species.remove(species[3])
    species.insert(3, userCorrection3.lower()) 
    print("Thank you, the new species is saved as " + species[3].lower(), end=".\n")
    print()
    
    #fame
    print(userPetName.title() + "'s way to fame is " + fame[3].lower(), end=".\n")
    print()
    print(WAYSTOFAME)
    print(*waystofamelist, sep="\n")
    print()
    userFame3 = input("Please enter a way to fame for this pet: ")
    fame.remove(fame[3])
    fame.insert(3, userFame3.title())
    print("Thank you, the new way to fame is saved as a " + userFame3.lower(), end=".\n")
    print()

#White Fang, location 4
elif upperUserPetName == "WHITE FANG":
    print(userPetName.title() + "'s species is " + species[4].lower(), end=".\n")
    print(userPetName.title() + "'s fame is from a " + fame[4].lower(), end=".\n")
    

#Keanu, location 5
elif upperUserPetName == "KEANU":
    print(userPetName.title() + "'s species is " + species[5].lower(), end=".\n")

    #fame
    print(userPetName.title() + "'s way to fame is " + fame[5].lower(), end=".\n")
    print()
    print(WAYSTOFAME)
    print(*waystofamelist, sep="\n")
    print()
    userFame5 = input("Please enter a way to fame for this pet: ")
    userFame5.title()
    fame.remove(fame[5])
    fame.insert(5, userFame5.title())
    print("Thank you, the new way to fame is saved as a " + userFame5.lower())
    print()
    

#Benji, location 6
elif upperUserPetName == "BENJI":

    #species
    print(userPetName.title() + "'s species is " + species[6].lower(), end=".\n")
    print()
    userCorrection6 = input("Please enter 'dog' or 'cat' for species: ")
    species.remove(species[6])
    species.insert(6, userCorrection6.lower()) 
    print("Thank you, the new species is saved as " + species[6].lower(), end=".\n")
    print()

    #fame
    print(userPetName.title() + "'s way to fame is " + fame[6].lower(), end=".\n")
    print()
    print(WAYSTOFAME)
    print(*waystofamelist, sep="\n")
    print()
    userFame6 = input("Please enter a way to fame for this pet: ")
    userFame6.title()
    fame.remove(fame[6])
    fame.insert(6, userFame6.title())
    print("Thank you, the new way to fame is saved as a " + userFame6.lower())
    print()

#Garfield, location 7
elif upperUserPetName == "GARFIELD":

    #species
    print(userPetName.title() + "'s species is " + species[7].lower(), end=".\n")
    print()
    userCorrection7 = input("Please enter 'dog' or 'cat' for species: ")
    species.remove(species[7])
    species.insert(7, userCorrection7.lower()) 
    print("Thank you, the new species is saved as " + species[7], end=".\n")
    print()

    #fame
    print(userPetName.title() + "'s fame is from a " + fame[7].lower())

#not in the walk of fame
else:
    print("Sorry, " + userPetName.title() + " is not on this Walk of Fame.")
    
    
#updated lists for species
print()
print("The updated species list: ")
print(*species)

#updated lists for Famous For
print()
print("The updated famous for list: ")
print(*fame)




