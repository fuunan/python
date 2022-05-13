def user_imformationes(first,last,**imformation):
    imformation['first name']=first
    imformation['last  name']=last
    return imformation
imformation=user_imformationes('y','jm',location='nanchang',field='biology')
print(imformation)