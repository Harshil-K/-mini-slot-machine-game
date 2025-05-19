#pylint: skip-file

import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3


symbolCount = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}


symbolValues = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def checkWinnings(columns, lines, bet, values):

    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbolToCheck = col[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
    
    return winnings, winningLines


#Get the items that will be in the slot machine
def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        #Deep copy
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

#Helps print all the rows for the slot machine
def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if(i != len(columns) - 1):
                print(column[row], end = " | ")
            else:
                print(column[row], end = "\n")

#Function collects user input that gets the deposit from the user
def deposit():
    while True:
        try:
            amount  = int(input("Enter an amount to deposit: $"))
            if(amount > 0):
                break
            else:
                print("Invalid input. Please enter a number greater than 0")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return amount

#Get the number of lines the user wants to bet on
def getNumberOfLines():
    while True:
        try:
            lines = int(input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? "))
            if(1 <= lines <= MAX_LINES):
                break
            else:
                print("Invalid input. Enter a valid number of lines.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

    return lines    

#Get the amount the user wants to bet
def getBet():
    while True:
        try:
            amount = int(input(f"Enter the amount between ${MIN_BET} and ${MAX_BET} you would like to bet. $"))
            if(MIN_BET <= amount <= MAX_BET):
                break
            else:
                print(f"Please enter a number between ${MIN_BET} and ${MAX_BET}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return amount

def spin(balance):
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"You do not have enough balance to bet ${totalBet}. Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}")
    
    slots = getSlotMachineSpin(ROWS, COLS, symbolCount)

    printSlotMachine(slots)

    winnings, winningLines = checkWinnings(slots, lines, bet, symbolValues)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winningLines)

    return winnings - totalBet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")

        if balance ==  0:
            print("Thank you for playing. You do not have any more money to bet.")
            print()
            break

        answer = input("Press enter to play or Q/q to quit: ")

        if answer == "q" or answer == "Q" :
            break
        balance += spin(balance)


main()
