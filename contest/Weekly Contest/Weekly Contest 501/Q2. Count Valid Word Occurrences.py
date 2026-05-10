from collections import Counter
import re
class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        text = "".join(chunks)
        pattern = r'[a-z]+(?:-[a-z]+)*' #mẫu regex để tìm các từ hợp lệ, bao gồm cả các từ có dấu gạch nối
        words = re.findall(pattern, text)
        word_count = Counter(words)
        return [word_count.get(query, 0) for query in queries]
        #Bản tối ưu memory bên dưới, không dùng regex, chỉ duyệt 1 lần qua chuỗi
        # s = ''.join(chunks)
        # n = len(s)

        # freq = {}

        # i = 0
        # while i < n:
        #     c = s[i]

        #     # start word
        #     if 'a' <= c <= 'z':
        #         start = i
        #         i += 1

        #         while i < n:
        #             c = s[i]

        #             if 'a' <= c <= 'z':
        #                 i += 1

        #             elif c == '-':
        #                 # hyphen phải kẹp giữa 2 chữ
        #                 if (
        #                     i + 1 < n and
        #                     'a' <= s[i + 1] <= 'z'
        #                 ):
        #                     i += 1
        #                 else:
        #                     break
        #             else:
        #                 break

        #         word = s[start:i]
        #         freq[word] = freq.get(word, 0) + 1

        #     else:
        #         i += 1

        # return [freq.get(q, 0) for q in queries]