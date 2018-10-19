def longest_run(s): 
    t=mt=0;c=m=i=1;l=len(s)
    while i<l-1: 
        k=c+1-min(abs(ord(s[i])-ord(s[t])),1)
        if k==c:t=i;c//=c 
        else:c=k
        i+=1
        if c > m:m=c;mt=t      
    return s[mt:mt + m] 