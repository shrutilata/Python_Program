def vowel_lower(S):
    for letter in S:
        letter = ord(letter)
        if(letter== 65 or letter==69 or letter==73 or letter==79 or letter==85):
            letter = letter+32
            print(chr(letter),end="")
        
        else:
            print(chr(letter),end="")
    
