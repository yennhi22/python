print("\a chu y")
print("\b space")
# print("\cx ")
# print("\Cx")
# print("\e")
print("\f")
#print("\M-\Cx")
print ('C:\\nowhere')
print (r'C:\\nowhere')
print (u'Hello, world!')
str = "this is string example....wow!!!";
print ("str.capitalize() : ", str.capitalize()) # viết hoa ký tự đầu tiên
#--------------
# thêm bnhaan vật phụ a vào đầu và cuối để chiều dài của chuỗi là 40
print ("str.center(40, 'a') : ", str.center(40, 'a'))
print ("str.center(41, 'a') : ", str.center(41, 'a'))
#-----------
# đếm xem chuỗi con xuất hiện trong phạm vi này bao nhiêu lần
sub = "i";
print ("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow";
print ("str.count(sub) : ", str.count(sub))
#--------------------------------


print ("Encoded String: " +str.encode('UTF-8','strict') )
print ("Decoded String: " + str.decode('UTF-8','strict'))