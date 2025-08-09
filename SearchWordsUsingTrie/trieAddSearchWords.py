trie = {}

def add(trie, word, iWord, nWord):
	if iWord < nWord:
		ch = word[iWord]
		if ch not in trie:
			trie[ch]={}
		add(trie[ch], word, iWord+1, nWord)

def search(trie, word, iWord, nWord):
	if iWord < nWord:
		ch = word[iWord]
		if ch == '.':
			ans = [search(trie[x], word, iWord+1, nWord) for x in trie.keys()]
			return True in ans
		if ch not in trie:			
			return False
		search(trie[ch], word, iWord+1, nWord)
	return True

def test(cmds, words):
	for i in range(len(cmds)):
		print(cmds[i], words[i])
		cmd=cmds[i]
		word=words[i]
		if cmd=='a':
			add(trie, word, 0, len(word))
		elif cmd=='s':
			print('\t', trie)
			ans = search(trie, word, 0, len(word))
			print(ans, )
test(['a', 'a', 'a','a','s','s','s','s'], 
	['dog', 'app', 'apple', 'banana', 'apple',
	'...', '.....', 'd.g', 'c.t']
	)