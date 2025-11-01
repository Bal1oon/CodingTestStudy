from itertools import combinations

l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
for password in combinations(alpha, l):
    vowel_count = sum(1 for char in password if char in vowels)
    consonant_count = l - vowel_count
    if vowel_count >= 1 and consonant_count >= 2:
        print(''.join(password))