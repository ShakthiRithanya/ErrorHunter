# Find the Largest Number: Accept two numbers and print the larger one.
def largest_of_two(a, b):
    if a > b:
        print(num1,"is greater")
        return a  
    else:
        print(num2,"is greater")
        return b
if __name__ == "__main__":
    num1 = int(input("Enter the First Number :"))
    num2 = int(input("Enter the Second Number :"))
    res = largest_of_two(num1,num1)
    print(res)
largest_of_two()