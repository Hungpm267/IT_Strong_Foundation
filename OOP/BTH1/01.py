

"""
1. Viết chương trình nhập vào một phân số, rút gọn phân số và xuất kết quả.
"""


class phanso:
    def __init__(self, tu =1, mau=1):
        self.tu = tu
        self.mau = mau

    def input(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))
        while self.mau == 0:
            print("mau so phia khac 0, vui long nhap lai")
            self.mau = int(input("Nhập mẫu số: "))

    def output(self):
        print(f"Phan so vua nhap(da rut gon) la: {self.tu}/{self.mau}")

    def timucln(self):
        t = abs(self.tu)
        m = abs(self.mau)
        while t != m:
            if t>m: 
                t=t-m
            else: 
                m=m-t
        return t

    def rutgon(self):
        ucln = self.timucln()
        self.tu //= ucln
        self.mau //= ucln

        


def main():
    ps1 = phanso()
    ps1.input()
    ps1.rutgon()
    ps1.output()


if __name__ == "__main__":
    main()
