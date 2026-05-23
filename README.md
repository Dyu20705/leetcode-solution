# LeetCode Solutions

Kho lưu trữ các lời giải LeetCode bằng Python, được tổ chức theo nhiều nhóm bài toán khác nhau để tiện luyện tập, tra cứu và mở rộng theo thời gian.

## Mục tiêu

- Lưu lại lời giải cho các bài LeetCode đã làm.
- Tách nội dung theo ngữ cảnh luyện tập: `daily`, `contest`, `quest`.
- Duy trì cấu trúc thư mục đơn giản để dễ tìm bài theo số thứ tự hoặc chủ đề.

## Cấu trúc thư mục

```text
leetcode-solution/
├── contest/
│   ├── Biweekly Contest/
│   └── Weekly Contest/
├── daily/
├── quest/
│   └── ds&a/
├── main.py
└── README.md
```

### 1. `daily/`

Chứa các bài luyện tập hằng ngày, hiện có **37** lời giải.

Quy ước đặt tên file:

```text
<problem_id>. <problem_title>.py
```

Ví dụ:

- `48. Rotate Image.py`
- `153. Find Minimum in Rotated Sorted Array.py`
- `1345. Jump Game IV.py`

### 2. `contest/`

Chứa lời giải cho các kỳ thi đấu LeetCode, hiện có **18** lời giải.

Tổ chức theo:

- `Weekly Contest`
- `Biweekly Contest`

Mỗi contest thường gồm các file:

```text
Q1. ...
Q2. ...
Q3. ...
Q4. ...
```

### 3. `quest/`

Chứa các bài luyện theo chủ đề dữ liệu và giải thuật, hiện có **10** lời giải.

Một số nhóm đang có:

- `Array 1`
- `Array 2`
- `Stack`
- `Monotonic Stack`

## Công nghệ sử dụng

- **Ngôn ngữ:** Python
- **Phong cách lời giải:** ưu tiên ngắn gọn, bám sát format `class Solution` quen thuộc của LeetCode

## Cách sử dụng

### Mở và tham khảo lời giải

Tìm bài theo số hoặc tên ngay trong thư mục tương ứng:

```powershell
rg --files
```

Hoặc lọc nhanh theo mã bài:

```powershell
rg --files | rg "48\\."
```

### Chạy thử cục bộ

Phần lớn file được viết theo format nộp trực tiếp lên LeetCode. Nếu muốn chạy cục bộ, bạn có thể tự tạo dữ liệu test và gọi class `Solution` trong một file tạm hoặc trong `main.py`.

Ví dụ:

```python
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
```

## Quy ước trong repo

- Tên file thường giữ nguyên số bài và tiêu đề trên LeetCode để dễ tra cứu.
- Một số lời giải có ghi chú ngắn bằng tiếng Việt để giải thích ý tưởng hoặc tối ưu.
- Repo ưu tiên lưu lời giải thực chiến, không đặt nặng framework hay bộ test chung ở thời điểm hiện tại.

## Định hướng mở rộng

Trong tương lai, repo có thể được bổ sung thêm:

- bảng thống kê số lượng bài theo chủ đề
- tag độ khó hoặc kỹ thuật áp dụng
- test runner đơn giản để chạy local một số bài tiêu biểu
- index tổng hợp để tìm bài nhanh hơn

## Ghi chú

`main.py` hiện là file trống tối giản và có thể dùng làm nơi thử nghiệm cục bộ khi cần.

---

Nếu bạn đang xây dựng thói quen luyện LeetCode mỗi ngày, repo này đóng vai trò như một nhật ký lời giải có cấu trúc, dễ mở rộng và dễ rà soát lại sau này.
