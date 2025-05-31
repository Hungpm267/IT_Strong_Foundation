


import random


class ChungCu():
    def __init__(self, tencc, sotang, dientich, tenql, sohuu):
        self.tencc = tencc
        self.sotang = sotang
        self.dientich = dientich
        self.tenql = tenql
        self.sohuu = sohuu

    def guiphieuthongbao(self):
        print(f'{self.tenql} - {self.tencc} - {self.sohuu}')

    def nhapsoluongcc(self):
        print("moi ban nhap so luong chung cu: ")

    def tienPhong(self):
        raise NotImplementedError("Phải override hàm này ở lớp con")
        

class CCVinhome(ChungCu):
    def __init__(self, tencc, sotang, dientich, tenql, sohuu):
        super().__init__(tencc, sotang, dientich, tenql, sohuu)

    def nhapsoluongcc(self):
        super().nhapsoluongcc()
        x= int(input("so luong chung cu vin: "))

    def guiphieuthongbao(self):
        return super().guiphieuthongbao()

    def tienPhong(self):
        tien =1 
        if self.dientich > 600:
            tien = random.randint(10, 15) * 6 * self.sotang
            return tien
        elif self.dientich <= 600:
            tien = random.randint(6, 10) * 6 * self.sotang

        return tien

class Bcons(ChungCu):
    def __init__(self, tencc, sotang, dientich, tenql, sohuu):
        super().__init__(tencc, sotang, dientich, tenql, sohuu)
    
    def nhapsoluongcc(self):
        super().nhapsoluongcc()
        x = int(input("so luong chung cu bcon la: "))
    
    def guiphieuthongbao(self):
        return super().guiphieuthongbao()

    def tienPhong(self):
        tien =1 
        if self.dientich > 600:
            tien = random.randint(8, 12) * 6 * self.sotang
            return tien
        elif self.dientich <= 600:
            tien = random.randint(5, 8) * 6 * self.sotang

        return tien
    

def main():
    cc1 = CCVinhome("vin home", 13, 25, "hung quan ly", "hung so huu")
    cc1.nhapsoluongcc()
    cc2 = Bcons("bcon", 44, 30, "manh quan ly", "manh so huu")
    cc2.nhapsoluongcc()

    print("vinhome gui phieu thong bao: ")
    cc1.guiphieuthongbao()
    print("bcons gui phieu thong bao: ")
    cc2.guiphieuthongbao()

    tongtien = cc1.tienPhong() + cc2.tienPhong()
    print(f'moi thang ban quan ly chung cu lang dai hoc thu ve {tongtien} trieu')

if __name__ == '__main__':
    main()