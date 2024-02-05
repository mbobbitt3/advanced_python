#find numbers 1-1000 divisble by 7
def find_mod():
	good_nums = [i for i in range(0,1001) if i %7 == 0]
	print(good_nums)

def contain_3():
	nums = [i for i in range(0,1001) if str(i).find('3') ] 
	print(nums)
#contains_3()

def vowels(string):
	vowels = ['a','e','i', 'o', 'u']
	word = [i for i in string if i.lower() not in vowels]
	full = ''.join(word)
	print(full)
#find_mod()
#vowels("california")
def four_letter_word(string):
	words = string.split(" ")
	four_l_words = [i for i in words if len(i) < 4]
	print(four_l_words)
#four_letter_word("the quick brown fox jumped over the small gray dog")
def word_len(string):
	words =  string.split(" ")
	wordlen = {word:len(word) for word in words}
	print(wordlen)

#word_len("the quick brown fox jumped over the small gray dog")

def nested_mod():
	good_nums = [i for i in range(0,1001) if [j for j in range(2,10) if i % j == 0]]
	print(good_nums)
nested_mod()
