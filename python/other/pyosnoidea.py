class ops:
    def NOR(a,b):
        return not(a or b)
    def NOT(a):
        return ops.NOR(a, a)
    def AND(a, b):
        return ops.NOT(ops.NOT(a) or ops.NOT(b))
    def OR(a, b):
        return ops.NOT(ops.NOR(a, b))
    def XOR(a, b):
        return ops.OR(ops.AND(a, ops.NOT(b)), ops.AND(ops.NOT(a), b))


#create memory architechture
class main:
    def init():
        mem = []
        for cell in range(0,65536):
            mem.append(cell)
            mem[cell] = 0
            
        IP = 0
        ip = 0

        while True:
            i = mem[IP]
            a = mem[i + 0]
            b = mem[i + 1]
            r = mem[i + 2]

            mem[ip] = i + 3

            f = ops.NOR(mem[a],mem[b])
            mem[r] = f

            return False

main.init()
