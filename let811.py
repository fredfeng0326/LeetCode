# 811. Subdomain Visit Count
import collections
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for item in cpdomains:
            number = int(item.split(' ')[0])
            domains = item.split(' ')[1].split('.')
            times = len(domains)
            for time in range(times):
                key = '.'.join(domains[time:])
                n = number
                if key in dic:
                    dic[key] += n
                else:
                    dic[key] = n
            out = []
            for key, val in dic.items():
                out.append(str(val) + ' ' + str(key))
        return out

    def subdomainVisits2(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                ans[".".join(frags[i:])] += count
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]


a = Solution()
print(a.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
print(a.subdomainVisits2(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))


a = [('mail.com', 901), ('yahoo.com', 50), ('google.mail.com', 900), ('wiki.org', 5), ('org', 5), ('intel.mail.com', 1), ('com', 951)]
print ["{} {}".format(ct, dom) for dom, ct in a]

