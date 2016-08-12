import sys
import os

def Task(query_string):
	os.chdir('./tasks')
	query_string = query_string.replace(' ','\ ')
	os.system('python3 '+query_string+'.py')
	os.chdir('..')

a = ['amazon' , 'alarm']
b = ['battery']
c = ['calendar', 'calculator','caffe','contacts']
d = ['document','dropbox']
e = ['explorer','ebay']
f = ['facebook' , 'flipkart', 'fortune']
g = ['google','google drive', 'gmail', 'google plus','git']
h = ['hungry','help']
i = []
j = ['joke']
k = []
l = ['location']
m = ['mahjong','map', 'music', 'movie']
n = ['news']
o = ['office']
p = ['power','pocket']
q = ['quora']
r = ['restaurant']
s = ['sudoku','shutdown','snapdeal']
t = ['terminal', 'torrent', 'trash', 'text editor','twitter']
u = ['ubuntu', 'unmount']
v = ['volume', 'vlc']
w = ['weather', 'web browser']
x = ['wifi', 'wikipedia']
y = ['youtube']
z = []

dic = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
List = []
## Recieve String Input from the voice recognizer program.
for i in range(1,len(sys.argv)):
	List.append(sys.argv[i])

string = ''
for l in List:
	string += str(l) + ' '
string.rstrip()

"""
def Show(char):
	try:
		try:
			print(dic[ord(char)-97])
		except IndexError:
			print('Query Not Found')
	except TypeError:
		print('Please Enter a char value')
"""
condition = False

str(string)

"""
print(List)
print(string)
"""

for i in List:
	if ord(i[0])-97 < 0:
		condition = False
		break
	else:
		order = ord(i[0])-97
		if i in dic[order]:
			condition = True
			Task(i)
			break
		else:
			pass
if condition == False:
	string = string.replace(' ','\ ')
	os.system('firefox --search '+string)

