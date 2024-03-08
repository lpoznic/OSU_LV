lyrics = {}
number_of_words = 0
 
with open(r'song.txt','r') as file:
 
    data = file.read()

    lines = data.split()

    for word in sorted(lines):
        for current in sorted(lines):
            print(word)    

