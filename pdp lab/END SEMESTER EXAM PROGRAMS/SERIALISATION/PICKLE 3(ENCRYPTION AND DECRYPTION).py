import re
import pickle
import base64


#using base64 encoding we can encode and decode to get the same password

class pass_protection:

    def __init__(self,input_file):
        self.input_file=input_file

    def encrypt(self):

        with open(self.input_file,'rb') as file:
            user_dict=pickle.load(file)

        for username,password in user_dict.items():
            encoded_pass=base64.b64encode(password.encode('utf-8')).decode('utf-8')
            user_dict[username]=encoded_pass

        with open(self.input_file,'wb')as file:
            pickle.dump(user_dict,file)

        with open(self.input_file,'rb') as file:
            encrypted_user_dict=pickle.load(file)

        return encrypted_user_dict

    def decrypt(self, encrypted_data, user_name, input_pass):
        encrypted_pass = encrypted_data[user_name]
        decoded_pass = base64.b64decode(encrypted_pass).decode('utf-8')

        if decoded_pass == input_pass:
            
            return 'Passwords match 100%'
        else:
            return 'Passwords do not match'



user1_file={'srihari':'12345','venkat':'4532'}
with open('user1.txt','wb')as file:
    pickle.dump(user1_file,file)
    
User1=pass_protection('user1.txt')
encrypted_data=User1.encrypt()
print('encrypted',encrypted_data)

decrypted_data=User1.decrypt(encrypted_data,'srihari','12345')
print('decrypted',decrypted_data)

                



        








