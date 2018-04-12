n = int(input ("Nhap so vao day"))
from fractions import Fraction
ketqua = sum(Fraction(1, d) for d in range(1, n + 1))
print ("dap an", ketqua)
