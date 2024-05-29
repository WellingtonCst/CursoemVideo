medida = float(input('Digite uma distancia em metros:'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a:\n Quilometro {}km\n Hectômetro {}hm\n Decâmetro {}dam\n Decímêtro {}dm\n centímêtro {}cm\n milimêtro {}mm'.format(medida,km,hm,dam,dm,cm,mm))
