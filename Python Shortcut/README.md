# **Python typing shorcut**

Here is the list:

```ahk
::]pfi::
send, for i in range():
send, {left}{left}
return

::]pfx::
send, for x in{space}
return

::]pf::
send, print(f""){left}{left}
return

::]p::
send, print(){left}
return

::]main::
send, if __name__ == "__main__":{ENTER}pass
return
```