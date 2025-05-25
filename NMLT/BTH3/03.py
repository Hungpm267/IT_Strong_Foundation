


"""
nhap mang, kiem tra mang co tang dan khong
"""


def nhapmnag(arr):
    temp = list(map(int, input("Nhap mang: ").split()))
    arr.extend(temp)
    # while len(arr) < 10:
    #     x = int(input())
    #     arr.append(x);

if __name__ =="__main__":
    arr = []
    nhapmnag(arr)
    print("Mang da nhap la: ", arr)

    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            print("Mang khong tang dan")
            exit()
        i += 1
    
    print("Mang tang dan")