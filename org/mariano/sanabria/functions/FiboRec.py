def fibRec(n):
    if n is 0:
    	return 0
    elif n is 1:
    	return 1
    else:
    	return fibRec(n-1) + fibRec(n-2)
