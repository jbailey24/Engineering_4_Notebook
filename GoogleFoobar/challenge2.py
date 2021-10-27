# l is the input list of unsorted strings

def solution(l):
    string = ""                      # defines string, output, and fin_output variables
    output = []
    fin_output = []
    
    for i in l:                      # this for loop sorts the input (does the magic)        
        m = i.split(".")             # splits each element in the list at the decimal
        for j in range(0, len(m)):   # turns strings from split list into integers
            m[j] = int(m[j])
        output.append(m)             # appends all elements together
        
    for j in sorted(output):         # this for loop turns sorted list back into form needed to submit
        for k in j:
            string = string + str(k) +    
        fin_output.append(string[:-1])
        string = ""
        
    return(fin_output)
