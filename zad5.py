dic = []
spamCount = 0
hamCount = 0
exclCount = 0
spamHam = open("SMSSpamCollection.txt")

for line in spamHam:
    line = line.rstrip()
    if(line.startswith("spam")):
        spamCount = spamCount + 1
        if(line.endswith("!")):
            exclCount = exclCount + 1
    elif(line.startswith("ham")):
        hamCount = hamCount + 1

spamHam.close()

hamVreage = float(hamCount/(hamCount+spamCount)) 

print("Koliko hama? " + str(hamCount) + " prosijek " + str(hamVreage))
print("Koliko spama? " + str(spamCount) + " prosijek " + str(1-hamVreage))

print("Spam, a završava sa !: " + str(exclCount))