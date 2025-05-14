gio1, phut1, giay1 = map(int, input('nhap thoi gian thu nhat: ').split())
while True:
    if gio1 <0 or gio1>23 or phut1<0 or phut1>59 or giay1<0 or giay1>59:
        print('thoi gian thu nhat khong hop le, vui long nhap lai')
        gio1, phut1, giay1 = map(int, input('nhap thoi gian thu nhat: ').split())
    else: 
        break


gio2, phut2, giay2 = map(int, input('nhap thoi gian thu hai: ').split())
while True:
    if gio2 <0 or gio2>23 or phut2<0 or phut2>59 or giay2<0 or giay2>59:
        print('thoi gian thu hai khong hop le, vui long nhap lai')
        gio2, phut2, giay2 = map(int, input('nhap thoi gian thu hai: ').split())
    else:
        break

print(f'thoi gian thu nhat la: {gio1:02d}:{phut1:02d}:{giay1:02d} ')
print(f'thoi gian thu hai la: {gio2:02d}:{phut2:02d}:{giay2:02d} ')



def tinh_thu_cong(gio1, phut1, giay1, gio2, phut2, giay2):
    # tinh tong cua thoi gian
    gio = gio1 + gio2
    phut = phut1 + phut2    
    giay = giay1 + giay2

    if giay >=60:
        phut+=1
        giay = giay -60
    if phut>=60:    
        gio+=1
        phut=phut-60

    print(f'tong thoi gian la: {gio:02d}:{phut:02d}:{giay:02d}')

    # tinh hieu cua thoi gian
    gio = gio1 - gio2
    phut = phut1 - phut2
    giay = giay1 - giay2
    if giay < 0:
        phut -=1
        giay = giay + 60
    if phut < 0:
        gio -=1
        phut = phut +60
    if gio <=0:
        gio = 0
        phut = 0
        giay = 0
    print(f'hieu thoi gian la: {gio:02d}:{phut:02d}:{giay:02d}')

def tinh_vs_thu_vien(gio1, phut1, giay1, gio2, phut2, giay2):
    from datetime import datetime, timedelta
    
    time1 = timedelta(hours = gio1, minutes = phut1, seconds = giay1)
    time2 = timedelta(hours = gio2, minutes = phut2, seconds = giay2)
    tong_time = time1 + time2
    hieu_time = time1 - time2

    print(f'tong thoi gian la: {tong_time}')
    if hieu_time < timedelta(0):
        hieu_time = timedelta(0)    
    print(f'hieu thoi gian la: {hieu_time}')
    

while True:
    print('======chon 1 de tinh tong va hieu thu cong, chon 2 de tinh tong va hieu su dung thu vien, chon 3 de thoat======')
    chon = input('nhap lua chon: ')
    match chon:
        case '1':
            tinh_thu_cong(gio1, phut1, giay1, gio2, phut2, giay2)
        case '2':
            tinh_vs_thu_vien(gio1, phut1, giay1, gio2, phut2, giay2)
        case '3':
            print('cam on ban da su dung chuong trinh')
            exit()


