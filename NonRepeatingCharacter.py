'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1. 

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

'''


class Solution(object):
    def firstUniqChar(self, s):
    	#It has a complexity of O(n^2) n is size of string
        l=list(s)
        x=-1
        for i in range(len(l)):
        	l1=l[:]
        	restart=False
        	l2=l1.pop(i)
        	#if any((True if l2==j else False for j in l1))==False:
        	for j in l1:
        		if l2==j:
        			restart=True
        			break
        	if restart==True:
        		continue

        	return i

      

        return -1 


    def firstUniqCharBetter(self, s):
    	#It has a complexity of O(2n) n is size of string
        l=list(s)
        count={}
        for i in range(len(l)):

        	if bool(count) == False or l[i] not in count:			#append the value
        		count[l[i]]=[i]
        	else:							#insert a new value
        		count[l[i]].append(i)
        
        for i in range(len(l)):
        	if len(count[l[i]])==1:
        		return count[l[i]][0]
        
        return -1       

		
x= Solution()

#print (x.firstUniqChar("leetcode"))
print (x.firstUniqCharBetter(input("Enter:")))
