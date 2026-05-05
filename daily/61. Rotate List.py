class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Bước 1: tính độ dài + tìm tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # Bước 2: tối ưu k
        k %= n
        if k == 0:
            return head

        # Bước 3: nối thành vòng
        tail.next = head

        # Bước 4: tìm điểm cắt
        steps_to_new_head = n - k
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # Bước 5: cắt vòng
        new_tail.next = None

        return new_head