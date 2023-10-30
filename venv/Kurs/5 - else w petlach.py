instruction = ['say hello', 'say how are you', 'ask for money','abort','say thank u', 'say bye']
instructionApproved = []

for instr in instruction:
    print('Adding instruction:', instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print('Aborting!')
        instructionApproved.clear()
        break
else: 
    print('Followig actions will be taken:', instructionApproved)

print('-'*30) # !!!
i = 0
while i < len(instruction):
    print('Adding instruction:', instruction[i])
    instructionApproved.append(instruction[i])

    if instruction[i] == 'abort':
        print('Aborting!')
        instructionApproved.clear()
        break
    i+=1
else:
    print('Followig actions will be taken:', instructionApproved)

print('_'*40)


