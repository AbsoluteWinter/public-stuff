# **Python Code Obfuscater**
by AbsoluteWinter  
version: 1.0.0


# **How to use**

```{python}
import requests
SrcCode = requests.get("https://raw.githubusercontent.com/AbsoluteWinter/public-stuff/main/Python%20Code%20Obfuscater/Python%20Code%20Obfuscater.py")
exec(SrcCode.text)
```
