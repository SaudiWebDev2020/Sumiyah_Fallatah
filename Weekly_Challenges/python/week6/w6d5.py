# stringAnagrams
# ----------------------------------------------------------------------------------------------------
# Given a string, return an array where each element is a string representing a different anagram (a different sequence of the letters in that string). Example: if given "tar", return ["art", "atr", "rat", "rta", "tar", "tra"]. For this challenge, you can use built-in string functions such as split().

def stringAnagrams(str_input, temp ='', result=None):
    if result = None:
        result = []
    
# gunicorn user_project.wsgi

# [Unit]
# Description=gunicorn daemon
# After=network.target
# [Service]
# User=ubuntu
# Group=www-data
# WorkingDirectory=/home/ubuntu/Stack-Project
# ExecStart=/home/ubuntu/Stack-Project/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/Stack-Project/user_project.sock user_project.wsgi:application
# [Install]
# WantedBy=multi-user.target

# server {
#   listen 80;
#   server_name 18.218.245.254;
#   location = /favicon.ico { access_log off; log_not_found off; }
#   location /static/ {
#       root /home/ubuntu/Stack-Project;
#   }
#   location / {
#       include proxy_params;
#       proxy_pass http://unix:/home/ubuntu/Stack-Project/user_project.sock;
#   }
# }

# sudo ln -s /etc/nginx/sites-available/user_project /etc/nginx/sites-enabled

def stringAnagrams(string_input,temp="",result=None):
    if result == None:
        result = []
    if len(string_input) > 0:
        for i in range (len(string_input)):
            stringAnagrams(string_input[0:i]+string_input[i+1:len(string_input)],temp + string_input[i],result)
    else:
        # print(temp)
        result.append(temp)
    return result

def stringAnagrams2(string_input,place_hold="",temp="",index=0,result=None):
    print(string_input,temp,index)
    if result == None:
        result = []
        place_hold = string_input
    
    if len(string_input) > index:
        stringAnagrams2(string_input, place_hold[0:index]+place_hold[index+1:len(place_hold)],temp + string_input[index],index + 1,result)
    else:
        print(temp)
        result.append(temp)
        
    return result
        
        
        
        
print(stringAnagrams('abc'))
# print(len(stringAnagrams2('abc')))