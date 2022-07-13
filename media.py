from genrnd import fun_genrnd as genrnd
import statistics

print("Funcion que calcula la media del vector obtenido en genrnd: ")
genrnd()
mean = statistics.mean(genrnd())
print("La media es: ",mean)