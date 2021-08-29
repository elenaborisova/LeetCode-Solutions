def num_unique_emails(emails):
    unique_emails = set()

    for email in emails:
        sep_idx = email.index('@')
        local_name = email[:sep_idx]
        domain_name = email[sep_idx + 1:]

        if '+' in local_name:
            plus_idx = local_name.index('+')
            local_name = local_name[:plus_idx]

        local_name = local_name.replace('.', '')
        full_email = local_name + '@' + domain_name
        unique_emails.add(full_email)

    return len(unique_emails)


print(num_unique_emails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
print(num_unique_emails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]))
