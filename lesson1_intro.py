print("hey")
print("2"+"2")
print(2+2)
if(5>2):
 print("5")
 if(5<6):
     print("six")
print("My name is", "Python.", end=" ")
print("Monty Python.")
print("My", "name", "is", "Monty", "Python.", sep="-")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("H", "E", "L", "L", "O", sep="-")
print("H", "E", "L", "L", "O", sep="\n"),

print("2")
print(2)
print(0o123)
print(0x123)
##2.5 -0.4
## 0.4 так: .4.
## : 4 та 4.0.
## : 300000000.  3E8
##
## Літера Е (можна використати і малу літеру е, від слова «exponent» — степінь) — це короткий запис фрази 
##«стільки-то, помножене на десять у такому-то стпепені».
##
## Фізична константа називається постійною Планка (і 
##позначається як h), згідно з підручниками, вона становить: 6,62607 х 10-34.
##Якщо ви хочете використати її в програмі, записується 
##вона так: 6.62607E-34
##
##print(0.0000000000000000000001)
##1e-22


print("I like \"Monty Python\"")
print('I like "Monty Python"')
print(True > False)
print(True < False)
print(2+2)

##Знак ** (подвійна зірочка) — оператор піднесення 
##до степеня. Його лівий аргумент є основою, а правий — 
##степенем.

print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)


print(2 * 3) 
print(2 * 3.) 
print(2. * 3) 
print(2. * 3.)

print(6 / 3) 
print(6 / 3.) 
print(6. / 3) 
print(6. / 3.)
print(6.2 / 0.3)


print(6 // 3) 
print(6 // 3.) 
print(6. // 3) 
print(6. // 3.)
print(6.2 // 0.3)

print(6 // 4) 
print(6. // 4)

print(-6 // 4) 
print(6. // -4)



print(14 % 4)

##Як бачите, результат буде 2. І ось чому:
##■ 14 // 4 буде 3 → це ціле число, частка;
##■ 3 * 4 буде 12 → як результат множення частки на дільник;
##■ 14 - 12 буде 2 → це остача,

print(12 % 4.5)
##Відповідь: 3.0 — не 3, а 3.0 (правило все ще працює: 
##12 // 4.5 буде 2.0; 2.0 * 4.5 буде 9.0; 12 - 9.0 буде 3.0).

print(-4 + 4) 
print(-4. + 8)

print(-4 - 4) 
print(4. - 8) 
print(-1.1)

print(+2)
##
##тже, якщо ви знаєте, що у множення * вищий пріоритет, ніж у додавання +, результат має бути для вас 
##очевидним.

##. Оператори та зв'язування
print(9 % 6 % 2)
print(2 ** 2 ** 3)
print(2 * 3 % 5)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

var = 1 
print(var)

var = 1 
account_balance = 1000.0 
client_name = 'John Doe' 
print(var, account_balance, client_name) 
print(var)

var = "3.7.1" 
print("Python version: " + var)

var1 = 1
print(var1) 
var1 = var1 + 1 
print(var1) 


a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)


## x = x * 2.
## sheep = sheep + 1.
## x *= 2 
##sheep += 1

##i = i + 2 * j => i += 2 * j
##var = var / 2 => var /= 2
##rem = rem % 10 => rem %= 10
##j = j - (i + var + rem) => j -= (i + var + rem)
##x = x ** 2 => x **= 2


var = "007" 
print("Agent " + var)

##    INPUT

###1
##print("Tell me anything...") 
##anything = input() 
##print("Hmm...", anything, "... Really?"
##
####2
##anything = input("Tell me anything...") 
##print("Hmm...", anything, "...Really?")
##
##      #3
##      anything = input("Enter a number: ") 
##something = anything ** 2.0 
##print(anything, "to the power of 2 is", something)
##
##      #4
##      # [Testing TypeError message
##anything = input("Enter a number: ") 
##something = anything ** 2.0
##print(anything, "to the power of 2 i3", something)


##anything = float(input("Enter a number: ")) 
##something = anything ** 2.0
##print(anything, "to the power of 2 i3", something)

### [Testing TypeError message
##anything = input("Enter a number: ") 
##something = anything ** 2.0
##print(anything, "to the power of 2 i3", something)
##leg_a = float(input("Input first leg length: ")) 
##leg_b = float(input("Input second leg length: "))
##hypo = (leg_a*'i-2 + leg_b**2) ** .5
##        print("Hypotenuse length 13", hypo)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2)
 ** .5)

fnam = input("May I have your first name, please? ") 
lnam = input("May I have your last name, please? ") 
print("Thank you.") 
print("\nYour name is " + fnam + " " + lnam + ".")


##  * - Повторення рядка (replication)

print("james"*3)

##малюєм прямокутник
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + 
 str((leg_a**2 + leg_b**2) ** .5))

print(18 ** .5)
print(4 ** 2)
print(2 ** 2)


name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")
print("\nPress Enter to end the program.")
input()
print("THE END.")


num1 = int(input("Enter the first number: "))
num2 =int( input("Enter the second number: "))
k = num1+num2
print(k)




