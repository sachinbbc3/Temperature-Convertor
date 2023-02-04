# This is the program for converting temperatures
celsius = float(input('input any number: '))
#this input is for celsius

#Calculate farenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree celsius is equal to %0.1f degree fahrenheit.' %(celsius,fahrenheit))
temp = fahrenheit

if temp > 92:
    print("It's very hot")  
    print("Drink a lot of water")

elif temp < 65:
    print("It's very cold")
    print(" Wear a jacket or a sweater")

else: 
    print("It's pleasant")
    