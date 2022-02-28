import json
import requests

def debug(x):
    # Debug
    #print("Debug")
    for i in x:
        print("parse " + str(i))

def convert_number(x):
    #convert number
    number_list=[]
    number_list = [x[0],int(x[1]),int(x[2]),int(x[3])]
    #print("convert number")
    return(number_list)
    
def replace_number(number_list, being_replace, to_replace):
    #replace number
    #number_list=number_list.pop
    replace_list=[]
    replace_list = [to_replace if item == being_replace else item for item in number_list]
    #print("replace number")
    return replace_list
        
def main():
    
    # Write the functions convert_number and replace_number here
    # Follow the logic below.
    site="https://api.npoint.io/2b57052af2060e84dc86"


    # Trying to load JSON into text
    r = requests.get(site)
    print(r.json())
    text = r.json()['users']
    
    debug(text)
    
    # call the function convert_number
    # convert all elements (except the first one) into number and return it as a list
    y = convert_number(text[0]) 
    #z = convert_number(text[1])
    print("y")
    print(y)
    
    # call the function replace_number
    # replace all number 1 by the number 10 in the function
    z = replace_number(number_list = y, being_replace = 1, to_replace = 10)

    print("z")
    print(z)

    sum = 0
    for i in z:
        if type(i) != str:
            #print(i)
            sum = sum + i
            print("sum = " + str(sum) + "; i =" + str(i))
    print ("Total = " + str(sum))

if __name__ == '__main__':
    main()
    
    
