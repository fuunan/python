def send_messages(sending,sended):
    while sending:
        sended_message=sending.pop()
        print(f"'{sended_message}' has be sended")
        sended.append(sended_message)




list1=['hello world','how are you','i m fine']
list2=[]

send_messages(list1,list2)
print(list1)
print(list2)