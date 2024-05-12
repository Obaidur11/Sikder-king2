import  random
#Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114

ugen=[]
for snigdho in range(5):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,94)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,190)
	h='Mobile Safari/537.36'
	ua=f'{a} {b}: {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ua)  
	
	print(ugen)