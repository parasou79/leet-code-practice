#Denominations {1, 2, 3}  multiple availbale
# target amt: 5

solutions = {}

def combine(tgt, dnm, soln):
	if tgt == 0:
		ans = tuple(soln)
		print(ans)
		solutions[ans]=1
		return
	tot = 0
	for x in soln:
		tot+=x
	#print('Total', tgt, tot, soln)
	for x in dnm:
		if tgt-x >= 0:
			if len(soln)==0:
				combine(tgt-x,dnm, [*soln, x])
			elif x >= soln[-1]:
				combine(tgt-x,dnm, [*soln, x])
		#else:
		#	print('Tgt', tgt, tot+x)

combine(5, (1,2,3), [])
print(len(solutions), solutions.keys())