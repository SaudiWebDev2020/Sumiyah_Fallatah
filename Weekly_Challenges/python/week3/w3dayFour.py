# Is Palindrome
# --------------------------------------------------------------------------------
# Strings like "Able was I, ere I saw Elba" or "Madam, I'm Adam" could be considered palindromes, because (if we ignore spaces, punctuation and capitalization) the letters are the same from front and back. Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.
# racecar
def remove_blanks(text):
    new_string= ""
    for char in text:
        if char != " " and char != "'" and char != ",":
            new_string += char
    return new_string

def palindrome(text):
    # i = 0 
    text = remove_blanks(text)
    text.upper()
    print(text)
    j = len(text)-1
    
    for x in range (0, len(text)):
        if text[x] != text[j]:
            return False
        else:
            return True

print(palindrome('racecar'))
print(palindrome('able was I ere I saw elba'))
print(palindrome("Madam, I'm Adam"))


# Longest Palindrome
# --------------------------------------------------------------------------------
# For this challenge, we will look not only at the entire string, but also substrings within it. For a string, return the longest palindromic substring. Given "what up, dada?", return "dad". Given "not much", return "n". Include spaces as well (i.e. be strict, as in the “Is Palindrome” challenge): given "My favorite racecar erupted!", return "e racecar e".
