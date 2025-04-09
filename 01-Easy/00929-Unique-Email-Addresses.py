"""929. Unique Email Addresses
Link: https://leetcode.com/problems/unique-email-addresses/
Difficulty: Easy
Description: Every valid email consists of a local name and a domain name, separated by the '@' sign.
Besides lowercase letters, the email may contain one or more '.' or '+'.
For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent
there will be forwarded to the same address without dots in the local name.
Note that this rule does not apply to domain names.
For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
This allows certain emails to be filtered. Note that this rule does not apply to domain names.
For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.
Given an array of strings emails where we send one email to each emails[i], return the number of
different addresses that actually receive mails."""

from typing import List


class Solution:
    @staticmethod
    def numUniqueEmails(emails: List[str]) -> int:
        """Optimal Solution: Hash Set and String Manipulation.
           Time Complexity: O(n), Space Complexity: O(n)"""
        # Initialize a hash set to store the unique email addresses
        unique_emails = set()

        # Iterate through all the emails
        for email in emails:
            # Split the email address into the local name and domain name
            local_name, domain_name = email.split('@')

            # Remove the periods in the local name and ignore the characters after the '+'
            local_name = local_name.replace('.', '').split('+')[0]

            # Add the email address to the hash set
            unique_emails.add(local_name + '@' + domain_name)

        # Return the number of unique email addresses
        return len(unique_emails)


# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com",
# "testemail+david@lee.tcode.com"], Output: 2
assert Solution.numUniqueEmails(["test.email+alex@leetcode.com",
                                 "test.e.mail+bob.cathy@leetcode.com",
                                 "testemail+david@lee.tcode.com"]) == 2

# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"], Output: 3
assert Solution.numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3

print("All unit tests are passed.")
