class Solution:
    def compress(self, chars: List[str]) -> int:
        r, w = 0, 0

        while r < len(chars):
            cnt = 0
            cur_char = chars[r]

            while r < len(chars) and chars[r] == cur_char:
                cnt += 1
                r += 1

            chars[w] = cur_char
            w += 1

            if cnt > 1:
                for digit in str(cnt):
                    chars[w] = digit
                    w += 1
            
        return w
