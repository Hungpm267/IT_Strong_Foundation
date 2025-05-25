"""
kiểm tra mảng đối xứng

"""

def nhapmang(arr):
    temp = list(map(int, input("Nhap mang: ").split()))
    arr.extend(temp)
    

if __name__ == "__main__":
    arr = []
    nhapmang(arr)
    print("Mang da nhap la: ", arr)

    flag = 1
    for i in range(0, len(arr)//2, 1):
        if arr[i] != arr[len(arr)-1-i]:
            flag = 0
            print("Mang khong doi xung")
            break

    if flag == 1:
        print("Mang doi xung")