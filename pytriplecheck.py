
userinput = input("Please enter the three sides of the triangle, separating each with a space")
numbers = list(userinput.split( ))
numbers = [ int(x) for x in numbers ]
numbers.sort()
#print(numbers)

a = numbers[0]
b = numbers[1]
c = numbers[2]

if a**2 + b**2 == c**2:
    print("Congratulations you have a pythagorean triple!")
else:
    print("This is not a triple")