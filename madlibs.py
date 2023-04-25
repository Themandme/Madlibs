import random
print("Game List: ")
print("Mad Libs")
print("Press 1 for Mad Libs and 2 for (TBD)")
madlibs=1
gameselection = int(input("Select game "))

if gameselection == 1:
  madlibspick = random.randint(1,2)
if madlibspick == 1:
      noun = input("Choose a noun: ")
      insturment = input("Insturment: ")
      movie = input("Movie or Tv Show: ")
      Adjective  = input("Choose positive adjective: ")
      trait = input("Input trait of movie: ")
      print("Whoa, I can't believe how good " + movie + " was")
      print("It was totally " + Adjective)
      print("I loved when the hero got the " + noun)
      print("Yeah, and when they learned that song on the " + insturment)
      print("You're right. " + movie + " was pretty great! Here's hoping for a sequel with even more " + trait)
if madlibspick == 2:
      Adjective = input("Choose positive adjective: ")
      noun = input("Choose a noun: ")
      verb = input("Choose a verb: ")
      place = input("Choose a place: ")
      print ("After all these years, I'm finally visiting " + place)
      print ("Since I was young, i've been told about how " + Adjective + "_" + place + "is")
      print ("I can't wait to " + verb + "when I get there")
      print ("And i can't forget to bring my " + noun + "with me")
if gameselection == 2:
    print("Not ready yet! Please play Mad Libs!")
    gameselection = int(input("Select game "))

if gameselection > 2:
    print("Invalid Input")
    gameselection = int(input("Select game "))
