

"""

🧠 Đề Bài: Tính Tổng trong Ma Trận
Viết chương trình Python thực hiện các yêu cầu sau:
    - Nhập một ma trận 2 chiều kích thước n x m từ bàn phím, với n là số hàng và m là số cột.
    - Tính và in tổng các hàng: Với mỗi hàng, tính tổng các phần tử trong hàng đó và in ra màn hình.
    - Tính và in tổng các cột: Với mỗi cột, tính tổng các phần tử trong cột đó và in ra màn hình.
    - Tính và in tổng toàn bộ ma trận: Tổng của tất cả các phần tử trong ma trận.
    - Nếu ma trận là ma trận vuông (tức là n == m), hãy:
    - Tính tổng của tam giác trên (phần tử nằm trên hoặc trên đường chéo chính, tức là các phần tử a[i][j] với j >= i).
    - Tính tổng của tam giác dưới (phần tử nằm dưới hoặc trên đường chéo chính, tức là các phần tử a[i][j] với j <= i).
    - Nếu không phải ma trận vuông, in thông báo không thể tính tổng tam giác.

📝 Yêu cầu bổ sung:
    - Viết hàm riêng cho từng chức năng.
    - Không dùng thư viện ngoài trừ các hàm có sẵn của Python (như input(), print()).
    - Đảm bảo mã chạy được với ma trận kích thước nhỏ và lớn (đến khoảng 100 x 100).

"""

def nhap_ma_tran(n, m, ma_tran):
    print(f"Nhập ma trận kích thước {n} x {m}: ")
    dict = {}
    
    for i in range(n):
        hang = []
        for j in range(m):
            x = int(input())
            hang.append(x)
        ma_tran.append(hang)

def in_ma_tran(ma_tran):
    print("Ma trận vừa nhập là: ")
    for i in range(len(ma_tran)):
        for j in range(len(ma_tran[i])):
            print(ma_tran[i][j], end=" ")
        print()

def in_tong_hang(hang, cot, ma_tran):
    dict = {}
    for i in range(hang):
        sum = 0
        for j in range(cot):
            sum = sum + ma_tran[i][j]
        dict[i] = sum
    for i in dict:
        print(f"Tổng hàng {i} là: {dict[i]}")

def in_tong_cot(hang, cot, ma_tran):
    dict = {}
    for i in range(cot):
        sum =0
        for j in range(hang):
            sum = sum+ma_tran[j][i]
        dict[i] = sum
    for i in dict:
        print(f"Tổng cột {i} là: {dict[i]}")
            
def in_tong_toan_bo(hang, cot, ma_tran):
    sum  =0 
    for i in range(hang):
        for j in range(cot):
            sum = sum + ma_tran[i][j]
    print(f"Tổng toàn bộ ma trận là: {sum}")

if __name__ == "__main__":
    print("Nhập số hàng n và số cột m của ma trận: ")
    n = int(input())
    m = int(input())
    ma_tran = []
    nhap_ma_tran(n, m , ma_tran)
    in_ma_tran(ma_tran)
    in_tong_hang(n, m, ma_tran)
    in_tong_cot(n ,m, ma_tran)
    in_tong_toan_bo(n, m, ma_tran)