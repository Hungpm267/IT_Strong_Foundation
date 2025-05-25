

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    print(f"tong cac chu so cua {n} la: ")
    tong =0
    while n > 0:
        tong = tong + n % 10
        n = n // 10

    print(tong)