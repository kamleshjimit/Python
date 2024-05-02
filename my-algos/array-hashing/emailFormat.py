def numUniqueEmails(emails: list[str]) -> int:
    """
    Calculates the number of unique email addresses after processing rules.

    Rules:
    - Dots (.) in the local name are ignored.
    - Everything after the first plus (+) sign in the local name is ignored.

    Args:
        emails: A list of email addresses (strings).

    Returns:
        The number of unique email addresses after processing rules.

    >>> numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])
    2
    >>> numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"])
    3
    """

    unique_emails = set()

    for email in emails:
        # Split the email address into local name and domain parts
        local_name, domain = email.split("@")

        # Process the local name:
        # 1. Remove everything after the first plus sign
        local_name = local_name.split("+")[0]
        # 2. Remove all dots
        local_name = local_name.replace(".", "")

        # Combine the processed local name with the domain
        processed_email = local_name + "@" + domain

        # Add the processed email to the set if it's unique
        unique_emails.add(processed_email)

    return len(unique_emails)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
