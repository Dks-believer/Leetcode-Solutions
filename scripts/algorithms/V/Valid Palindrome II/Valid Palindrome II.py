// Runtime: 7032 ms (Top 5.01%) | Memory: 643 MB (Top 5.03%)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        has_deleted = False

        def compare(s, has_deleted):

            if len(s) <= 1:
                return True

            if s[0] == s[-1]:
                return compare(s[1:-1], has_deleted)
            else:
                if not has_deleted:
                    return compare(s[1:], True) or compare(s[:-1], True)
                else:
                    return False

        return compare(s, has_deleted)