
class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        l=[]
        for i in range(len(A)):
            s=sorted(A[i])
            s.append(i+1)
            #s=sorted(s)
            l.append(s)
        
        #print sorted(l)
        
        d={}
        
        for i in range(len(l)):
            x="".join(l[i][:-1])
            y=l[i][-1]
            if x in d.keys():
                d[x].append(y)
            else:
                d[x]=[]
                d[x].append(y)
        
        #print sorted(d.keys())
        t=[]
        for j in sorted(d.keys()):
            t.append(d[j])
        return t
        

