Dưới đây là bản **tổng hợp các kỹ thuật lập trình phổ biến** (thường gặp trong coding interviews) kèm mô tả ngắn, bài toán mẫu, và khi nào nên dùng.

---

## 🧠 **TỔNG HỢP KỸ THUẬT GIẢI THUẬT PHỔ BIẾN**

---

### 1. 🔄 **Two Pointers**

**Ý tưởng:** Dùng hai con trỏ để quét qua mảng từ hai đầu hoặc cùng một đầu (di chuyển con trỏ theo điều kiện).

**Dùng khi:**

* Mảng **đã sắp xếp**
* Tìm **cặp** thỏa mãn điều kiện
* **Tối ưu độ phức tạp** thay vì dùng 2 vòng lồng nhau

**Ví dụ:**

* Tìm hai số có tổng bằng `target` trong mảng đã sắp xếp
* Kiểm tra chuỗi đối xứng (palindrome)

---

### 2. 🪟 **Sliding Window**

**Ý tưởng:** Dùng một "cửa sổ" di động (với kích thước cố định hoặc linh hoạt) để duyệt qua mảng/chuỗi mà không cần lặp lại nhiều lần.

**Dùng khi:**

* Cần kiểm soát **một đoạn liên tiếp**
* Cần tìm **tổng/tích/tần suất** trong đoạn con
* Tối ưu thay vì dùng nested loop

**Ví dụ:**

* Độ dài subarray nhỏ nhất có tổng ≥ k
* Tìm chuỗi con không chứa ký tự lặp
* Đếm tần suất ký tự

---

### 3. 📊 **Prefix Sum / Cumulative Sum**

**Ý tưởng:** Tính tổng dồn để nhanh chóng truy xuất tổng đoạn con bất kỳ.

**Dùng khi:**

* Tính **tổng subarray nhanh**
* Tránh dùng vòng lặp lồng nhau cho tổng liên tiếp

**Ví dụ:**

* Subarray có tổng bằng `k`
* Đếm subarray chia hết cho `k`
* Đếm số lượng mưa giữa 2 ngày

---

### 4. 🧮 **Hash Map / Dictionary**

**Ý tưởng:** Lưu trữ và truy xuất thông tin **O(1)** theo key-value.

**Dùng khi:**

* Cần đếm tần suất (Counter)
* Cần truy cập nhanh theo điều kiện
* Xử lý ánh xạ (mapping), đồng cấu trúc, anagram...

**Ví dụ:**

* Nhóm từ đồng âm
* Kiểm tra có subarray tổng bằng 0 không
* Subarray chia hết cho `k`

---

### 5. ⏫ **Binary Search**

**Ý tưởng:** Tìm kiếm trong dãy **đã sắp xếp** theo cách chia đôi.

**Dùng khi:**

* Mảng hoặc dãy có tính chất **đơn điệu** (tăng/giảm)
* Cần tìm **ngưỡng/tối ưu hóa**

**Ví dụ:**

* Tìm phần tử nhỏ nhất lớn hơn target
* Tìm độ dài subarray tối thiểu thỏa điều kiện
* Tìm root bậc hai xấp xỉ

---

### 6. 🔗 **Fast and Slow Pointers (Tortoise & Hare)**

**Ý tưởng:** Dùng 2 con trỏ với tốc độ khác nhau để phát hiện vòng lặp hoặc điểm hội tụ.

**Dùng khi:**

* Danh sách liên kết
* Phát hiện chu trình
* Tìm trung điểm

**Ví dụ:**

* Phát hiện vòng lặp trong Linked List
* Tìm điểm gặp trong chu trình
* Tìm middle node

---

### 7. 🔁 **Backtracking**

**Ý tưởng:** Thử từng khả năng, quay lui nếu sai.

**Dùng khi:**

* Cần duyệt tất cả tổ hợp/hoán vị
* Bài toán có ràng buộc (constraints)

**Ví dụ:**

* Sudoku
* N-Queens
* Tổ hợp chữ số trên bàn phím

---

### 8. 🧩 **Dynamic Programming (DP)**

**Ý tưởng:** Ghi nhớ kết quả con để tránh tính lại.

**Dùng khi:**

* Bài toán có tính chất **tối ưu hóa** + **con trùng lặp**
* Cần xây bảng (`dp[]`, `dp[][]`)

**Ví dụ:**

* Dãy con tăng dài nhất
* Tối ưu ba lô (Knapsack)
* Đếm số cách leo cầu thang

---

### 9. 🧮 **Greedy (Tham lam)**

**Ý tưởng:** Luôn chọn phương án tốt nhất tại thời điểm hiện tại.

**Dùng khi:**

* Bài toán có cấu trúc cho phép chọn "từng bước tốt nhất" → toàn cục tối ưu

**Ví dụ:**

* Đổi tiền
* Họp không trùng lịch
* Đoạn phủ sóng nhỏ nhất

---

### 10. 🕸️ **Union-Find / Disjoint Set Union (DSU)**

**Ý tưởng:** Gộp và tìm đại diện của tập hợp.

**Dùng khi:**

* Bài toán liên quan **nhóm/connected components**
* Graph không cần DFS/BFS đầy đủ

**Ví dụ:**

* Kiểm tra chu trình trong đồ thị
* Đếm số vùng kết nối
* Kruskal trong Minimum Spanning Tree

---

