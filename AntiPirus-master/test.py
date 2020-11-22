# Fengze Wu (wu.3222)

def pentagonal_number(n):
	if n == 1:
		return 1
	else:
		return (5*n-5)+pentagonal_number(n-1)

print(pentagonal_number(4))

def encode(s):
	p = s[0]
	i = 0
	result=''
	for c in range(len(s)):
		if s[c] != p:
			result+=str(i)+p
			i = 1
			p = s[c]
		else:
			i+=1
		if c == len(s)-1:
			result+=str(i)+p
	return result
print(encode('AAAABBBCCDAA'))


def decode(s):
	result = ''
	for c in range(len(s)):
		if c%2==0:
			i = int(s[c])
		else:
			result+=i*s[c]
	return result

print(decode('4A3B2C1D2A'))

g = {"]": "[",
"}": "{",
")": "("}

def is_balanced(s): 
    stack = [] 
    for i in s: 
        if i not in g.keys(): 
            stack.append(i) 
        else:
            if ((len(stack) <= 0) or
                (g[i] != stack.pop())): 
                return False
    return len(stack) == 0
print(is_balanced("([])[]({})"))

import random 
def Monte_Carlo_Method():
	c,s=0,0
	for i in range(100000): 
	    x= random.random()-0.5
	    y= random.random()-0.5
	    dist= x**2 + y**2
	    if dist<= 0.25: 
	        c+= 1
	    s+= 1
	return 4*c/s

print(Monte_Carlo_Method())     

