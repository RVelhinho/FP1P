from math import sqrt

#1.1.1:
def gera_chave1(letras):
    return (letras[:5]),(letras[5:10]),(letras[10:15]),(letras[15:20]),(letras[20:25]) #Desta forma podese facilmente dividir o tuplo original em cinco subtuplos diferentes cada um com cinco elementos

#1.1.2(primeira parte):
def obtem_codigo1(car,chave): 
    for j in range(0,len(chave)):
        if car in chave[j]:
            for i in range(len(chave[j])):#j corresponde aos subtuplos da chave
                if chave[j][i]==car: #i corresponde as posicoes dentro dos subtuplos
                    soma=str(j)+str(i) #juntase a string de j ou linha e i ou coluna
                    return soma #resultado final
                
#1.1.2(segunda parte):
def codifica1(cad,chave):
    res=''
    for l in range(len(cad)): #para todas as posicoes da cadeia 
        res=res+obtem_codigo1(cad[l],chave) #adicionamse dois numeros correspondentes a um caratere de cada vez
    return res

#1.1.3(primeira parte):
def obtem_car1(cod,chave):
    cod_int=int(cod) # fazse a transformacao para inteiro para poder realizar as operacoes seguintes
    linha=cod_int//10
    coluna=cod_int%10
    for i in range(len(chave)): #vai procurar em todos os subtuplos
        for j in range(len(chave[i])): # vai procurar em todas as posicoes dos subtuplos
            if i==linha and j==coluna:
                res=chave[i][j]
                return res 
    
#1.1.3(segunda parte):
def descodifica1(cad_codificada,chave):
    codif=eval(cad_codificada) # passagem para inteiro
    res=''
    while codif>0: # ciclo que permite passagem por todos os numeros de 2 em 2
        string=codif%100
        res=obtem_car1(str(string),chave) + res
        codif=codif//100
    return res
        
#1.2.1:

def gera_chave2(letras):
    el=round(sqrt(len(letras))) #numero de elementos de cada subtuplo ou numero de colunas
    linhas=len(letras)//el #numero de linhas completas
    tuplo=()
    el_ul=len(letras)%el # numero de elementos da ultima linha
    for i in range(linhas):
        tuplo+=(letras[i*el:(i+1)*el],) # quando o numero de carateres e um quadrado perfeito
    if el_ul!=0: # quando o numero de carateres nao e um quadrado perfeito
        tuplo+=(letras[len(letras)-el_ul:],)
    return tuplo

#1.2.2(primeira parte):
def obtem_codigo2(car,chave):
    soma=''
    for el in range(len(chave)):
        if car in chave[el]:
            return obtem_codigo1(car,chave) #utiliza a funcao anteriormente definida
    return 'XX' # caso o carater nao pertenca a chave vai devolver XX
    
#1.2.2(segunda parte):
def codifica2(cad,chave):
    res=''
    for l in range(len(cad)): #para todos os carateres da funcao
        res=res+str(obtem_codigo2(cad[l],chave)) #utiliza a funcao definida anteriormente
    return res

#1.2.3(primeira parte):
def obtem_car2(cod,chave):
    if cod=='XX':
        return '?'
    else:
        return obtem_car1(cod,chave) # utiliza a funcao ja definida
                      
#1.2.3(segunda parte):
def descodifica2(cad_codificada,chave):
    res=''
    for el in range(0,len(cad_codificada),2):
        res+=obtem_car2(cad_codificada[el:el+2],chave) # passagem pelos carateres de 2 em 2
    return res
            