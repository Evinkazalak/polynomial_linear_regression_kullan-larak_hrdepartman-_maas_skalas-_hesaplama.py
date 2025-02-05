# -*- coding: utf-8 -*-
"""Polynomial_Linear_Regression_Kullanılarak_HRDepartmanı_Maas_Skalası_Hesaplama.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-kVdNgu3INqdVkOYVwlR0MumG3IVnDtW
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df=pd.read_csv("polynomial.csv",sep=";")

df

#veri setine bir bakalım
plt.scatter(df['deneyim'],df['maas'])
plt.xlabel('Deneyim (yıl)')
plt.ylabel('Maaş')

#mevcut çizim 1.png adıyla kaydedilecek ve belirtilen çözünürlükte diskte saklanacaktır
plt.savefig('1.png',dpi=300)
plt.show()

# 1 tane polynomial regression nesnesi oluşturması için polynomialFeatures fonksiyonunu çağırıyoruz

polynomial_regression=PolynomialFeatures(degree=4) #n :polinom derecesi
x_polynomial=polynomial_regression.fit_transform(df[['deneyim']])

#regresyon modelimizi mevcut gerçek verilerle eğitiyoruz.

reg=LinearRegression()
reg.fit(x_polynomial,df['maas'])

#elimizdeki verilere göre modelimiz nasıl bir sonuç grafiği oluşturuyor onu görelim

y_head=reg.predict(x_polynomial)
plt.plot(df['deneyim'],y_head,color='red',label='polynomial regression')
plt.legend()

plt.scatter(df['deneyim'],df['maas'])
plt.show()

#polinom derecesini arttırdığımızda daha güzel fit ediyor mu ona bakalım

x_polynomial1=polynomial_regression.fit_transform([[4.5]])
reg.predict(x_polynomial1)