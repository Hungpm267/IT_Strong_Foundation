# kiểm tra xem ký tự nhập vào có phải là chữ cái hay không, sau đó in ra dạng in hoa của ký tự đó (nếu cần)
# A:65 -> Z:90 và a:97 -> z:122

x = input("Nhập vào một ký tự: ")
while x != "end":
    if len(x) == 1 and x.isalpha() == True:
        if ord(x) >=65 and ord(x) <=90:
            print("day la chu cai in hoa, chuyen sang in thuong la: ", chr(ord(x)+32))
            
        elif ord(x)>=97 and ord(x)<=122:
            print("day la chu cai in thuong, chuyen sang in hoa la: ", chr(ord(x)-32))
    
    x = input("Nhập vào một ký tự: ")