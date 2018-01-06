"""
there is something useful in search a substring in string
type : string
rtype : interge

Resource: LeetCode, Longest Substring Without Repeating Characters

O(n)
"""

def MaxlenthOfSubstring(s):
	start = Maxlenth = 0
	usedChar = {}
	
	for i in range(len(s)):
		if s[i] in usedChar and start <= usedChar[s[i]]:   
			start = usedChar[s[i]] + 1			# meet a repeat charcter,restting start index
		else:
			Maxlenth = max(Maxlenth, i - start + 1)
		usedChar[s[i]] = i
		
	return Maxlenth
