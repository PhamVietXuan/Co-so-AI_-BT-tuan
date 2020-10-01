import random

#Set bit tại vị trí thứ i(tính từ phải sang trái, i = 0, 1, 2, 3,.. n) của biến x
#input: số x và vị trí cần set bit i
#output: kết quả là số nguyên sau khi đã set bit
def set_bit(x, i):
    return x | (1 << i)


#Get bit tại vị trí thứ i(tính từ phải sang trái, i = 0, 1, 2, 3,.. n) của biến x
#input: số x và vị trí cần set bit i
#output: kết quả là số nguyên sau khi đã get bit
def get_bit(x, i):
    return x & (1<<i)


def get_bit_01(x, i):
    return (x>>i) & 1
#Tính nghiệm của phương trình bậc hai bằng phương pháp ngẫu nhiên
#input: hệ số a, b c của phương trình aX^2 + bX + c =0
#Output: Nghiệm của phương trình bậc hai
def phuong_trinh_b2(a, b, c):#he so a, b, c cua phuong trinh aX^2 + bX + c = 0
    pass

print(get_bit_01(10,2))
