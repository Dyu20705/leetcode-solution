'''
Đây là thuật giải cho bài toán 3629. Minimum Jumps to Reach End via Prime Teleportation trên LeetCode. Bài toán yêu cầu tìm số bước nhảy tối thiểu để đi từ vị trí đầu tiên đến vị trí cuối cùng trong một mảng, với các bước nhảy có thể là nhảy sang trái, nhảy sang phải hoặc nhảy đến một vị trí khác có giá trị nguyên dương nhỏ nhất chia hết cho giá trị tại vị trí hiện tại (nếu có). Thuật giải sử dụng thuật toán BFS để khám phá các vị trí tiếp theo và một số kỹ thuật tối ưu hóa để cải thiện hiệu suất của thuật toán.
Hiệu suất hiện tại: Runtime O(n log log n + n) - O(n log log n) để tính toán số nguyên dương nhỏ nhất chia hết cho mỗi số nguyên dương từ 2 đến 10^6 bằng thuật toán Sieve of Eratosthenes, và O(n) để xây dựng bucket và thực hiện BFS. Space O(n + MX) - O(n) cho mảng visited và O(MX) cho mảng used, cùng với không gian cho bucket.
'''
from typing import List

#Tính toán tất cả các số nguyên dương nhỏ hơn hoặc bằng 10^6 và lưu trữ số nguyên dương nhỏ nhất chia hết cho mỗi số nguyên dương đó (spf - smallest prime factor). Đồng thời, lưu trữ tất cả các số nguyên dương nhỏ hơn hoặc bằng 10^6 là số nguyên dương nhỏ nhất chia hết cho một số nguyên dương nào đó (primes - danh sách các số nguyên dương nhỏ nhất chia hết cho một số nguyên dương nào đó).
MX = 10**6 + 1 #Định nghĩa một hằng số MX là 10^6 + 1, đại diện cho giới hạn trên của các số nguyên dương mà chúng ta sẽ tính toán và lưu trữ thông tin về chúng.

spf = [0] * MX #Tạo một mảng spf có kích thước MX, được khởi tạo với giá trị 0. Mảng này sẽ được sử dụng để lưu trữ số nguyên dương nhỏ nhất chia hết cho mỗi số nguyên dương từ 0 đến MX-1.
primes = [] #Tạo một danh sách primes rỗng, sẽ được sử dụng để lưu trữ tất cả các số nguyên dương nhỏ hơn hoặc bằng 10^6 là số nguyên dương nhỏ nhất chia hết cho một số nguyên dương nào đó.

#Sử dụng thuật toán Sieve of Eratosthenes để tính toán số nguyên dương nhỏ nhất chia hết cho mỗi số nguyên dương từ 2 đến MX-1. Nếu spf[i] == 0, điều đó có nghĩa là i là một số nguyên dương nhỏ nhất chia hết cho chính nó, vì vậy chúng ta gán spf[i] = i và thêm i vào danh sách primes. Sau đó, chúng ta lặp qua tất cả các số nguyên dương nhỏ hơn hoặc bằng i trong danh sách primes và cập nhật spf cho các bội của i. Nếu p là số nguyên dương nhỏ nhất chia hết cho i, thì chúng ta gán spf[v] = p cho tất cả các bội v của i (v = i * p). Nếu p đã là số nguyên dương nhỏ nhất chia hết cho i, chúng ta dừng việc cập nhật spf cho các bội của i.
for i in range(2, MX):
    #Nếu spf[i] == 0, điều đó có nghĩa là i là một số nguyên dương nhỏ nhất chia hết cho chính nó, vì vậy chúng ta gán spf[i] = i và thêm i vào danh sách primes.
    if spf[i] == 0:
        spf[i] = i
        primes.append(i)

    #Sau đó, chúng ta lặp qua tất cả các số nguyên dương nhỏ hơn hoặc bằng i trong danh sách primes và cập nhật spf cho các bội của i. Nếu p là số nguyên dương nhỏ nhất chia hết cho i, thì chúng ta gán spf[v] = p cho tất cả các bội v của i (v = i * p). Nếu p đã là số nguyên dương nhỏ nhất chia hết cho i, chúng ta dừng việc cập nhật spf cho các bội của i.
    for p in primes:

        v = i * p #Tính toán bội v của i bằng cách nhân i với p.

        if v >= MX: #Nếu bội v của i vượt quá giới hạn MX, chúng ta dừng việc cập nhật spf cho các bội của i bằng cách
            break

        spf[v] = p #Gán spf[v] = p, nghĩa là số nguyên dương nhỏ nhất chia hết cho v là p.

        if p == spf[i]: #Nếu p đã là số nguyên dương nhỏ nhất chia hết cho i, chúng ta dừng việc cập nhật spf cho các bội của i bằng cách
            break


class Solution:
    #Sử dụng thuật toán BFS để tìm số bước nhảy tối thiểu từ vị trí đầu tiên đến vị trí cuối cùng trong mảng nums. Mỗi bước nhảy có thể là nhảy sang trái, nhảy sang phải hoặc nhảy đến một vị trí khác có giá trị nguyên dương nhỏ nhất chia hết cho giá trị tại vị trí hiện tại (nếu có). Sử dụng một hàng đợi để lưu trữ các vị trí cần khám phá và một mảng bytearray để đánh dấu các vị trí đã được thăm.
    def minJumps(self, nums: List[int]) -> int:

        n = len(nums) #Lấy độ dài của mảng nums và lưu trữ nó trong biến n.
        
        if n == 1: #Nếu độ dài của mảng nums là 1, điều đó có nghĩa là chúng ta đã ở vị trí cuối cùng ngay từ đầu, vì vậy chúng ta có thể trả về 0 bước nhảy.
            return 0

        spf_local = spf #

        bucket = {} #Tạo một từ điển bucket để lưu trữ các vị trí của mảng nums dựa trên giá trị nguyên dương nhỏ nhất chia hết cho giá trị tại vị trí đó. Cụ thể, bucket[p] sẽ chứa một danh sách các chỉ số i mà nums[i] có số nguyên dương nhỏ nhất chia hết là p.

        #Lặp qua tất cả các phần tử trong mảng nums và xác định số nguyên dương nhỏ nhất chia hết cho mỗi phần tử. Sau đó, thêm chỉ số của phần tử đó vào bucket tương ứng với số nguyên dương nhỏ nhất chia hết. Nếu số nguyên dương nhỏ nhất chia hết đã tồn tại trong bucket, chúng ta thêm chỉ số vào danh sách hiện có; nếu chưa tồn tại, chúng ta tạo một danh sách mới chứa chỉ số đó.
        for i, x in enumerate(nums):

            v = x #Lấy giá trị tại vị trí i trong mảng nums và lưu trữ nó trong biến v.

            while v > 1: #Trong khi v lớn hơn 1, chúng ta tiếp tục tìm số nguyên dương nhỏ nhất chia hết cho v bằng cách sử dụng spf_local[v]. Sau đó, chúng ta thêm chỉ số i vào bucket tương ứng với số nguyên dương nhỏ nhất chia hết. Cuối cùng, chúng ta chia v cho số nguyên dương nhỏ nhất chia hết để tiếp tục tìm kiếm cho đến khi v trở về 1.

                p = spf_local[v] #Lấy số nguyên dương nhỏ nhất chia hết cho v từ mảng spf_local và lưu trữ nó trong biến p.

                if p in bucket: #Nếu p đã tồn tại trong bucket, chúng ta thêm chỉ số i vào danh sách hiện có trong bucket[p].
                    bucket[p].append(i)
                else: #Nếu p chưa tồn tại trong bucket, chúng ta tạo một danh sách mới chứa chỉ số i và gán nó cho bucket[p].
                    bucket[p] = [i]

                while spf_local[v] == p: #Trong khi số nguyên dương nhỏ nhất chia hết cho v vẫn là p, chúng ta tiếp tục chia v cho p để loại bỏ tất cả các bội của p trong quá trình tìm kiếm số nguyên dương nhỏ nhất chia hết tiếp theo.
                    v //= p

        visited = bytearray(n) #Tạo một mảng bytearray có kích thước n để đánh dấu các vị trí đã được thăm trong quá trình BFS. Mảng này được khởi tạo với giá trị 0, nghĩa là tất cả các vị trí ban đầu đều chưa được thăm. Khi một vị trí được thăm, chúng ta sẽ gán giá trị 1 cho vị trí đó trong mảng visited.
        visited[0] = 1 #Đánh dấu vị trí đầu tiên (chỉ số 0) là đã được thăm bằng cách gán giá trị 1 cho visited[0].

        used = bytearray(MX) #Tạo một mảng bytearray có kích thước MX để đánh dấu các số nguyên dương nhỏ nhất chia hết đã được sử dụng để nhảy đến các vị trí khác trong quá trình BFS. Mảng này được khởi tạo với giá trị 0, nghĩa là tất cả các số nguyên dương nhỏ nhất chia hết ban đầu đều chưa được sử dụng. Khi một số nguyên dương nhỏ nhất chia hết được sử dụng để nhảy đến các vị trí khác, chúng ta sẽ gán giá trị 1 cho vị trí tương ứng trong mảng used.

        q = [0] #Tạo một danh sách q để sử dụng như một hàng đợi trong thuật toán BFS. Ban đầu, chúng ta thêm chỉ số 0 vào hàng đợi, vì chúng ta bắt đầu từ vị trí đầu tiên của mảng nums.
        head = 0 #Tạo một biến head để theo dõi vị trí hiện tại trong hàng đợi q. Ban đầu, head được đặt là 0, nghĩa là chúng ta sẽ bắt đầu khám phá từ phần tử đầu tiên của hàng đợi.

        steps = 0 #Tạo một biến steps để đếm số bước nhảy đã thực hiện trong quá trình BFS. Ban đầu, steps được đặt là 0, nghĩa là chúng ta chưa thực hiện bất kỳ bước nhảy nào.

        #Để tối ưu hóa hiệu suất, các biến cục bộ được tạo ra để tránh việc truy cập vào các biến toàn cục trong vòng lặp BFS. Điều này giúp giảm thời gian truy cập và cải thiện hiệu suất của thuật toán.
        nums_local = nums #Tạo một biến cục bộ nums_local để truy cập vào mảng nums trong vòng lặp BFS.
        visited_local = visited #Tạo một biến cục bộ visited_local để truy cập vào mảng visited trong vòng lặp BFS.
        used_local = used #Tạo một biến cục bộ used_local để truy cập vào mảng used trong vòng lặp BFS.
        bucket_local = bucket #Tạo một biến cục bộ bucket_local để truy cập vào từ điển bucket trong vòng lặp BFS.

        append = q.append #Tạo một biến cục bộ append để truy cập vào phương thức append của danh sách q trong vòng lặp BFS. Điều này giúp giảm thời gian truy cập và cải thiện hiệu suất của thuật toán khi thêm phần tử vào hàng đợi.

        while head < len(q): #Trong khi head vẫn còn trong phạm vi của hàng đợi q, chúng ta tiếp tục thực hiện BFS để khám phá các vị trí tiếp theo. Vòng lặp này sẽ tiếp tục cho đến khi chúng ta đã khám phá tất cả các vị trí có thể hoặc tìm thấy vị trí cuối cùng (n - 1).

            level_end = len(q) #Lưu trữ độ dài hiện tại của hàng đợi q vào biến level_end. Điều này giúp chúng ta biết được số lượng phần tử trong hàng đợi tại cấp độ hiện tại của BFS, từ đó chúng ta có thể xử lý tất cả các phần tử trong cấp độ đó trước khi tăng số bước nhảy (steps) lên 1.

            while head < level_end: #Trong khi head vẫn còn trong phạm vi của cấp độ hiện tại (level_end), chúng ta tiếp tục khám phá các vị trí tiếp theo từ hàng đợi q. Vòng lặp này sẽ xử lý tất cả các phần tử trong cấp độ hiện tại trước khi tăng số bước nhảy (steps) lên 1.

                i = q[head] #Lấy phần tử tại vị trí head trong hàng đợi q và lưu trữ nó trong biến i. Đây là vị trí hiện tại mà chúng ta đang khám phá trong quá trình BFS.
                head += 1 #Tăng biến head lên 1 để chuyển sang phần tử tiếp theo trong hàng đợi q cho lần khám phá tiếp theo.

                if i == n - 1: #Nếu vị trí hiện tại (i) là vị trí cuối cùng của mảng nums (n - 1), điều đó có nghĩa là chúng ta đã đạt được mục tiêu và có thể trả về số bước nhảy đã thực hiện (steps) như kết quả của hàm.
                    return steps

                ni = i - 1 #Tính toán vị trí mới (ni) bằng cách nhảy sang trái từ vị trí hiện tại (i) bằng cách trừ 1. Đây là một trong những bước nhảy có thể thực hiện trong quá trình BFS.

                #Nếu vị trí mới (ni) hợp lệ (không âm) và chưa được thăm, đánh dấu nó đã được thăm và thêm nó vào hàng đợi để khám phá.
                if ni >= 0 and not visited_local[ni]:
                    visited_local[ni] = 1
                    append(ni)

                ni = i + 1 #Tính toán vị trí mới (ni) bằng cách nhảy sang phải từ vị trí hiện tại (i) bằng cách cộng 1. Đây là một trong những bước nhảy có thể thực hiện trong quá trình BFS.

                #Nếu vị trí mới (ni) hợp lệ (nhỏ hơn n) và chưa được thăm, đánh dấu nó đã được thăm và thêm nó vào hàng đợi để khám phá.
                if ni < n and not visited_local[ni]:
                    visited_local[ni] = 1
                    append(ni)

                x = nums_local[i] #Lấy giá trị tại vị trí hiện tại (i) trong mảng nums_local và lưu trữ nó trong biến x. Đây là giá trị mà chúng ta sẽ sử dụng để xác định các vị trí có thể nhảy đến dựa trên số nguyên dương nhỏ nhất chia hết cho x.

                #Nếu giá trị tại vị trí hiện tại lớn hơn 1 và là một số nguyên dương nhỏ nhất chia hết cho một số nguyên dương nào đó (spf_local[x] == x) và chưa được sử dụng để nhảy đến các vị trí khác (not used_local[x]), thì đánh dấu nó đã được sử dụng và thêm tất cả các vị trí có giá trị nguyên dương nhỏ nhất chia hết cho x vào hàng đợi để khám phá.
                if x > 1 and spf_local[x] == x and not used_local[x]:

                    used_local[x] = 1 #Đánh dấu số nguyên dương nhỏ nhất chia hết cho x đã được sử dụng để nhảy đến các vị trí khác bằng cách gán giá trị 1 cho used_local[x].

                    b = bucket_local.get(x) #Lấy danh sách các vị trí có giá trị nguyên dương nhỏ nhất chia hết cho x từ bucket_local bằng cách sử dụng phương thức get. Nếu x không tồn tại trong bucket_local, phương thức get sẽ trả về None.

                    if b: #Nếu danh sách b không rỗng (tức là có các vị trí có giá trị nguyên dương nhỏ nhất chia hết cho x), chúng ta tiếp tục xử lý các vị trí trong danh sách b.

                        for j in b: #Lặp qua tất cả các vị trí j trong danh sách b, đây là các vị trí có giá trị nguyên dương nhỏ nhất chia hết cho x. Nếu vị trí j chưa được thăm, chúng ta đánh dấu nó đã được thăm và thêm nó vào hàng đợi để khám phá.

                            if not visited_local[j]: #Nếu vị trí j chưa được thăm (tức là visited_local[j] == 0), chúng ta đánh dấu nó đã được thăm bằng cách gán giá trị 1 cho visited_local[j] và thêm nó vào hàng đợi để khám phá bằng cách gọi append(j).
                                visited_local[j] = 1
                                append(j)

                        del bucket_local[x] #Sau khi đã xử lý tất cả các vị trí trong danh sách b, chúng ta xóa mục bucket_local[x] để giải phóng bộ nhớ, vì chúng ta đã đánh dấu tất cả các vị trí có giá trị nguyên dương nhỏ nhất chia hết cho x là đã được thăm và không cần thiết phải giữ lại thông tin này nữa.

            steps += 1 #Sau khi đã xử lý tất cả các phần tử trong cấp độ hiện tại của BFS, chúng ta tăng số bước nhảy (steps) lên 1 để chuyển sang cấp độ tiếp theo của BFS.

        return -1 #Nếu chúng ta đã khám phá tất cả các vị trí có thể mà không đạt được vị trí cuối cùng (n - 1), điều đó có nghĩa là không thể đến được vị trí cuối cùng từ vị trí đầu tiên, vì vậy chúng ta trả về -1 để biểu thị rằng không có giải pháp nào tồn tại.