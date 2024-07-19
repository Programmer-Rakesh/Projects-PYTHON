# String concatinatio  ( How to put strings together)
# Suppose we want to create a string that says "subscribe to____"
#youtuber = "Hapsi"

# A few waus to to this :
#print("Subsrcibe to " + youtuber)
#print("Subscribe to {}".format(youtuber))
#print(f"Subscribe to {youtuber}")

adj = input("Adjective : ")
verb1 = input("Ver1 : ")
verb2 = input("Verb2 : ")
famous_person = input("Famous Person : ")

madlib =  f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)