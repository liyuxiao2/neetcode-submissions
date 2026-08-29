class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for e in emails:
            local, domain = e.split("@")

            plus = local.find("+")

            local = local[:plus] if plus > 0 else local

            local = local.replace(".", "")

            seen.add((local, domain))
        
        return len(seen)