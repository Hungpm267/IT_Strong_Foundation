






def nhap_mang(arr):
    print(f"Nhập phần tử cho mảng: ")
    temp = list(map(int, input().split()))
    arr.extend(temp)

def xuat_mang(arr):
    
    for i in range(len(arr)):
        print(arr[i], end=" ")

def xoa_phan_tu(arr, vitri_xoa):
    for i in range(len(arr)):
        if i == vitri_xoa:
            for j in range(i , len(arr) - 1):
                arr[j] = arr[j + 1]
            arr.pop()
            break

def tim_max(arr):
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    
    for i in range(len(arr)):
        if arr[i] == max_value:
            print(i, end=" ")

if __name__ == "__main__":
    arr = []
    nhap_mang(arr)
    print("Mảng vừa nhập là: ")
    xuat_mang(arr)

    vitri_xoa = int(input("\nvui long chon vi tri k: "))
    xoa_phan_tu(arr, vitri_xoa)
    print("Mảng sau khi xóa là: ")
    xuat_mang(arr)

    print("\ncac phan tu co gia tri lon nhat trong mang la: ")
    tim_max(arr)