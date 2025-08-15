let arr = [1,2,3,4,5]
let max = arr.reduce((prev, curr) => {
	console.log(prev, curr)
	if (prev < curr) 
		prev=curr 
	return prev
})
console.log(`Max in [${arr}] is ${max}`)
