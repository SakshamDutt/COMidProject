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

riscv_registers={
    "zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100",
    "t0":"00101","t1":"00110","t2":"00111","s0":"01000","fp":"01000",
    "s1":"01001","a0":"01010","a1":"01011","a2":"01100","a3":"01101",
    "a4":"01110","a5":"01111","a6":"10000","a7":"10001","s2":"10010",
    "s3":"10011","s4":"10100","s5":"10101","s6":"10110","s7":"10111",
    "s8":"11000","s9":"11001","s10":"11010","s11":"11011","t3":"11100",
    "t4":"11101","t5":"11110","t6":"11111"
}
