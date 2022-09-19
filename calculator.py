def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def substract(n1, n2):
    return n1 - n2


operators = {
    "/": divide,
    "*": multiply,
    "+": add,
    "-": substract,

}

listcalcul = []
continuecalcul = True
while continuecalcul:
    num1 = int(input("Enter the number1 please: "))
    num2 = int(input("Enter the number2 please: "))
    for operator in operators:
        print(operator)
    operatorchoice = input("Enter the operator please: ")
    calcul = operators[operatorchoice]
    result = calcul(num1, num2)
    print(f"{num1} {operatorchoice} {num2} = {result}")
    listcalcul.append(result)
    choicetocontinue = input("tape yes to continue")
    if choicetocontinue == "no":
        continuecalcul = False

print(listcalcul)