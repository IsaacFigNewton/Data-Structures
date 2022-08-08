S = "tacocat"

def anagram (S):
    if len(S) < 2:
        return True
    
    if S[0] != S[-1]:
        return False

    return anagram(S[1:len(S)-1])

if (anagram(S)):
    print(S + " is an anagram.")
else:
    print(S + " is NOT an anagram.")
    
