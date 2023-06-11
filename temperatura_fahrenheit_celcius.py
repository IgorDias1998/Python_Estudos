#Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9)

graus_fahrenheit = int(input('Digite a temperatura em F: '))
graus_celcius = 5 * ((graus_fahrenheit-32) / 9)

print(f"Temperatura em °C: {graus_celcius:.2f}")