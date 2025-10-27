"""
Código da aula de Liguagens de Pogramação

Date: 10/10/2025

Authors: Davi Dressler e Elias Vieira

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter


np.random.seed(42)

N=180
base_temp=22.0
amp=8.0
noise_temp=1.5
noise_energy=10.0
 

data_inicial = np.datetime64("2025-01-01")
dates = np.arange(data_inicial, data_inicial + N)

t = np.arange(N)

ruido_temp = np.random.normal(0, noise_temp, N)
temp = base_temp + amp*np.sin(2*np.pi*t/30) + ruido_temp

ruido_energy = np.random.normal(0, noise_energy, N)
energy = 200 + 5*np.abs(temp - base_temp) + ruido_energy

spykes = np.random.choice(N, 3, replace=False)
for spyke in spykes:
    energy[spyke] += 80.0

df = pd.DataFrame({"temp": temp, "energy": energy}, index=dates)

print(f"DataFrame Transposto:\n{df.T}")

print("#"*60)

print(f"Primeiras 10 linhas do DataFrame:\n{df.head(10)}")

print("#"*60)

print(f"Estatísticas do DataFrame:\n{df.describe()}")


#Cálculo do HDD e CDD
df['HDD'] = (base_temp - df['temp']).clip(0, None)
df['CDD'] = (df['temp'] - base_temp).clip(0, None)

#Calculo da média movel de 7 dias
kernel = np.ones(7)/7
media_movel = np.convolve(df["temp"], kernel, mode= "same")

df["temp_ma7"] = media_movel

fig = plt.figure(figsize= (12,8))
gs = fig.add_gridspec(2, 2, hspace= 0.35, wspace= 0.25)

locator = AutoDateLocator()  
fmt = ConciseDateFormatter(locator)


#Gráfico 1
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(df["temp"], lw= 1.0, label= "Temperatura")
ax1.plot(df["temp_ma7"], lw= 2.0, label= "Média móvel (7d)", color= "darkorange")

ax1.fill_between(x= dates, y1=df["temp"] , y2= base_temp, where= df["HDD"], color= "skyblue", alpha= 0.3, label= "Acima da temperatura base")
ax1.fill_between(x= dates, y1=df["temp"] , y2= base_temp, where= df["CDD"], color = "red", alpha= 0.15, label = "Abaixo da temperatura base")

ax1.set_title("Série histórica da temperatura")
ax1.set_ylabel("°C", rotation = 0)
ax1.legend(bbox_to_anchor=(0.55, -0.1), fontsize= 5, ncol= 2)

ax1.xaxis.set_major_locator(locator)
ax1.xaxis.set_major_formatter(fmt)

      
#Gráfico 2
ax2 = fig.add_subplot(gs[0,1])
ax2.scatter(x= df["temp"], y= df["energy"], alpha= 0.7)

df_spykes = df[df.index.isin(dates[spykes])]

ax2.scatter(x= df_spykes["temp"], y= df_spykes["energy"], alpha= 0.7, color= "red")

ax2.set_title("Temperatura x Energia")
ax2.set_xlabel("°C")
ax2.set_ylabel("KW/h")

for spyke in spykes:
    ax2.annotate("spike", (df["temp"].iloc[spyke], df["energy"].iloc[spyke]),
                 xytext=(8, 8), textcoords="offset points",
                 arrowprops=dict(arrowstyle="->", lw=0.8) , 
                 ha= "right", va= "center_baseline")


# Gráfico 3
ax3 = fig.add_subplot(gs[1, 0])

intervalos = [10, 14, 18, 22, 26, 30, 34]
ax3.hist(df["temp"], bins= intervalos, color= "skyblue")

n, bins, patches = ax3.hist(df["temp"], bins= intervalos)

for i in range(len(n)):
    altura_barra = n[i]
    pos_x = (bins[i] + bins[i+1]) / 2
    pos_y = altura_barra + 3  
    ax3.text(pos_x, pos_y, f'{int(altura_barra)}', ha='center', va='center_baseline')
    
ax3.set_xticks(bins)
ax3.set_ylabel("Frequência")
ax3.set_xlabel("Temperatura (ºC)")
ax3.set_title("Histograma da Temperatura")

ax3.set_ylim(top=51)


#Gráfico 4
weekly = df.resample("W").agg({"energy":"sum", "temp":"mean"})
ax4 = fig.add_subplot(gs[1, 1])

ax4.bar(x= weekly.index, height= weekly["energy"], width=5, align="center", label="Energia (semanal)")

ax4_t = ax4.twinx()  
ax4_t.plot(weekly.index, weekly["temp"], marker="o", lw=1.8, label="Temp média (semanal)", color= "darkorange")

ax4.legend(bbox_to_anchor=(0.27, -0.1), fontsize = 6)
ax4_t.legend(bbox_to_anchor=(0.58, -0.1), fontsize= 6)
 

ax4.set_title("Consumo semanal de energia")
ax4.set_ylabel("KW/h")

ax4.xaxis.set_major_locator(locator)
ax4.xaxis.set_major_formatter(fmt)

fig.tight_layout()
plt.savefig('numpy_matplotlib.png', dpi= 150)

plt.show()

