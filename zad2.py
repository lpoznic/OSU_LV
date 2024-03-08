try:
    x = float(input("Upišite ocjenu: "))
    if x<0 or x>1:
        print("Ocjena nije u intervalu [0,1]")
    if(x>= 0.9 and x<=1):
        print("A")
    elif(x>= 0.8 and x<0.9):
        print("B")
    elif(x>= 0.7 and x<0.8):
        print("C")
    elif(x>= 0.6 and x<0.7):
        print("D")
    elif(x>=0 and x<0.6):
        print("F")


except:
    print('Ocjena nije pravilno unesena')