import os
place = str(input("Enter your city"))
string = 'curl http://wttr.in ' + place
os.system(string)
