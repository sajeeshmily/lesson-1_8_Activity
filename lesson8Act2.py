
numn = int(input("Enter the numerator: "))
numd = int(input("Enter the denominator: "))

if numd != 0:
    if numn % numd == 0:
        print(numn, "is divisible by", numd)
    else:
        print(numn, "is not divisible by", numd)
else:
    print("Denominator cannot be zero.")
