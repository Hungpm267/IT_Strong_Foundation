









def nhapmang(arr, n):
    i = 0
    while i<n:
        x = int(input(f"Nhap phan tu thu {i+1}: "))
        arr.append(x)
        i+=1

def xoa_ptu(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            for j in range(i, n-1):
                arr[j] = arr[j+1]
            n = arr.pop()
            break

if __name__ == "__main__":
    n  = int(input("Nhap so phan tu cua mang: "))
    arr = []
    nhapmang(arr, n)

    print("Mang da nhap la: ", arr)

    x = int(input("Nhap phan tu can xoa: "))
    xoa_ptu(arr, n, x)
    print("Mang sau khi xoa phan tu la: ", arr)
    
