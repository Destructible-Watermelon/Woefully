import re
import time
#################
#DOWN functions!#
#################
def AtoB():
    stack_B.append(stack_A.pop())

def diff():
    push(stack_A.pop()-stack_B.pop())

def mult():
    push(stack_A.pop()*stack_B.pop())

def dupe():
    stack_B.append(stack_A[-1])
down_funcs=(AtoB,diff,mult,dupe)

################
#DDR functions!#
################
def move():
    global cp
    cp[0]+=stack_A.pop()
    while cp[0]>=len(program[cp[0]]):
        cp[0]=cp[0]-len(program[cp[0]])
        cp[1]+=1
        if cp[1]>=len(program):cp[1]-len(program)

def bool():
    push(int(stack_A.pop()))

def inpt():
    push(ord(input()) if i_o_ascii else int(input()))

def otpt():
    print(chr(stack_A.pop())if i_o_ascii else stack_A.pop())

def swap():
    global i_o_ascii
    i_o_ascii=not i_o_ascii
ddr_funcs=(move,bool,inpt,otpt,swap)

i_o_ascii=False
stack_A=[0]
stack_B=[0]
push=stack_A.append

og_program=open(input()).read()
program=og_program.split("\n")
cp=[0,0]
if re.findall("[^| \n]| (\n|$)|(\n|^) |^[^ ]*$", og_program):
    print("confuse :(")
    exit()
finished=False
while not finished:
    ip=cp[:]
    while program[ip[1]][ip[0]]!=' ':
        ip[0]+=1
        if len(program[ip[1]])<=ip[0]:
            ip[1]+=1
            ip[0]=0
    instruction_dir=-1
    while True:
        instruction_counter=1
        if len(program)-1>ip[1] and ' ' in program[ip[1]+1][ip[0]-1:ip[0]+2]:
            instruction_dir=-1
        while len(program)-1>ip[1] and ' ' in program[ip[1]+1][ip[0]-1:ip[0]+2]:

            if instruction_dir==-1:
                instruction_dir=program[ip[1]+1][ip[0]-1:ip[0]+2].find(' ')
            elif program[ip[1]+1][ip[0]+instruction_dir-1:][:1]==' ':
                ip[1]+=1
                ip[0]+=instruction_dir-1
                instruction_counter+=1
            else:break
        if instruction_counter==1:finished=True

        if instruction_counter==2:continue
        if instruction_dir==0:push(instruction_counter-3)
        elif instruction_dir==1:down_funcs[(instruction_counter-3)%4]()
        elif instruction_dir==2:ddr_funcs[(instruction_counter-3)%5]()
        if not len(program)-1>ip[1] or not ' ' in program[ip[1]+1][ip[0]-1:ip[0]+2]:
            break