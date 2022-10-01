# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))
def _multiplication_table(num):
    # Iterate 10 times from i = 1 to 10
    return [print(num, 'x', i, '=', num*i) for i in range(1,11)]

if __name__ == "__main__":
    #main()
    _multiplication_table(num)