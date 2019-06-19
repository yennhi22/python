xs =[()] # list chứa 1 tuple( list không rỗng ,tuple rỗng)
print(xs)
print(xs[0])
res = [False] *2
if xs:#kiểm tra xem xs có rỗng hay không
    res[0]=True
if xs[0]:
    res[1]=True
print(res)
list =[ 5,1,2,3,4]
print(list)
tuple= ()
print(tuple)
#---------------------
# hàm đếm số bit của 1 số
def countBits(n):
    return n.bit_length()
print(countBits(5))
# c2
n=5
print(n.bit_length()) # đếm số bit cần có để biểu diễn 1 số
#------------------
def modulus(n):
    if  type(n)==int: # hàm type lấy ra kiểu dữ liệu
        return n % 2
    else:
        return -1

print(modulus(4.3))
x=3.24
print(type(x))
#---------------
# sắp xếp
def simpleSort(arr):

    n = len(arr)

    for i in range(n): # range(n) là hàm phạm vi, nếu chỉ có 1 thông số thì mặc định là từ 0 đến n
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
    return arr
print(simpleSort(list))
print(range(5))
def sapxep
#------------------





