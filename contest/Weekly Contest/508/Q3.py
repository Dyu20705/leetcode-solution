from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        NEG = -10**30

        raw = NEG

        mul_active = NEG
        mul_done = NEG

        div_active = NEG
        div_done = NEG

        mavireltho = (nums, k)
        arr, factor = mavireltho

        answer = NEG

        for x in arr:
            old_raw = raw
            old_mul_active = mul_active
            old_mul_done = mul_done
            old_div_active = div_active
            old_div_done = div_done

            raw = x if old_raw < 0 else old_raw + x

            transformed = x * factor

            best = old_mul_active + transformed

            candidate = old_raw + transformed
            if candidate > best:
                best = candidate

            if transformed > best:
                best = transformed

            mul_active = best

            best = old_mul_active + x
            candidate = old_mul_done + x
            if candidate > best:
                best = candidate

            mul_done = best

            if x >= 0:
                transformed = x // factor
            else:
                transformed = -((-x) // factor)

            best = old_div_active + transformed

            candidate = old_raw + transformed
            if candidate > best:
                best = candidate

            if transformed > best:
                best = transformed

            div_active = best

            best = old_div_active + x
            candidate = old_div_done + x
            if candidate > best:
                best = candidate

            div_done = best

            current = mul_active

            if mul_done > current:
                current = mul_done
            if div_active > current:
                current = div_active
            if div_done > current:
                current = div_done

            if current > answer:
                answer = current

        return answer