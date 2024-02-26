# São imutaveis
t1 = (1,2,3,4,5,6,5,5,5,7,8)

print(t1.count(5)) #retorna quantas occorencias existe na lista
print(3 in t1) 

# Todos os metodos que alteram listas não podem ser usados em tublas
# - sort(), append(), pop(), reverse()...

#é possivel criar lista apartir de tublas:
grupo17 = list(t1)
