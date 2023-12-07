s=input()
hashtable={}
i,res=0,0
for j in range(1,len(s)+1):
    if s[j-1] not in hashtable.keys():
        hashtable[s[j-1]]=j
    else:
        i=max(hashtable[s[j-1]],i)#max一定不能省，不然i就有可能回退了，不信可以试试abba
        hashtable[s[j-1]]=j
    res=max(res,j-i)
print(res)

# 相当于，两个指针一前一后再运动，j相当于一直在向前移动，没有重复的就加进来，res也就不断增大，如果有重复的，把i挪到重复的那个地方，
# 注意判断一下，重复的地方在不在j到i之间，在的话才需要移动i
