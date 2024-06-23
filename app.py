#zad 1

a= int(input("Podaj wartość zmiennej a: "))
b=int(input("Podaj wartość zmiennej b: "))
if a >= 0 and a < 10 and b >= 0 and b < 10:
 il=a*b
 print("Iloczyn wynosi: " , il)
else:
 print("Dane poza zakresem od 0 do 9!")
 
 jezyk = input(str("Podaj nazwę ulubionego języka programowania"))
if jezyk == "Python":
    print("Zostań naukowcem od przetwarzania danych")
elif jezyk == "Java":
    print("Twórz aplikacje na urządzenia mobilne.")
elif jezyk =="c#":
    print("Stwórz grę multimedialną w Unity")
elif jezyk =="PHP":
    print("Możesz tworzyć strony intenetowe")
elif jezyk =="SQL":
    print("Rozwijaj systemy bazodanowe")
elif jezyk =="":
    print("Nie podales jezyka")
