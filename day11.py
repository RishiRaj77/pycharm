def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
operaters = {
        "+" : addition,
        "-" : subtraction,
        "*" : multi,
        "/" : division
}
def calculator():
    num1 =int(input("first num = "))
    num2 =int(input("second num = "))

    for symbol in operaters:
        print(symbol)
    should_continue = True

    while should_continue:

     operation_symbol = input("pick any operation")
     calculation= operaters[operation_symbol]
     answer=calculation(num1,num2)

     print(f" {num1} {operation_symbol} {num2} : {answer}")

    if input(f" y to continue n to stop ") == "y":
        num1 = answer
    else:
        should_continue = False
    calculator()

calculator()