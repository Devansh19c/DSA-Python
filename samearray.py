# class solution:
#     def check(self,A,B,N):
#         A=[1,2,3,4,5]
#         B=[1,2,3,5,6]

#         A=list(set(A))
#         B=list(set(B))
#         for i in range(0,len(A)-1,1):
#             if A[i]==B[i]:
#                 return 1
#             else:
#                 return 0
        

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        # A=list(set(A))
        # B=list(set(B))
        A.sort()
        B.sort()
        if A==B:
            return 1
        else:
            return 0



