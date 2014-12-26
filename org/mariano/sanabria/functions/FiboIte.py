#Modulo FiboIte.py
def fibIte(n):
    a=0
    b=1
    if n is 0:
    	return 0
    elif n is 1:
    	return 1
    else:
    	for i in range(2, n+1):
    		c=a+b
    		a=b
    		b=c
    	return b
