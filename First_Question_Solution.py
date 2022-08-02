from ast import operator
from typing import final


class Solution:
    def add_sub(self,input):
        # Created an array of characters which needs to be ignored.
        ignore=['(',')','_',' ','']
        # Created an array of operators to be used that is addition and substraction.
        operators=['+','-']
        result_string=''

        arr_final=[]
        temp=''

        # Putting values which are not in ignore array in result_string. 
        for i in range (len(input)):
            if input[i] not in ignore:
                result_string=result_string+input[i]

        #Printing result_string
        print (result_string)

        #In order to perform operations easily. Putting data into array.
        #First Push data into result_string. If operator found in a string then push data from temp and operator into array.
        for i in range (len(result_string)):
            if result_string[i] not in operators:
                temp=temp+result_string[i]
            else:
                if len(temp)>0:

                    arr_final.append(temp)
                arr_final.append(result_string[i])
                temp=''
        if(len(temp)>0):
            arr_final.append(temp)

        #If operators are present at end, return Invalid String.
        if arr_final[-1]=='+' or arr_final[-1]=='-':
            return "Invalid String."

        #Operator Adjustment:
        #if + and - are adjacent characters or - and + are adjacent characters then keep -.
        #if - and - are adjacent charcaters then insert +.
        #if + and + are adjacent characters then insert +.
        for i in range (len(arr_final)):
            if (arr_final[i]=='+' and arr_final[i+1]=='-') or (arr_final[i]=='+' and arr_final[i+1]=='+'):
                #['200', '+', '-', '100500', '+', '10000', '+'] => ['200', '-', '100500', '+', '10000', '+']
                arr_final[i]=''
            elif (arr_final[i]=='-' and arr_final[i+1]=='-'):
                arr_final[i+1]=''
                arr_final[i]='+'
            elif (arr_final[i]=='-' and arr_final[i+1]=='+'):
                arr_final[i+1]=''

        #To get numbers and operators from the array.
        arr_final_new=[]
        for i in range (len(arr_final)):
            if arr_final[i] not in ignore:
                arr_final_new.append(arr_final[i])


        #Condition to ignore operators and numbers greater than 100,000,000 before converting to integer.
        for i in range (len(arr_final_new)):
            if (arr_final_new[i] != "-"):
                if (arr_final_new[i] != "+"):
                    arr_final_new[i]=int(arr_final_new[i])
                    if(arr_final_new[i] > 100_000_000):
                        return "Number exceeds Given Limit, Exiting program."

        #Evaluate the value of expression
        Output = eval(' '.join(str(x) for x in arr_final_new))
  
        # Printing output
        print("Initial list", arr_final_new)
        print("Answer after solving list is:", Output)

        #Returning output as a String
        return str(Output)

if __name__=="__main__":
    obj=Solution()
    cont = 'y'
    while cont == 'y' or cont != 'Y':
        cont = input('Do you wish to Enter String(Y/N): ')
        if cont == 'y' or cont== 'Y':
            input_string=input("Please Enter String: ")
            print(obj.add_sub(input_string))
        else:
            break

        #Test Cases


        #print(obj.add_sub(input = '200 + ((-100500 + 10000) + 2000)') == '-88300')     #True
        # print(obj.add_sub(input = '-200 + ((-100500 + 10000) + 2000)') == '-88700')   #True
        # print(obj.add_sub(input = '200 + ((-100_500 + 100_00) + 20_00)') == '-88300') #True
        # print(obj.add_sub(input = '200 + ((-100_500 + 100_00) + 20_00 + )'))          #Invalid String
        # print(obj.add_sub(input = '- 200 + ((-100_500 + 100_00) + 20_00)') == '-88700')   #True

        
