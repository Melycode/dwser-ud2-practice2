# 1. Crea una función greet() que imprima “Hello world” por consola. 
def greet():
    print("Hello world")

#2. Crea una función greet(name) que imprima “Hello <nombre>” por consola, 
#y llámala varias veces con distintos nombres. 

def greet1(name):
    print(f"Hello {name}")

greet1("Antonio")
greet1("Akemi")
greet1("Milan")


def greet2(name):
    return f"Hello {name}"

print(greet2("José Antonio"))
print(greet2("Akemi Guadalupe"))
print(greet2("Milan Adrián"))


#3. Crea una función pow(a, b) que devuelva el resultado de a elevado a la b
def pow(a,b):
    print(a**b)
pow(2,3) 


def pow1(a,b):
    return a**b 

print(pow1(2,3)) 


#4. Crea una función celsius_to_fahrenheit(temperature) que transforme 
#Celsius en Fahrenheit y devuelva el resultado. 
def celsius_to_fahrenheit(temperature):
        return (temperature * 1.8) + 32 #esta fórmula siempre es para convertir C a F

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(20))


#5. Crea una función area_circle(radius) que devuelva el área de un círculo. 
def area_circle(radius):
    return (radius **2) * 3.1416

print(area_circle(3))
print(area_circle(6))

#6. Crea una función avg(a, b, c) que devuelva la media de tres números a, b y c. 
def avg(a,b,c):
    return (a + b + c) / 3

print(avg(10,20,30))


#7. Crea una función concat(a, b, c) que devuelva una única cadena de texto, 
#concatenando las cadenas a, b y c.
def concat(a,b,c):
    return f"{a} {b} {c}"

print(concat("Hola", "Ana", "Gómez"))

#8. Crea una función full_name(name, surname1, surname2) que devuelva el 
#nombre completo de una persona. 
def full_name(name, surname1, surname2):
    return f"{name} {surname1} {surname2}"

print(full_name("Akemi", "Gutiérrez", "Guerrero"))

#9. Crea una función current_age(birth_year) que devuelva la edad actual de 
#una persona (sin tener en cuenta el día). 
def current_age(bith_year):
    return 2026 - bith_year

print(current_age(1979))

#10. Crea una función introduction(name, surname1, surname2, birth_year) que 
#utilice las 2 funciones anteriores e imprima por pantalla “Hello, I’m 
#<nombre completo> and I’m <edad> years old”. 
def introduction(name, surname1, surname2, birth_year):
    print (f"Hello, I’m {full_name(name, surname1, surname2)} and I’m {current_age(birth_year)} years old")

introduction("Frida", "Carnero", "De Guerrero", 1953)

#11. Crea una función welcome() que imprima “Welcome to this Python lesson” 
#por consola. 
def welcome():
    print(f"Welcome to this Python lesson")

welcome()

#12. Crea una función welcome(name) que imprima “Hello, <nombre>, welcome 
#to this Python lesson” por consola. 
def welcome1(name):
    print(f"Hello, {name}, welcome to this Python lesson")

welcome1("Melissa")

#13. Crea una función double(number) que devuelva el doble de un número. 
def double(number):
    return(number * 2)

print(double(2))

#14. Crea una función price_with_tax(price) que devuelva el precio de un 
#producto sumándole el IVA (21%). 
def price_with_tax(price):
    return price + (price * 0.21) #también price * 1.21 es mejor x ser corto

print(price_with_tax(10))


#15. Crea una función price_with_tax(price, tax) que devuelva el precio de un 
#producto sumándole el impuesto dado como parámetro. 
def price_with_tax1(price, tax):
    return price + (price * tax) 

print(price_with_tax1(20,0.18))


#16. Crea una función volume_cube(side) que devuelva el volumen de un cubo. 
#El volumen de un cubo es lado3 
def volume_cube(side):
    return side ** 3 

print(volume_cube(8))


#17. Crea una función time_to_seconds(hours, minutes, seconds) que devuelva 
#el número total de segundos, dado un número de horas, minutos y 
#segundos. 
def time_to_seconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds

print(time_to_seconds(1, 43, 58))

#18. Crea una función pretty_text(text) que devuelva una cadena con el formato 
#“=== <texto> ===”. 
#Por ejemplo, “=== My cool text ===” 
def pretty_text(text):
    return f"=== {text} ==="

print(pretty_text("My cool text"))

#19. Crea una función format_name(name, surnames) que devuelva una 
#cadena de texto con el formato “<Apellidos>, <Nombre>”. 
#Por ejemplo, “Pérez Álvarez, Pepito” 
def format_name(name, surnames):
    return f"{surnames}, {name}"

print(format_name("Melissa", "Guerrero Carnero" ))


#20. Crea una función passed(grade1, grade2, grade3) que calcule la media de 
#tres notas y devuelva True o False, según si la media es mayor o igual que 5. 
def passed(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3
    return average >= 5

print(passed(9, 6, 8))


#21. Crea una función student_passed(name, surnames, grade1, grade2, grade3) 
#que imprima por consola “<Apellidos>, <Nombre> has passed the subject: 
#<True/False>”. 
#Por ejemplo, “Pérez Álvarez, Pepito has passed the subject: True” 
def student_passed(name, surnames, grade1, grade2, grade3):
    print(f"{format_name(name, surnames)} has passed the subject: {passed(grade1, grade2, grade3)}")

student_passed("Frida", "Guerrero Carnero", 9,8,7)