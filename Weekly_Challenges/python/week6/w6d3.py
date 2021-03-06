# Binary String Expansion
# ---------------------------------------------------------------------------------
# You will be given a string containing characters ‘0’, ‘1’, and ‘?’. For every ‘?’, either ‘0’ or ‘1’ characters can be substituted. Write a recursive function that returns an array of all valid strings that have ‘?’ characters expanded into ‘0’ or ‘1’.
# Ex.: binStrExpand("1?0?") should return ["1000","1001","1100","1101"]. For this challenge, you can use string functions such as slice(), etc., but be frugal with their use, as they are expensive.

# def binStrExpand(string):
#     q='?'
#     i=0
#     if q not in string:
#         return 
#     else: 
        
#         if q in string[i] and q=1:
            
#             q = int(q)
#             string[i].append(q)

#         elif q in string[i+1] and q=0:
#             q = int(q)
#             string[i].append(q)
#         return binStrExpand(string[i+1])

# print(binStrExpand("1?00"))

def binStrExpand(input_str,index=0,return_list=None):
    if return_list==None:
        return_list=[]
    if len(input_str) == index:
        return return_list
    elif len(return_list) == 0:
        if input_str[index] == '0' or input_str[index] == '1':
            return_list.append(input_str[0:index+1])
            index += 1
            return binStrExpand(input_str,index,return_list)
        else:
            return_list.append('0')
            return_list.append('1')
            index += 1
            return binStrExpand(input_str,index,return_list)
    else:
        if input_str[index] == '0' or input_str[index] == '1':
            for it in range (len(return_list)):
                # print('Here',return_list,input_str[index])
                return_list[it] = f"{return_list[it]}{input_str[index]}"
            index += 1
            return binStrExpand(input_str,index,return_list)
        else:
            newList = []
            for it in range (len(return_list)):
                newList.append(f"{return_list[it]}0")
                # print('--', return_list)
                newList.append(f"{return_list[it]}1")
                # print('**', return_list)
            # prints('.*.', binStrExpand(input_str,index,newList))
            index += 1
            # print('...', binStrExpand(input_str,index,newList))
            return binStrExpand(input_str,index,newList)
        
# if __name__ == "__main__":
print(binStrExpand("??"))
print(binStrExpand("1?0?"))
# print('*'*30)
print(binStrExpand("??"))