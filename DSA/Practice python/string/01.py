"""
Bài 1:
Viết chương trình nhập vào một chuỗi, in ra chuỗi đảo ngược của nó.
Bài 2:
Viết chương trình nhập vào một chuỗi, đếm số lần xuất hiện của từng ký tự trong chuỗi.
Bài 3:
Viết chương trình nhập vào một chuỗi, kiểm tra xem chuỗi đó có phải là chuỗi Palindrome hay không (chuỗi đối xứng).
Bài 4:
Viết chương trình nhập vào một chuỗi, in ra chuỗi với các ký tự đầu mỗi từ được viết hoa.
Bài 5:
Viết chương trình nhập vào một chuỗi, xóa tất cả các khoảng trắng thừa (chỉ giữ lại một khoảng trắng giữa các từ).
Bài 6:
Viết chương trình nhập vào một chuỗi và một ký tự, đếm xem ký tự đó xuất hiện bao nhiêu lần trong chuỗi.
Bài 7:
Viết chương trình nhập vào một chuỗi, in ra tất cả các từ dài nhất trong chuỗi.
Bài 8:
Viết chương trình nhập vào một chuỗi, thay thế tất cả ký tự số trong chuỗi bằng dấu *.
Bài 9:
Viết chương trình nhập vào hai chuỗi, kiểm tra xem chúng có phải là hoán vị của nhau không (anagram).
Bài 10:
Viết chương trình nhập vào một chuỗi, loại bỏ tất cả các ký tự không phải chữ cái.

"""


class chuoi:
    def __init__(self, mystring):
        self.mystring = mystring

    def bai1_reverse(self) -> str:
        return self.mystring[::-1]

    def bai2_countchar(self):
        mydict = {}
        for c in self.mystring:
            if c in mydict:
                mydict[c] += 1
            else:
                mydict[c] = 1

        for key, value in mydict.items():
            print(f'{key} xuat hien: {value} lan')

    def bai3_palindrome(self) -> bool:
        """
        return self.mystring == self.mystring[::-1]
        return self.mystring == ''.join(reversed(self.mystring))
        """
        i = 0
        j = len(self.mystring)-1
        while (i < j):
            if (self.mystring[i] < self.mystring[j]):
                return False
            i += 1
            j -= 1
        return True


    def bai4_camelize(self) -> str:

        words = self.mystring.lower().split()
        mychuoi = ' '.join(word.capitalize() for word in words)
        return mychuoi
        """
        words = self.mystring.lower().split()
        camelized = ' '.join(word.capitalize() for word in words)
        self.mystring = camelized
        return self.mystring
        """

    def bai6_demkytutrongchuoi(self, x):
        self.mystring


def main():
    str = input("mời bạn nhập string: ")
    obj = chuoi(str)
    chon = int(input('mời bạn nhập lựa chọn: '))
    match chon:
        case 1:
            print(f'chuỗi sau đảo ngược là: {obj.bai1_reverse()}')
        case 2:
            obj.bai2_countchar()
        case 3:
            print(f'chuoi la palindrome: {obj.bai3_palindrome()}')
        case 4:
            str = obj.bai4_camelize()
            print(f'camelize chuoi la: {str}')
        case default:
            return "nothing"

    """
    mydict = {'x': 10, 'y': 20}
    items_view = mydict.items()
    print(items_view)
    print(list(items_view))
    """


if __name__ == '__main__':
    main()
