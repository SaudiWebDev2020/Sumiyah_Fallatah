# Remove Blanks
#---------------------------------------------------------------------------------------------
# Create a function that, given a string, returns the string, without blanks. Given " play that
# Funky Music ", returns a string containing "playthatFunkyMusic".
word = " play that Funky Music "
def removeBlanks(x):
    z = []
    for i in range (0, len(x), 1):
        if x[i] != " ":
            z.append(x[i])
            # print(z)
    return ''.join(z)
print(removeBlanks(word))





# Get String Digits
#---------------------------------------------------------------------------------------------
# Create a JavaScript function that given a string, returns the integer made from the string’s
# digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1,357,924,680.

x = "0s1a3y5w7h9a2t4?6!8?0"
def getdigit(x):
    my_list = []
    for i in range (0, len(x), 1):
        z= int(x[i])
        y = isinstance(z,int)
        if y == True:
            my_list.append(x[i])
            print(my_list)
    # return ''.join(z)
print(getdigit(x)) #simply wont work... 

# Acronyms
#---------------------------------------------------------------------------------------------
# Create a function that, given a string, returns the string’s acronym (first letters only,
# capitalized). Given "there's no free lunch - gotta pay yer way", return "TNFL-GPYW". Given
# "Live from New York, it's Saturday Night!", return "LFNYISN".

def acronym(y):
    for y in range (0,len(y),1):

