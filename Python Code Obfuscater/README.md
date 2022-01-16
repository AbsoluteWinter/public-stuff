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

## **Code example:**

### Setup
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


### Test run:
```python
import requests
SrcCode = requests.get("https://raw.githubusercontent.com/AbsoluteWinter/public-stuff/main/Python%20Code%20Obfuscater/Python%20Code%20Obfuscater.py")
exec(SrcCode.text)
mycode = r"""
print("Hello")
"""
print(CodeObfuscate(mycode))
```
```python
# Output:
exec('\x69\x6d\x70\x6f\x72\x74\x20\x62\x61\x73\x65\x36\x34')
VrCxIdVkOQsn='ZXhlYygnXHg2OVx4NmRceDcwXHg2Zlx4NzJceDc0XHgyMFx4NjJceDYxXHg3M1x4NjVceDM2XHgzNFx4'
rRjWulSWLsoB='MjBceDYxXHg3M1x4MjBceDRkXHg2Mlx4NTlceDYxXHg0Ylx4NzFceDRiXHg0OFx4NDdceDUzXHg2ZFx4'
NVFsqIhyskJA='MmNceDYzXHg2Zlx4NjRceDY1XHg2M1x4NzNceDIwXHg2MVx4NzNceDIwXHg2MVx4NTRceDVhXHg3N1x4'
XclmZjgXPGTC='NjRceDU3XHg2ZFx4NjRceDU4XHg3Nlx4NGNceDJjXHg3YVx4NmNceDY5XHg2Mlx4MjBceDYxXHg3M1x4'
GBBrovGWqhfP='MjBceDRjXHg2Ylx4NmFceDY4XHg0OVx4NzdceDc3XHg3OVx4NTBceDU4XHg1MScpCkRQb0RNTFFjZkhu'
SoGwTtpEQgNm='bj0ncldrbW1hQmRHTicKTXlPaXF1d3JKcmVyPSdqM0FzTzI5aVhaJwpPQ2NvZ1JyYkRTWlE9J1BkOGJH'
nXijlZgwjaTc='ZGUwWVUnCk9OQkp1bU94b2h5Uz0nT0JnN0hTTlRaTScKTEFhSHhJaVVxR3hRPSdPLzg9JwpwYkhRRWNk'
tQViXvulPUAY='UHlJTGs9RFBvRE1MUWNmSG5uK015T2lxdXdySnJlcitPQ2NvZ1JyYkRTWlErT05CSnVtT3hvaHlTK0xB'
ZOHxTAsvsrmD='YUh4SWlVcUd4UQpZVklBVURpYlV5Y2tMdk09ZXZhbCgnXHg2Mlx4NjFceDczXHg2NVx4MzZceDM0XHgy'
RGtTyBELfrOS='ZVx4NjJceDM2XHgzNFx4NjRceDY1XHg2M1x4NmZceDY0XHg2NVx4MjhceDI3XHg2M1x4NmRceDM5XHgz'
NJFNIlTUkipH='MFx4NThceDdhXHg0NVx4N2FceDI3XHgyZVx4NjVceDZlXHg2M1x4NmZceDY0XHg2NVx4MjhceDI5XHgy'
beaUVKlPHSdL='OScpLmRlY29kZSgpCkhaeFlKTWRRaWZXYVJpaz0nXHgzY1x4NzNceDc0XHg3Mlx4NjlceDZlXHg2N1x4'
JNQnoHUfzdTY='M2UnCllGYURHcGV6ZXdyZ0pBUj0nXHg2NVx4NzhceDY1XHg2MycKZXhlYygnXHg2NVx4NzZceDYxXHg2'
EixdsodwZYBN='Y1x4MjhceDYzXHg2Zlx4NmRceDcwXHg2OVx4NmNceDY1XHgyOFx4NGRceDYyXHg1OVx4NjFceDRiXHg3'
rJBkRqhvJSZv='MVx4NGJceDQ4XHg0N1x4NTNceDZkXHgyZVx4NjJceDM2XHgzNFx4NjRceDY1XHg2M1x4NmZceDY0XHg2'
GLeEHnosATPv='NVx4MjhceDRjXHg2Ylx4NmFceDY4XHg0OVx4NzdceDc3XHg3OVx4NTBceDU4XHg1MVx4MmVceDY0XHg2'
LoylpQCghHoL='NVx4NjNceDZmXHg2ZFx4NzBceDcyXHg2NVx4NzNceDczXHgyOFx4NGRceDYyXHg1OVx4NjFceDRiXHg3'
UluZNVNJGsdT='MVx4NGJceDQ4XHg0N1x4NTNceDZkXHgyZVx4NjJceDM2XHgzNFx4NjRceDY1XHg2M1x4NmZceDY0XHg2'
HrkaCUmzIDMX='NVx4MjhceDYxXHg1NFx4NWFceDc3XHg2NFx4NTdceDZkXHg2NFx4NThceDc2XHg0Y1x4MmVceDY1XHg2'
fQeFQRrCoUby='ZVx4NjNceDZmXHg2NFx4NjVceDI4XHg3MFx4NjJceDQ4XHg1MVx4NDVceDYzXHg2NFx4NTBceDc5XHg0'
dzAebtiWoxSE='OVx4NGNceDZiXHgyY1x4NTlceDU2XHg0OVx4NDFceDU1XHg0NFx4NjlceDYyXHg1NVx4NzlceDYzXHg2'
KIFMfKYTClSV='Ylx4NGNceDc2XHg0ZFx4MjlceDJlXHg2NVx4NmVceDYzXHg2Zlx4NjRceDY1XHgyOFx4MjlceDI5XHgy'
TCmgNnIpvhCR='OVx4MjlceDJjXHg0OFx4NWFceDc4XHg1OVx4NGFceDRkXHg2NFx4NTFceDY5XHg2Nlx4NTdceDYxXHg1'
tJqEzAcXvOtA='Mlx4NjlceDZiXHgyY1x4NTlceDQ2XHg2MVx4NDRceDQ3XHg3MFx4NjVceDdhXHg2NVx4NzdceDcyXHg2'
JhENpayikiFo='N1x4NGFceDQxXHg1Mlx4MjlceDI5JykK'
mZGxLreneNWN=VrCxIdVkOQsn+rRjWulSWLsoB+NVFsqIhyskJA+XclmZjgXPGTC+GBBrovGWqhfP+SoGwTtpEQgNm+nXijlZgwjaTc+tQViXvulPUAY+ZOHxTAsvsrmD+RGtTyBELfrOS+NJFNIlTUkipH+beaUVKlPHSdL+JNQnoHUfzdTY+EixdsodwZYBN+rJBkRqhvJSZv+GLeEHnosATPv+LoylpQCghHoL+UluZNVNJGsdT+HrkaCUmzIDMX+fQeFQRrCoUby+dzAebtiWoxSE+KIFMfKYTClSV+TCmgNnIpvhCR+tJqEzAcXvOtA+JhENpayikiFo
RFoTpgUGddZsMuf='\x3c\x73\x74\x72\x69\x6e\x67\x3e'
STgbGnvqnJSyLbX='\x65\x78\x65\x63'
eval(compile(base64.b64decode(mZGxLreneNWN),RFoTpgUGddZsMuf,STgbGnvqnJSyLbX))
```
