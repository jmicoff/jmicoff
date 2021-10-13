print("Five point two")
smallest = None
largest = None
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = int(sval)
    except:
        print('Invalid Input')
        continue
    if largest is None :
        largest = fval
    elif fval > largest :
        largest = fval
    print(largest, fval)
    if smallest is None :
        smallest = fval
    elif fval < smallest :
        smallest = fval
    print(smallest, fval)
print(largest, fval)
print(smallest, fval)
print('After' , largest)
print('After' , smallest)
print("All done")
print("Largest number entered:", largest)
print("Smallest number entered", smallest)
