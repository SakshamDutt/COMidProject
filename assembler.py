def imm(st):
    sti=int(st)
    ab=abs(sti)
    bst=bin(ab)
    ns=bst[2:]
    nzero=12-len(ns)
    v='0'*nzero
    pv=v+ns
    if sti>=0:
        return pv
    else:
        inv=''
        for ch in pv:
            if ch=='0':
                inv+='1'
            else:
                inv+='0'
        inv=int(inv,2)        
        inv+=1
        inv=bin(inv)
        ninv=inv[2:]
        npv=ninv[len(ninv)-12:]
        return npv 
def imm20(st):
    sti=int(st)
    ab=abs(sti)
    bst=bin(ab)
    ns=bst[2:]
    nzero=20-len(ns)
    v='0'*nzero
    pv=v+ns
    if sti>=0:
        return pv
    else:
        inv=''
        for ch in pv:
            if ch=='0':
                inv+='1'
            else:
                inv+='0'
        inv=int(inv,2)        
        inv+=1
        inv=bin(inv)
        ninv=inv[2:]
        npv=ninv[len(ninv)-20:]
        return npv
