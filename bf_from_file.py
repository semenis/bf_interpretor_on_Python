from bf import runcode
with open('input.txt') as file:
    code = file.read().strip().replace('\n','').replace(' ','')
runcode(code)