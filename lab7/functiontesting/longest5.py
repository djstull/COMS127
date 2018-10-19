def longest_run(s): 
    l={}
    for ch in s:
        if ch in l.keys():l[ch]+=1
        else:l[ch]=1
    m=0;j=""
    for k in s:
        if l[k]>m:m=l[k];j=k
    return m*j