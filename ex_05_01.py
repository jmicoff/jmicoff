print("Five point one")
num = 0
tot = 0.0
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = int(sval)
    except:
        print('Invalid Input')
        continues
    num = num + 1
    tot = tot + fval
print("All done")
print("Total: ",tot, "Number of numbers entered:", num, "\nAverage:", tot/num)
