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
