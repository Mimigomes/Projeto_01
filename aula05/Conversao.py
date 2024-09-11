class Conversao:
     
     def velocidade():
         kmh = [75.4,30.6,120,32.8,20.8]
         mph = [round(x/1.61,2)for x in kmh]
         x = 0
         while(x<5):
               print(kmh[x],"Kmh em pes Mph ",mph[x])
               x += 1
     
     def temperatura():
          celsius = [45,30,12.5,32.6,50]
          fehrenheit = [round((x*1.8)+32,2) for x in celsius]
          x = 0
          while(x<5):
               print(celsius[x],"Celsius em pes são ",fehrenheit[x])
               x += 1
          
     def altura():
          metro = [10,100,500,250,1000]
          pes = [round (x/0.3048,2) for x in metro]
          x = 0
          while(x<5):
               print(metro[x],"Metro em pes são ",pes[x])
               x += 1
     
     def idade():
          anos =[12,29,45,2,5,16]
          meses = [x*12 for x in anos]
          x = 0
          while(x<=5):
               print(anos[x],"Anos em meses são ",meses[x])
               x =+1
    