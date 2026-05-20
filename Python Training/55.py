# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

import re

n = input("Enter a value := ") 

result = re.findall(r"\w+\@\w+\.com",n) 

if result:
    a = re.findall(r"@(\w+)",n)
    print(a) 
else:
    print("format of email is wrong ")  