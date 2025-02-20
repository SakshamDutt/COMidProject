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
        
rtype={'add':{'funct7':'0000000','func3':'000','opcode':'0110011'},
       'sub':{'funct7':'0100000','func3':'000','opcode':'0110011'},
       'slt':{'funct7':'0000000','func3':'010','opcode':'0110011'},
       'srl':{'funct7':'0000000','func3':'101','opcode':'0110011'},
       'or':{'funct7':'0000000','func3':'110','opcode':'0110011'},
       'and':{'funct7':'0100000','func3':'111','opcode':'0110011'}}

riscv_registers={
    "zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100",
    "t0":"00101","t1":"00110","t2":"00111","s0":"01000","fp":"01000",
    "s1":"01001","a0":"01010","a1":"01011","a2":"01100","a3":"01101",
    "a4":"01110","a5":"01111","a6":"10000","a7":"10001","s2":"10010",
    "s3":"10011","s4":"10100","s5":"10101","s6":"10110","s7":"10111",
    "s8":"11000","s9":"11001","s10":"11010","s11":"11011","t3":"11100",
    "t4":"11101","t5":"11110","t6":"11111"
}

itype={'lw':{'funct3':'010','opcode':'0000011'},
       'addi':{'funct3':'000','opcode':'0010011'},
       'jalr':{'funct3':'000','opcode':'1100111'}}

btype={'beq':{'funct3':'000','opcode':'1100011'},
       'bne':{'funct3':'001','opcode':'1100011'},
       'blt':{'funct3':'100','opcode':'1100011'}}
fi=open(r"C:\Users\supri\OneDrive\Desktop\CO project\source.txt",'r')
dol={}
ino=0
for line in fi:
    line.rstrip()
    lt=line.split()
    if lt[0] not in itype and lt[0] not in rtype and lt[0] not in btype and lt[0]!='sw' and lt[0]!='jal':
        lt[0]=lt[0].rstrip(":")
        dol[lt[0]]=ino
    ino+=4
fi.close()       

f=open(r"C:\Users\supri\OneDrive\Desktop\CO project\source.txt","r")
ft=open(r"C:\Users\supri\OneDrive\Desktop\CO project\bin.txt","w")
for line in f:
    line.rstrip()
    lt=line.split()
    if lt[0] not in itype and lt[0] not in rtype and lt[0] not in btype and lt[0]!='sw' and lt[0]!='jal':
        lt.pop(0)   
    nl=lt[1].split(",")
    if lt[0] in rtype:
        v=f'{rtype[lt[0]]['funct7']}{riscv_registers[nl[2]]}{riscv_registers[nl[1]]}{rtype[lt[0]]['func3']}{riscv_registers[nl[0]]}{rtype[lt[0]]['opcode']}\n'
        ft.write(v)
    if lt[0] in itype:
        if lt[0]=='lw':
            nlt=nl[1].split("(")
            nlt[1]=nlt[1].rstrip(')')
            immd=None
            if nlt[0] in dol:
                immd=imm(str(dol[nlt[0]]-cino))
            else:
                immd=imm(nlt[0])    
            v=f'{immd}{riscv_registers[nlt[1]]}{itype[lt[0]]['funct3']}{riscv_registers[nl[0]]}{itype[lt[0]]['opcode']}\n'
            ft.write(v)
        else:
            immd=None
            if nl[2] in dol:
                immd=imm(str(dol[nl[2]]-cino))
            else:
                immd=imm(nl[2])    
            v=f'{immd}{riscv_registers[nl[1]]}{itype[lt[0]]['funct3']}{riscv_registers[nl[0]]}{itype[lt[0]]['opcode']}\n'    
            ft.write(v)
    if lt[0]=='sw':
        nlt=nl[1].split("(")
        nlt[1]=nlt[1].rstrip(')')
        ins=lt[0]
        rs2=riscv_registers[nl[0]]
        rs1=riscv_registers[nlt[1]]
        immd=None
        if nlt[0] in dol:
            immd=imm(str(dol[nlt[0]]-cino))
        else:
            immd=imm(nlt[0])    
        imm115=immd[:7]
        imm40=immd[7:]
        v=f'{imm115}{rs2}{rs1}010{imm40}0100011\n'
        ft.write(v)    
