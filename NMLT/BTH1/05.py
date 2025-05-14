from math import sqrt
# Bài 5: Viết chương trình giải phương trình bậc 2 ax^2 + bx + c = 0 với a, b, c là các số thực cho trước.

lap = True

while lap:
    try:
        a, b, c = map(int, input("nhập a, b, c lần lượt(cả 3 =9 nếu muốn exit hoặc nhapp65 sai định dạng): ").split())
        lap = False if a ==9 and b == 9 and c == 9 else True
        if a == 0:
            if b != 0:
                print("phương trình có 1 nghiệm x = ", -c / b)
            else:
                if c == 0: 
                    print("phương trình vô số nghiệm")
                else:
                    print("phương trình vô nghiệm")
        else:
            delta = b*b -4*a*c
            if delta < 0:
                print('phương trình vô nghiệm')
            elif delta == 0:
                print("phương trình có 1 nghiệm x = ", -b / (2*a))
            else:
                print(f'phương trình có 2 nghiệm phân biệt: {(-b+sqrt(delta)/2*a)} và {(-b-sqrt(delta)/2*a)}')
    except ValueError:
        print("nhập sai định dạng")
        lap = False