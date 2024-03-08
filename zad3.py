numbers = []
number = 0
avg = 0

while True:
    number = input("Upišite broj: ")
    if number == "Done":
        print(numbers)
        break

    else:
        try:
            numbers.append(float(number))
        except:
            print("Nije unesen broj")

avg = float(sum(numbers)) / float(len(numbers))

print("Srednja vrijednost liste: " + str(avg))
print("Najveći broj: " + str(max(numbers)))
print("Najmanji broj: " + str(min(numbers)))
    
    