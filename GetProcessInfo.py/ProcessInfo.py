#Utility to display the memory occupied by a process
import os, sys

_processes =os.popen('ps aux')
_userName=os.getlogin()
#print os.getlogin
print "User That  has logged in", os.getlogin()

_message="Do you want to Display Information About",_userName
option=raw_input(_message)
#Experimenting with Control Flow Statements

if option == 'yes':
    print "Yes"
    #Get System Information
    _osName=os.name
    print _userName," has ", _osName,sys.platform,os.uname()
    
    
    
    
else:
    print "Bye Bye"
    
