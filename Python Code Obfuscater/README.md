# **Python Code Obfuscater**
by AbsoluteWinter  
version: 1.0.0


## **How to use**

Paste these lines in python script:
```python
import requests
SrcCode = requests.get("https://raw.githubusercontent.com/AbsoluteWinter/public-stuff/main/Python%20Code%20Obfuscater/Python%20Code%20Obfuscater.py")
exec(SrcCode.text)
```

## Code example:
```python
import requests

Src1 = "https://raw.githubusercontent.com/Absolu"
Src2 = "teWinter/public-stuff/main/Python%20Code"
Src3 = "%20Obfuscater/Python%20Code%20Obfuscater"
Src4 = ".py"
Src = Src1 + Src2 + Src3 + Src4
SrcCode = requests.get(Src)
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

### For google colab:
```python
import requests
Src1 = "https://raw.githubusercontent.com/Absolu"
Src2 = "teWinter/public-stuff/main/Python%20Code"
Src3 = "%20Obfuscater/Python%20Code%20Obfuscater"
Src4 = ".py"
Src = Src1 + Src2 + Src3 + Src4
SrcCode = requests.get(Src)
exec(SrcCode.text)

yourcode = r"""

"""

print("#Here is your obfuscated code:\n#START")
print(CodeObfuscate(yourcode))
print("\b#END")
```
