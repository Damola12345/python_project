import sys

print("welcome to my favorite artiste game")

playing = input("Do you want to play? ")

supported_value = ["y", "yes"]

if playing.lower() not in supported_value:
    sys.exit(1)

print("okay let's play")

artiste = input("who's my fav artiste: ")
artiste_db = {
    "buju":         ["something sweet", "never stopped", "i do"],
    "ayra star":    ["beggie beggie", "fashion killer", "lonely"],
    "ruger":        ["dior", "snapchat", "bounce"],
    "wizkid":       ["big mood", "true love", "blessed"]
}

print("your fav artiste is {}".format(artiste))
if artiste.lower() in artiste_db:
    print("correct")
else:
    print("incorrect")
    sys.exit(1)



artiste_track = input("enter a track of your fav artiste: ")

if artiste not in artiste_db:
    print("Artiste not found")
    sys.exit(1)


picked_artiste = artiste_db[artiste]

if artiste_track.lower() in picked_artiste:
    print("music found, correct!!! ")
else:
    print("music not found, incorrect!!!")
    sys.exit(1)


print("congrat you got it right! ")
