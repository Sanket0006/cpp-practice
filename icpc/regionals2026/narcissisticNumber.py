from math import floor, log10, pow
def main():
    num = int(input())

    temp = num
    sum = 0

    while (temp % 10 == 0):
        temp //= 10

    newNum = 0
    lenDigit = floor(log10(num)) + 1

    while (temp > 0):
        digit = temp % 10
        sum += int(pow(digit, lenDigit))
        newNum += digit
        newNum *= 10
        temp //= 10

    while (newNum % 10 == 0):
        newNum //= 10

    print("yes") if sum == newNum else print("no") 

main()