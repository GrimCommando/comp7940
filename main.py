def print_factor(x):
    print(x)
    
def main():
    # Find the all factors of x using a loop and the operator % 
    # % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
    x = 52633
    i=0
    f=0
    for i in range(x+1):
    # your code here
        if i == x:
            break
        i=i+1
        f = x % i
        print_factor(f)

if __name__ == '__main__':
    main()
    
