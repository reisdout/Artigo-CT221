
petro = readmatrix('PETR3.SA.csv');
petro_val = petro(:,5)
H_petro = hurst(petro_val)

embraer = readmatrix('EMBR3.SA.csv');
embraer_val = embraer(:,5)
H_embraer = hurst(embraer_val)

vale = readmatrix('VALE3.SA.csv')
vale_val = vale(:,5)
H_vale = hurst(vale_val)

H_petro
H_embraer
H_vale



