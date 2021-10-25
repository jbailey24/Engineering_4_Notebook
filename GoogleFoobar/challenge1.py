x = input("Enter the gibberish ")   # remove line to submit

def solution(x):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    output = ""                                 # creates empty output string
    
    for i in x:                                 # checks every letter in the input
        if i in alphabet:                       # if it is in the alphabet (aka is a lowercase letter) 
            inputindex = alphabet.index(i)      # finds index of letter
            outputindex = 25 - int(inputindex)  # finds inverse index
            j = alphabet[outputindex]           # finds letter at inverse index
        else:
            j = i                               # if uppercase, puncuation, number, etc, just returns input unchanged
        output = output + str(j)                # sequentially adds outputs to string
    return(output)                              # returns output
    
solution(x)                     # remove line to submit
