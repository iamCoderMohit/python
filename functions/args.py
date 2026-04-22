# *args - Arbitrary Arguments and **kwargs - Arbitrary Keyword Arguments

# def sum1(*nums):
#     # ans = sum(nums)
#     # print(ans)

#     #(1, 2, 3, 3)

#     for val in nums:
#         print(val)

# sum1(1, 2, 3, 3)

# tuple

# {word: meaning}
# {key: value}

def info(**details):
    #dictionary
    details['clg'] = 'abc'
    print(details)

# info(name = "Mohit", clg = "abc", job = "SE")
# info(name = "Mohit", clg = "abc")
# info(kdhfias = "Mohit", luiasdfhi = "abc", akdgsaf = 12)

a = {
    'name': 'mohit',
    'clg': 'abc'
}

a['clg'] = 'def'
a['job'] = 'se'
print(a)