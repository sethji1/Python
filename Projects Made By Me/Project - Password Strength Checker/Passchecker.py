print("Welcome To Password Strength Checker")
print("Your Password should be 8 Charcaters Long")
pass_input= str(input("Enter You Password Please:"))
a = len(pass_input)
if(a>8):
    print("Password Is Valid")
elif(a<8):
    print("Password Should Be 8+ Word long")
