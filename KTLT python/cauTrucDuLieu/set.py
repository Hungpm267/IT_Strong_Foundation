'''
🧩 Bài tập: Quản lý Tập Hợp Sinh Viên Đăng Ký Môn Học
🎯 Mô tả:
 - Một trường đại học có 3 môn học tự chọn: Toán, Lý, Hóa. Mỗi sinh viên có thể đăng ký một hoặc nhiều môn.
 - Bạn cần viết chương trình cho phép:
 - Nhập danh sách sinh viên của từng môn.
 - Thực hiện một số thao tác phân tích dựa trên set.

📥 Input yêu cầu từ người dùng:
 - Nhập danh sách sinh viên đăng ký từng môn học (tên sinh viên, không trùng lặp trong cùng môn).

🛠 Các chức năng cần thực hiện:
 - In ra danh sách tất cả sinh viên đã đăng ký ít nhất một môn.
 - Tìm các sinh viên đăng ký tất cả các môn.
 - Tìm các sinh viên chỉ đăng ký đúng một môn.
 - Tìm các sinh viên đăng ký cả Toán và Lý nhưng không đăng ký Hóa.
 - Tìm các sinh viên không đăng ký môn nào cả (gợi ý: hỏi thêm toàn bộ sinh viên trong lớp, ví dụ nhập thêm danh sách 
toàn bộ sinh viên trong lớp).
'''

# Bước 1: Nhập danh sách sinh viên
toan = set(input("Nhập danh sách sinh viên môn Toán (phân tách bởi dấu phẩy): ").split(','))
ly = set(input("Nhập danh sách sinh viên môn Lý (phân tách bởi dấu phẩy): ").split(','))
hoa = set(input("Nhập danh sách sinh viên môn Hóa (phân tách bởi dấu phẩy): ").split(','))
tat_ca = set(input("Nhập danh sách toàn bộ sinh viên lớp (phân tách bởi dấu phẩy): ").split(','))

# Làm sạch dữ liệu
toan = {s.strip() for s in toan if s.strip()}
ly = {s.strip() for s in ly if s.strip()}
hoa = {s.strip() for s in hoa if s.strip()}
tat_ca = {s.strip() for s in tat_ca if s.strip()}

# Câu 1: Sinh viên đăng ký ít nhất một môn
it_nhat_mot_mon = toan | ly | hoa
print("1. Sinh viên đăng ký ít nhất một môn:", it_nhat_mot_mon)

# Câu 2: Sinh viên đăng ký tất cả các môn
tat_ca_mon = toan & ly & hoa
print("2. Sinh viên đăng ký tất cả các môn:", tat_ca_mon)

# Câu 3: Sinh viên chỉ đăng ký đúng một môn
chi_toan = toan - ly - hoa
chi_ly = ly - toan - hoa
chi_hoa = hoa - toan - ly
chi_mot_mon = chi_toan | chi_ly | chi_hoa
print("3. Sinh viên chỉ đăng ký đúng một môn:", chi_mot_mon)

# Câu 4: Sinh viên đăng ký cả Toán và Lý nhưng không đăng ký Hóa
toan_ly_khong_hoa = (toan & ly) - hoa
print("4. Sinh viên đăng ký Toán và Lý nhưng không Hóa:", toan_ly_khong_hoa)

# Câu 5: Sinh viên không đăng ký môn nào
khong_mon_nao = tat_ca - it_nhat_mot_mon
print("5. Sinh viên không đăng ký môn nào:", khong_mon_nao)

