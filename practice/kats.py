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

# def cakes(recipe, available):
#     # max_cakes = float('inf')
#     #
#     # for ingredient, amount in recipe.items():
#     #     if ingredient not in available or available[ingredient] < amount:
#     #         return 0
#     #     max_cakes = min(max_cakes, available[ingredient] // amount)
#     #
#     # return max_cakes
#     return min(available.get(k, 0) / recipe[k] for k in recipe)
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return -(-self.item_count() // self.items_per_page)

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        if page_index == self.page_count() - 1:
            return self.item_count() % self.items_per_page or self.items_per_page
        return self.items_per_page

    def page_index(self, item_index):
        if item_index < 0 or item_index >= self.item_count():
            return -1
        return item_index // self.items_per_page


# def scramble(s1, s2):
#     # return [i for i in s2 if s2.count(i) <= s1.count(i)] == list(s2)  ## kinda slow
#     return all(s1.count(x) >= s2.count(x) for x in set(s2))

# def decode_morse(morse_code):
#     # Remember - you can use the preloaded MORSE_CODE dictionary:
#     # For example:
#     # MORSE_CODE['.-'] = 'A'
#     # MORSE_CODE['--...'] = '7'
#     # MORSE_CODE['...-..-'] = '$'
#     decoded_message = ''
#     for word in morse_code.split('   '):
#         for letter in word.split():
#             decoded_message += MORSE_CODE[letter]
#         decoded_message += ' '
#     return decoded_message.strip()
