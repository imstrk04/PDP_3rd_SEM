def spam_words(filename):
    with open(filename, 'r') as f:
        spam_words = [word.strip() for word in f.readlines()]
        return spam_words

def check_file(testfile, spam_words):
    with open(testfile, 'r') as f:
        content = f.read()
        words = content.split()
        count = sum(word in spam_words for word in words)
        spam_percentage = (count / len(words)) * 100

        if spam_percentage >= 40:
            print("Spam File!")
            modified_content = replace_spam_content(content, spam_words)
            with open('modified_spam.txt', 'w') as modified_file:
                modified_file.write(modified_content)
            print("Modified content saved to modified_spam.txt.")
        else:
            print("Genuine file")

def replace_spam_content(content, spam_words):
    for word in spam_words:
        content = content.replace(word, '')
    return content

if __name__ == '__main__':
    spam_words_list = spam_words('bag_of_spam.txt')
    check_file('bag_of_spam.txt', spam_words_list)
