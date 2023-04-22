# Lognormal Function
f(x) = A/x * exp(-1* ((log(x) - mu)**2/(2*sigma**2)))

# Parameters
xc=12.56
mu = 2.5306
sigma = 0.000185
t1 = xc - 0.006
t2 = xc + 0.01
A = 90000

# Fit Function
set fit errorvariables
fit [xc-0.006:xc+0.01] f(x) '/home/ubuntu/Documents/Dissertation/Emissão_de_matéria_em_Cristais_Iônicos _Calculo_Tempo_de_Voo_de_Ions_Secundarios/2_LiF_6MeV_Cu_electron_gun/python_programs/Concat_DataFrame.dat' using 2:44 via A
fit [xc-0.006:xc+0.01] f(x) '/home/ubuntu/Documents/Dissertation/Emissão_de_matéria_em_Cristais_Iônicos _Calculo_Tempo_de_Voo_de_Ions_Secundarios/2_LiF_6MeV_Cu_electron_gun/python_programs/Concat_DataFrame.dat' using 2:44 via sigma
fit [xc-0.006:xc+0.01] f(x) '/home/ubuntu/Documents/Dissertation/Emissão_de_matéria_em_Cristais_Iônicos _Calculo_Tempo_de_Voo_de_Ions_Secundarios/2_LiF_6MeV_Cu_electron_gun/python_programs/Concat_DataFrame.dat' using 2:44 via mu
fit [xc-0.006:xc+0.01] f(x) '/home/ubuntu/Documents/Dissertation/Emissão_de_matéria_em_Cristais_Iônicos _Calculo_Tempo_de_Voo_de_Ions_Secundarios/2_LiF_6MeV_Cu_electron_gun/python_programs/Concat_DataFrame.dat' using 2:44 via A, sigma, mu

set print 'fit_parameters.txt'
print A,sigma,mu

#Plot
set xrange [t1:t2]
plot '/home/ubuntu/Documents/Dissertation/Emissão_de_matéria_em_Cristais_Iônicos _Calculo_Tempo_de_Voo_de_Ions_Secundarios/2_LiF_6MeV_Cu_electron_gun/python_programs/Concat_DataFrame.dat' using 2:44 title 'data',\
f(x) title 'best lognorm curve'
set xlabel "Tempo de voo [µs]
set ylabel "Contagem"


