




def isprime(n):
    if n <2:
        return False
    else:
        for i in range(2, n, 1):
            if n % i == 0:
                return False
    return True

if __name__ == "__main__":
    n = int(input("Nhap n: "))
    print(f"Cac so nguyen to nho hon {n} la: ")
    for i in range(2, n+1):
        if isprime(i): 
            print(i, end = "-")



