


"""
3. Viết chương trình nhập vào hai phân số. Tính tổng, hiệu, tích, thương giữa chúng và xuất kết quả.
"""

class PhanSo:
    def __init__(self, tu =1, mau= 1):
        self.tu = tu
        self.mau = mau

    def input(self):
        self.tu = int(input('nhap tu so: '))
        self.mau = int(input('nhap mau so: '))

    def output(self):
        print(f"phan so vua nhap la: {self.tu} / {self.mau}")

    def tong(self, phanso):
        tong = PhanSo()
        tong.tu = self.tu * phanso.mau + self.mau * phanso.tu
        tong.mau = self.mau * phanso.mau
        return tong

    def hieu(self, phanso):
        hieu = PhanSo()
        hieu.tu = self.tu * phanso.mau - self.mau * phanso.tu
        hieu.mau = self.mau * phanso.mau
        return hieu
    
    def tich(self, phanso):
        tich = PhanSo()
        tich.tu = self.tu * phanso.tu
        tich.mau = self.mau * phanso.mau
        return tich
def main():
    try:
        
        ps1 = PhanSo()
        ps1.input()
        ps1.output()

        ps2 = PhanSo()
        ps2.input()
        ps2.output()

        pstong = ps1.tong(ps2)
        print(f"tong hai phan so la: {pstong.tu}/{pstong.mau}")
        pshieu = ps1.hieu(ps2)
        print(f"hieu hai phan so la:{pshieu.tu}/{pshieu.mau}")
        pstich = ps1.tich(ps2)
        print(f"tich hai phan so la: {pstich.tu}/ {pstich.mau}")
        
    except ValueError as e:
        print(f"co loi: {e}")

if __name__ == '__main__':
    main()