multiples = [x*7 for x in range(1,11)]
print("multiple of 7 using list comprehension: {}".format(multiples))

#anothe example

languages = ['python','c','ruby','go','c++']
lengths = [len(language)for language in languages]
print("no of word in languages using list comprehension: {}".format(lengths))