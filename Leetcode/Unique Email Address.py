class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        ans = set()

        for ele in emails:
            domain = ele.split('@')[1]
            if '+' in ele:
                email = ele.partition('+')[0].replace('.','')
            else:
                email = ele.split('@')[0].replace('.','')
            ans.add(email + '@' + domain)

        return len(ans)

sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(sol.numUniqueEmails(emails))