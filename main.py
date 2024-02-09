#REMOVE PASS AND FIX THIS FUNCTION
def anagram(input1,input2):
    if input1 or input2 == ' ':
        return False
    
    input1 = input1.upper().strip()
    input1_split = list(input1)
    
    for i in input1_split:
        if i == ' ':
            input1_split.remove(i)
        else:
            continue
 
    input2 = input2.upper().strip()
    input2_split = list(input2)

    for i in input2_split:
        if i == ' ':
            input2_split.remove(i)
        else: continue

    for i in input1_split:
        if i in input2_split:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    input1 = input()
    input2 = input()
    print(anagram(input1,input2))
    