import pickle
import re


class Spamdetection:
    def __init__(self,spam_file):
        self.spam_file=self.load_words(spam_file)

    #loading default spam words 
    def load_words(self,spam_file):
        try:
            with open(spam_file,'rb')as file:
                content=pickle.load(file)
                
        #except the empty file error
        except(FileNotFoundError,EOFError):
            spam_words=['danger','warning','lottery']
            
            with open(spam_file,'wb')as file:
                pickle.dump(spam_words,file)
            return spam_words
        return content

    #replace spam words with re functions
    def replace_spam_text(self,test_file):
        for i in self.spam_file:
            test_file=re.sub(r'\b'+re.escape(i)+r'\b','*****',test_file)
        return test_file

    #replace spam words with spaces or any words 
    def modify_file(self,input_file,output_file):

        with open(input_file,'rb')as file:
            content=pickle.load(file)

        modified_content=self.replace_spam_text(content)

        with open(output_file,'wb') as file:
            pickle.dump(modified_content,file)

        with open(output_file,'rb') as file:
            replaced_texts=pickle.load(file)
        return replaced_texts

    #percentage of spam content
    def analyze_percentage(self,test_file):
        with open(test_file,'rb')as file:
            file_content=pickle.load(file)

        total_words=len(re.findall(r'\b\w+\b',file_content))
        spam_words=sum(1 for i in self.spam_file if re.search(r'\b'+re.escape(i)+r'\b',file_content))

        spam_percentage=(spam_words/total_words)*100

        if spam_percentage>40:
            print('spam detected')
        else:
            print('spam level less than 40 safe to use')
        print('total words',total_words,'spam words',spam_words)
        
        
            
            
#writing content to test.txt
content_to_write=''' hi hello im giving you a warning
you are in danger '''

with open('test.txt','wb') as file:
    pickle.dump(content_to_write,file)

Spamfile=Spamdetection('bag_of_spam.txt')
resultant_file=Spamfile.modify_file('test.txt','modified_test.txt')
print(resultant_file)
spam_percentage=Spamfile.analyze_percentage('test.txt')


    

