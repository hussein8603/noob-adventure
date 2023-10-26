print(" Hej,Välkommen till Husseins frågesport!!! ")
name = input(" Vänligen ange ditt namn? ")
sport =input(" Vänligen ange ditt favorit sport? ")
team =input(" Ditt favorit lag inom fotboll är =) ?")
print(f" Alltså ditt namn är:{name}, ditt favorit sport är:{sport} och ditt favorit fotbollslag är:{team} Vad kul............")

print(" Nu ser vi till ifall du är verkligen intresserad av sport!!! ")
print(" Här kommer Husseins 5 magiska sport frågor!!!!!")

point = 0

print(" Fråga 1: ")
q1 = input (" Vilket fotbollslag vann senaste Champions Leauge? obs! ange svaret i små bokstäver!  ")
if q1 == "manchester city":
    print(f" rätt svar, du fick 7 poäng ")
    point =  point + 7
else:
    print (" fel svar, du förlorade 7 poäng ")
    point = point -7
 
print(" Fråga 2: ")   
q2 = input (" Vilket år föddes hockey spelaren Peter Forsberg? ")
if q2 == "1973":
    print(f" rätt svar, du fick 7 poäng ")
    point =  point + 7
else:
    print (" fel svar, du förlorade 7 poäng ")
    point = point - 7
 
print("Fråga 3:")       
q3 = input (" Vilket år spelade Sverige VM final mot Brasilien? ")
if q3 == "1958":
    print(f" rätt svar, du fick 7 poäng ")
    point =  point + 7
else:
    print (" fel svar, du förlorade 7 poäng ")
    point = point - 7
    
print(" Fråga 4: ")         
q4 = input (" Var kommer fotbollspelaren Karl-Heinz Rummenigge ifrån? obs! ange svaret i små bokstäver!  ")
if q4 == "tyskland":
    print(f" rätt svar, du fick 7 poäng ")
    point = point + 7
else:
    print(" fel svar, du förlorade 7 poäng ")
    point = point - 7
print(" Fråga 5: ")       
q5 = input (" Hur många VM guld medaljer har Sverige vunnit inom Hockey? ")
if q5 == "11":
    print(f" rätt svar, du fick 7 poäng ")
    point =  point + 7
else:
    print (" fel svar, du förlorade 7 poäng ")
    point = point - 7   

while True:
    print (" Ditt slutliga resultat är: ",point," poäng =)=)=) ")
    print(" Vilket fotbollslag har vunnit mest VM guld? ")
    val = input(" 1/Tyskland? 2/Brasilien? 3/Italien? ")
    if val in ( '1','2','3', ):
        try:
            print(" Hmmmmm...mmmm...DET ÄR:!!! ")
        except ValueError:
            print(" FEL inmatning. vänligen ange ett nummer. ")
            continue
        if val == '1':
            print(" fel svar =() ")
          
        elif val == '2':
            print(f" rätt svar, du har precis öppnat pandora box och har nu tillgång till de filosofiska stenarna!!! ")
           
        elif val == '3':
            print("fel svar =()")
         
                
        slut_steg = input(" Nu är du färdig med Husseins useless frågesport, vill avsluta? (ja/nej): ")
        if slut_steg == "ja":
          break
      