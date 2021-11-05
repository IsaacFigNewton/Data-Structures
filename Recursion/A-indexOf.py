"""
#Non-recursive way
def indexOf (string, substring):
    #mainChars = string.split()
    #searchChars = substring.split()
    startIndex = -1
    tempLocation = -1
    foundSubstringStart = False
    for i in range(len(string)):
        #Check if the current character in the main string matches the first one in the substring
        #and it's not currently checking the main string against the substring
        if (not foundSubstringStart and string[i] == substring[0]):
            foundSubstringStart = True
            tempLocation = i
        #If the first character of the substring matches one in the main string
        if (foundSubstringStart):
            #Make sure that the strings don't start to get compared outside of the substring's length
            if (i-tempLocation < len(substring)):
                #Compare each character in the substring with the respective character in the main string and
                #if they're not the same, say that the substring wasn't found
                if (string[i] != substring[i-tempLocation]):
                    foundSubstringStart = False
                    i = tempLocation + 0
                    tempLocation = -1
            #If the substring was found and the program sucessfully searched all the respective characters in
            #the main string without quitting, assume that it found the substring and break
            else:
                break;
    return tempLocation
"""

#Recursive way
def indexOf(mainstr,substr, currentIndex):
    #Termination case
    if (len(mainstr) < len(substr)):
        return -1
    #If the substring is found, return the index at which it was found
    if (mainstr[0: len(substr)] == substr):
        return currentIndex
    #Otherwise, call the fundction again
    else:
        currentIndex += 1
        return indexOf(mainstr[1: len(mainstr)], substr, currentIndex)

def runTestCases():
    mainString = "This is a string"

    #This should return 0
    substring = "This"
    indexOfSubstring = str(indexOf(mainString, substring, 0))
    print("Found substring \"" + substring + "\" in \"" + mainString + "\" at index " + indexOfSubstring)

    #Should return 5
    substring = "is a"
    indexOfSubstring = str(indexOf(mainString, substring, 0))
    print("Found substring \"" + substring + "\" in \"" + mainString + "\" at index " + indexOfSubstring)

    #Should return 10
    substring = "string"
    indexOfSubstring = str(indexOf(mainString, substring, 0))
    print("Found substring \"" + substring + "\" in \"" + mainString + "\" at index " + indexOfSubstring)

    #Should return -1
    substring = "."
    indexOfSubstring = str(indexOf(mainString, substring, 0))
    print("Found substring \"" + substring + "\" in \"" + mainString + "\" at index " + indexOfSubstring)

if __name__ == "__main__":
    runTestCases()