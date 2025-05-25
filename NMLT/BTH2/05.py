


"""

tim uoc chung lon nhat cua hai so
"""
def ucln(a, b):
    while a!=b:
        if a>b: a = a-b
        else: b=b-a

    return a

if __name__ == "__main__":
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    u = ucln(a, b)
    print(f"Uoc chung lon nhat cua {a} va {b} la: {u}")