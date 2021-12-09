def mreplace(s,r,rw):
    if not isinstance(s,str):
        print('s should be str')
    if(isinstance(r,list) and isinstance(rw,list)):
        for i in range(0,len(r)):
            s = s.replace(str(r[i]),str(rw[i]))
    elif(isinstance(r,str) and isinstance(rw,str)):
        s =  s.replace(r,rw)
    elif(isinstance(r,list) and isinstance(rw,str)):
        for c in r:
            s = s.replace(c,rw)
    return s