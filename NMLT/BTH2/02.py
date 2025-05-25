"""
tinh tong giai thua: tong  = 1! + 2! + 3! + ... + n!
"""



def giaithua(n):
    gt =1;
    for i in range(n, 0, -1):
        gt = gt*i
    return gt

if __name__ == "__main__":
    tong = 0
    n = int(input("Nhap n: "))
    for i in range(1, n+1, 1):
        tong = tong + giaithua(i)

    print(f"tong cua {n} giai thua la: {tong}")