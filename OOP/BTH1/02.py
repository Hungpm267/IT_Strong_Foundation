"""
2. Viết chương trình nhập vào hai phân số, tìm phân số lớn nhất và xuất kết quả.
"""

class PhanSo:
    def __init__(self, tu=1, mau=1):
        self.tu = tu
        self.mau = mau

    def nhap(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))

    def xuat(self):
        print(f'Phân số vừa nhập là: {self.tu}/{self.mau}')

    def so_sanh(self, phan_so_khac):
        thuong1 = self.tu / self.mau
        thuong2 = phan_so_khac.tu / phan_so_khac.mau
        if thuong1 < thuong2:
            print("Phân số thứ nhất nhỏ hơn phân số thứ hai.")
        else:
            print("Phân số thứ hai nhỏ hơn hoặc bằng phân số thứ nhất.")

def main():
    ps1 = PhanSo()
    ps2 = PhanSo()

    ps1.nhap()
    ps1.xuat()

    ps2.nhap()
    ps2.xuat()

    ps1.so_sanh(ps2)

if __name__ == '__main__':
    main()
