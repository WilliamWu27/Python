stupidthing = input("sign: ")
s = input("number of times: ")
z= int(s)
sbg = stupidthing * ((z-1)*2 + 1)
pr = ''
for k, x in enumerate(range(z)):
	pr = f'{" " * k}{sbg}\n{pr}'
	sbg = sbg[1:-1]
print(pr)