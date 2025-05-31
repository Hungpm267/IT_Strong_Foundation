"""
Viết một hàm nhận vào một danh sách các số nguyên và trả về phần tử xuất hiện nhiều nhất trong danh sách.
Cho một dictionary có key là từ (str) và value là nghĩa của từ. Viết hàm trả về từ có độ dài dài nhất.
Viết hàm nhận vào một danh sách các dictionary và gộp chúng lại. Nếu key trùng, hãy cộng giá trị.
"""


class baitap():
    def __init__(self, list):
        self.list = list

    def getMostFrequent(self):
        dict = {}
        for num in self.list:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        if not dict:
            print("Dictionary này đang rỗng!")  # ✅ Sẽ in ra dòng này
            return None
        else:
            for key, value in dict.items():
                print(f'{key} xuat hien: {value} lan')
            return max(dict, key=dict.get)

    def getMostLongestKey(self) -> str:
        dict = {
            'cat': 'a small animal',
            'elephant': 'a large animal',
            'dog': 'a loyal animal'
        }

        longest = ""
        for key in dict.keys():
            if len(key) > len(longest):
                longest = key
        return longest

    @staticmethod
    def mergeDict() -> None:
        mydict = {
            1: 100, 2: 200, 3: 300, 4: 400, 5: 500
        }
        mydict2 = {
            1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600, 7: 700, 8: 800, 9: 900, 10: 1000
        }

        cackeycuadict2 = list(mydict2.keys())
        for i in cackeycuadict2:
            if i in list(mydict.keys()):
                mydict[i] +=mydict2[i]
            else:
                mydict[i] = mydict2[i]
        
        for key, value in mydict.items():
            print(f'{key} - {value}')


def main():
    list = [3, 6, 5, 3, 6, 1, 7, 5, 9, 8, 5, 6, 5, 5, 2,
            4, 3, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    obj = baitap(list)
    print(f'so co tan suat xuat hien nhieu nhat la: {obj.getMostFrequent()}')
    print(f'key co do dai dai nhat la: {obj.getMostLongestKey()}')
    print(f"merge dict: {obj.mergeDict()}")


if __name__ == '__main__':
    main()


"""
=======================================================================================================
 max(frequency)
➡️ Trả về key lớn nhất, theo giá trị của key chứ không phải value.
max(frequency, key=frequency.get)
➡️ Cũng trả về một key, nhưng là key có value lớn nhất.
"""
