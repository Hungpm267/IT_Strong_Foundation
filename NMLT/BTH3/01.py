


"""
Viết chương trình thực hiện các yêu cầu sau:

    Nhập tối đa 10 số nguyên vào một mảng. Bắt đầu nhập từ phần tử thứ 0 và 1.

    Sau đó tiếp tục nhập các phần tử tiếp theo, nhưng chỉ khi giá trị hiện tại lớn hơn giá trị trước đó (tức là nhập dãy tăng dần). Nếu người dùng nhập một số không lớn hơn số trước đó, việc nhập sẽ dừng lại.

    Sau khi kết thúc việc nhập, chương trình sẽ:

    Duyệt qua các phần tử đã nhập

    In ra các số nguyên tố trong mảng đó.

"""

def nhapmang(arr):
    
    temp = list(map(int, input("Nhap mang: ").split()))
    arr.extend(temp)
    """
    while len(arr) < 10:
        x = int(input())
        arr.append(x);"""
        

def isprime(n):
    if n<2: return False
    for i in range (2, int(n ** 0.5)+1, 1):
        if n % i ==0: return False
    return True

if __name__ == "__main__":
    arr = []
    nhapmang(arr)
    print("Mang da nhap la: ", arr)
    print("Cac so nguyen to trong mang la: ")
    for i in range (0, len(arr), 1):
        if isprime(arr[i]):
            print(arr[i], end = " ")










"""
1. append()
    a = [1, 2, 3]
    a.append([4, 5])
    print(a)  # 👉 [1, 2, 3, [4, 5]]
✅ Thêm một phần tử là danh sách [4, 5] → danh sách bị lồng.

2. extend()
    a = [1, 2, 3]
    a.extend([4, 5])
    print(a)  # 👉 [1, 2, 3, 4, 5]
✅ Thêm từng phần tử của [4, 5] vào danh sách → dàn phẳng.
"""

