request=input("Введите название песни в формате \"НазваниеПесни.txt\" из предложенных: Believer, Burn out, Demons, Warriors, Whatever it takes ") 
heads_count=0 
lines_count=0 
chorus_count=0 
#letters=["\n","[Verse1]","[Pre-Chorus]", "[Chorus]", "[Verse 2]", "[Bridge]"] 
#new_file=open(request, "w+") 
#new_file.write() 
with open(request, "r") as f: 
    head="[Verse 1]" #просто чтобы посчитать заголовки, задаем это 
    for line in f: 
        if line!="\n" and head=="[Verse 1]": 
            heads_count+=1 #считаем заголовки 
            head="notVerse 1" 
        elif line=="\n": 
            head="[Verse 1]" 
        if line.strip(): 
            lines_count+=1 #считаем все строки не считая пустых 
        print(line) 
        chorus="[Chorus]" 
         
        #if line=="[Chorus]" and f[line+1]=="\n": 
        #    chorus_count+=1 #считаем припев 
             
lines=lines_count-heads_count #отнимаем от всего количества строк - количество заголовков 
print("Общее количество строк без заголовков и пустых строк: ", lines) 
#print(chorus_count)