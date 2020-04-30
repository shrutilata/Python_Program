#Source Code:--

def vowel_upper(S):
    for letter in S:
        letter=ord(letter)
        if(letter==97 or letter==101 or letter==105 or letter==111 or letter==117):
            letter = letter - 32
            print(chr(letter),end="")
        
        else:
            print(chr(letter),end="")
            
#Driver Code:--
vowel_upper("i am shruti")

#Output:--
I Am shrUtI

