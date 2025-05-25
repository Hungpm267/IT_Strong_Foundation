"""
nhap n, tinh tong 1/2 + 1/4 + 1/6 + ... + 1/2n
"""

if __name__  == "__main__":
    n = int(input("Nhap n: "))
    tong = 0
    for i in range(1, n+1):
        tong+=(1/(2*i))
    print("Tong 1/2 + 1/4 + 1/6 + ... + 1/2n = ", tong)