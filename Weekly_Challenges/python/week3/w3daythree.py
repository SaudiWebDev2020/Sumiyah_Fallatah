# Parens Valid
# ----------------------------------------------------------------------------------------
# Create a function that, given an input string, returns a boolean whether parentheses in that string are valid. Given input "y(3(p)p(3)r)s", return true. Given "n(0(p)3", return false. Given "n)0(t(0)k", return false.

def valid_p (word):
    count = 0
    for i in range ( len(word)):
        if word[i] == '(':
            # open.append(word[i])
            count+= 1
            print(count)
        elif word[i] == ')':
            # close.append(word[i])
            # print(close)
            count+= -1
            print(count)
    
    if count < 0:
        return False
    elif count == 0:
        return True

    # if len(open) == len(close):
    #     return True
    # elif len(open) != len(close):
    #     return False

print(valid_p("y(3(p)p(3)r)s"))
print(valid_p("n(0(p)3"))
print(valid_p("n)0(t(0)k"))  # tried 2 ways both give true in this case 


# Braces Valid
# ----------------------------------------------------------------------------------------
# Given a string, returns whether the sequence of various parentheses, braces and brackets within it are valid. For example, given the input string "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!", return true. Given "d(i{a}l[t]o)n{e", return false. Given "a(1)s[O(n]0{t)0}k", return false.

def valid_b(word):
    a=0 b=0 c=0
    for i in range (len(word)):
        if word[i] == '(':
            a=a+1
        if word[i] == '[':
            b=b+1
        if word[i] == '{':
            c=c+1
        if word[i] == ')':
            a=a-1
        if word[i] == ']':
            b=b-1
        if word[i] == '}':
            c=c-1

    