# Book Index
# ------------------------------------------------------------------------
# Write a function that given a sorted array of page numbers, return a string representing a book index. Combine consecutive pages to create ranges. Given 
# [1, 3, 4, 5, 7, 8, 10], return the string "1, 3-5, 7-8, 10".
def bookIndex(num_string):
    var = "" 
    string_x = ""
    for x in range (0, len(num_string)-1):
        if (num_string[x]-(num_string[x+1])) != 1:
            string_x += str(num_string[x])
            print(num_string[x+1])
            print(string_x + ',')
            # print(num_string[x]+1)
        # elif num_string[x+1] == (num_string[x]+1):
        #     print(num_string[x+1])
        #     print(num_string[x]+1)
        #     var = num_string[x+1]
        # else: 
        #     string_x += str(num_string[x])
        #     string_x += str(var) 


    return string_x

print(bookIndex([1, 3, 4, 5, 7, 8, 10]))




# Common Suffix
# ------------------------------------------------------------------------
# When given an array of words, returns the largest suffix (word-end) that is common between all words. For example, for input ["ovation", "notation", "action"], return "tion". Given ["nice", "ice", "sic"], return "".
