class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        #first we create a set, and in that set we will have the unique emails
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            #we handle the + rule - we omit everything that is after the + 
            local = local.split('+')[0]
            local = local.replace('.',"")
            unique_emails.add(f"{local}@{domain}")
        return len(unique_emails)