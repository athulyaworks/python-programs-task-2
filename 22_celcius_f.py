#Use map() to convert temperatures from Celsius to Fahrenheit. 

celsius = list(map(float, input("Enter Celsius temperatures by space-separated: ").split()))

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print("Fahrenheit temperatures:", fahrenheit)




