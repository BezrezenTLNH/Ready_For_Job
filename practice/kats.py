# def get_count(sentence):
#     return sum(['a, e, i, o, u'] in sentence)


# sent = "aeiou"
# res = ['a', 'e', 'i', 'o', 'u']
# print(sum(c in 'aeiou' for c in sent))


# ex = "This website is for losers LOL!"
# vowels = 'aeiou'
# print(''.join([i for i in ex if i.lower() not in 'aeiou']))

# def square_digits(num):
#     return int(''.join([str(int(n)**2) for n in str(num)]))

# def duplicate_encode(word):
#     return ''.join(['(' if word.lower().count(w) == 1 else ')' for w in word.lower()])

# def word_multiply(word: str, multi: int) -> str:
#     return word * multi

# def persistence(n):
#     count = 0
#     while n >= 10:
#         result = 1
#         while n > 1:
#             result *= n % 10
#             n //= 10
#         n = result
#         count += 1
#
#     return count

# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
#     # return ' '.join([str(ord(char)%32) for char in text if char.isalpha()])

# def order(sentence):
#
#     return ' '.join(sorted(sentence.split(), key=lambda w: sorted(w)))
#
# def narcissistic(value):
#     return sum([int(val)**len(str(value)) for val in str(value)]) == value


# def max_sequence(arr):
#     max_ending_here = max_so_far = 0
#
#     for num in arr:
#         max_ending_here = max(0, max_ending_here + num)
#         max_so_far = max(max_so_far, max_ending_here)
#
#     return max_so_far

def cakes(recipe, available):
    max_cakes = float('inf')

    for ingredient, amount in recipe.items():
        if ingredient not in available or available[ingredient] < amount:
            return 0
        max_cakes = min(max_cakes, available[ingredient] // amount)

    return max_cakes
