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

def word_multiply(word: str, multi: int) -> str:
    return word * multi


text = 'python'
print(word_multiply(text, 2))


