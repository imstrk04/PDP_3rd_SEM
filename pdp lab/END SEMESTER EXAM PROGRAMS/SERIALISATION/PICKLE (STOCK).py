
import pickle
class stock:

    def __init__(self,name,language,company,rate,date,time):
        self.name=name
        self.language=language
        self.company=company
        self.rate=rate
        self.date=date
        self.time=time

    def display_stock(self):
        return f'{self.company},{self.rate},{self.date},{self.time}'


if __name__=='__main__':
    #getting name and language from the user 
    def get_user_input():
        name=input('enter your name(type exit to leave)')
        if name.lower()=='exit':
            return None,None
        else:
            language=input('enter your preferred language')
        return name,language

    #creating the stock list
    stock_list=[]

    #getting user_name and appending the lang and name along with other details 
    while True:
        user_name,pref_lang=get_user_input()
        
        if user_name is None:
            break
        else:
            hcl_stock=[user_name,pref_lang,'hcl','1,250,000','16.06.05','10.5AM']
            stock_list.append(hcl_stock)

            
    #storing the list object in the pickle file
    with open('stock.txt','wb')as file:
        pickle.dump(stock_list,file)

    with open('stock.txt','rb')as file:
        content=pickle.load(file)
    print('file content',content)
