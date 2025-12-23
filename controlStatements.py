# Control Statements - break(Stops the loop iteration), continue(Skips the iteration), pass(does nothing, just used to mark the point for later)
# break
for i in range(0,10) :
    if i==8 : break 
    print(i)

# continue
for i in range(0,10+1) : 
    if i==8 : continue
    print(i)

# pass
for i in range(0,5+1) : 
    if i==2 : pass
    print(i)