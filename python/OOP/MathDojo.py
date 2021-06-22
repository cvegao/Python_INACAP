class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

    def std(self, num, *nums):
        n = 2 + len(nums)
        mean = self.result + num
        for i in nums:
            mean += i
        mean = mean / n
        subtotal = (self.result - mean)**2 + (num - mean)**2
        for i in nums:
            subtotal += (i - mean)**2
        total = subtotal / (n - 1)
        return total**.5


# crear una instruccion:
md = MathDojo()
# para probar:
print("------ Testing ADD method ------")
print("md.add(1, 2, 4)")
print(md.add(1, 2, 4).result)
print("md.add(1)")
print(md.add(1).result)
print("md.add(1, 9)")
print(md.add(1, 9).result)

print("------ Testing SUBSTRACT method ------")
print("md.subtract(1, 2, 4)")
print(md.subtract(1, 2, 4).result)
print("md.subtract(1)")
print(md.subtract(1).result)
print("md.subtract(9, 1)")
print(md.subtract(9, 1).result)

md.result = 0
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)  # debe imprimir 5
# corre cada uno de los metodos algunos mas veces y valida el resultado!
