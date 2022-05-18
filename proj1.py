file_contents="To upload your text file, run the following cell that contains all the code for a custom uploader widget. Once you run this cell, a Browse button should appear below it. Click this button and navigate the window to locate your saved text file."
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    frequencies ={}
    file_contents = file_contents.split()
    for word in file_contents:
        for letter in word:
            if letter in punctuations:
                letter =""
    for word in file_contents:
        if word.lower() not in frequencies:
            frequencies[word.lower()]=1
        else:
            frequencies[word.lower()]+=1
    print(frequencies)
calculate_frequencies(file_contents)