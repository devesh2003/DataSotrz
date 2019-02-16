text = input('Enter a string : ')

dict = "a,z,x,s,w,q,e,d,c,v,f,r,t,g,b,n,h,y,m,j,u,k,l,p,o,i"

for char in text:
	index = dict.find(char)
	print(index)
