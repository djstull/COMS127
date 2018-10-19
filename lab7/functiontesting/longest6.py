def longest_run(s):
    t=mt=c=m=1;i=2;l=len(s)
    while i<l:
        k=c+1-min(abs(ord(s[i])-ord(s[t])),1)
        if k==c:t=i;c//=c 
        else:c=k
        i+=1
        if c>m:m=c;mt=t      
    return s[mt:mt + m]