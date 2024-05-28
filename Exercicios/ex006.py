n = int(input('Digite um valor:'))
d = n*2
t = n*3
r = n**(1/2)
print(' O dobro de {} vale {}\n O triplo de {} vale {}\n A raiz quadrada de {} é igual a {:.2f}'.format(n, d, n, t, n, r))

#ou podemos fazer da seguinte maneira:
#print('O dobro de {} vale {}\n O triplo de {} vale {} \n A raiz quadrada de {} é igual a {}'.format(n, (n*2), n, (n*3), n, (n**(1/2))))