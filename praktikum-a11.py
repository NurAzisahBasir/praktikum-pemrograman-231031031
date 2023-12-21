#Fungsi Rekursif Fibonacci 
def fibonacci(n):
    if n<0:
        print('Tidak ada bilangan yang bernilai negatif')
    elif n==0 or n==1:   
       return n    
    else:       
        return fibonacci(n-1) + fibonacci(n-2) 
#Program Utama
hasil=fibonacci(20)
print("Fibonacci(20) = %d" % hasil)

fibb = int(input('Masukkan sebuah bilangan: '))
if fibb<0:
    print('Tidak ada bilangan yang bernilai negatif')
else:
    hasil_fib = fibonacci(fibb)
    print(f'Fibonacci({fibb}) = {hasil_fib}')
    

