#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


;=======================================================================================
; Python code shortcut

::]pfi::
send, for i in range():
send, {left}{left}
return

::]pfx::
send, for x in{space}
return

; sort in ascending order
::]psort::
send, for i in range(len(lst)):{enter}
send, for j in range(i{+}1,len(lst)):{enter}{tab}
send, if lst[i] {>} lst[j]: lst[i],lst[j] {=} lst[j],lst[i]
return

; sort in descending order
::]psort1::
send, for i in range(len(lst)):{enter}
send, for j in range(i{+}1,len(lst)):{enter}{tab}
send, if lst[i] {<} lst[j]: lst[i],lst[j] {=} lst[j],lst[i]
return


::]pf::
send, print(f""){left}{left}
return


::]p::
send, print(){left}
return