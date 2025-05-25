

"""
Viết chương trình thực hiện các yêu cầu sau:

    Nhập số nguyên n là số phần tử của mảng a (với 1 ≤ n ≤ 1000).

    Nhập n số nguyên cho mảng a[1]..a[n].

    Kiểm tra xem trong mảng có tồn tại ít nhất một phần tử âm hay không:

    Nếu không có phần tử âm, in ra:

    Mang khong co phan tu am
    Nếu có phần tử âm, hãy:

    Tìm giá trị âm lớn nhất trong mảng.

    In ra giá trị âm lớn nhất và vị trí đầu tiên nó xuất hiện (vị trí tính từ 1).
"""


def nhapmang(arr):
    temp = list(map(int, input("Nhap mang: ").split()))
    arr.extend(temp)

if __name__ == "__main__":
    arr = []
    nhapmang(arr)
    print("Mang da nhap la: ", arr)

    flag = 0
    min = 0
    for index, value in enumerate(arr):
        if value < 0:
            flag = 1
            if min > value:
                min = value
                index_min = index

    if flag == 0:
        print("Mang khong co phan tu am")
        exit()
    else:
        print("Phan tu am lon nhat trong mang la: ", min)
        print("Vi tri phan tu am lon nhat la: ", index_min + 1)
