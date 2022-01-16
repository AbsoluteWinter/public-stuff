# **Python Code Obfuscater**
by AbsoluteWinter  
version: 1.0.0


# **How to use**

Paste these lines in python script:
```python
import requests
SrcCode = requests.get("https://raw.githubusercontent.com/AbsoluteWinter/public-stuff/main/Python%20Code%20Obfuscater/Python%20Code%20Obfuscater.py")
exec(SrcCode.text)
```

Code example:
```python
import requests

SrcCode = requests.get("https://raw.githubusercontent.com/AbsoluteWinter/public-stuff/main/Python%20Code%20Obfuscater/Python%20Code%20Obfuscater.py")
exec(SrcCode.text)
#COhelp() # help function


# Input code that want to obfuscate
yourcode = r"""
# put your code in here
# in order to obfuscate
"""

# Run function
obfus = CodeObfuscate(yourcode)


# write to .txt file
txtfile = open("obfuscated_code.txt","w")
txtfile.writelines(obfus)
txtfile.close()
```