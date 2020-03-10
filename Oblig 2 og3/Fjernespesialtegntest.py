# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:48:40 2020

@author: Tor 
"""
#streng='Så!Fryktelig\fint,vær.'

#print(streng.translate({ord(i): None for i in ',."\:;()-?!'}))
#steng=streng.translate({ord(i): None for i in ',."\:;()-?!'})



def fjern_spesialtegn(streng):
    #[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
    
    streng=streng.translate({ord(i): None for i in ',."\:;()-?!'})
    return streng

f="jeg hater hei hater hater hater livet!!!!"
a="Hei på deg bitchass livet"
b="Per sier hei livet"
c="hei Per livet!"
d="hei livet geeshshsrg "
e="livet"
liste_med_dokumenter=[a,b,c,d,e,f]
liste_av_mengder=[]

def finn_unike_ord_i_streng(streng):
    streng=fjern_spesialtegn(streng)
    streng=streng.lower()
    streng=streng.strip()
    streng=streng.split()
    unike_ord=set(streng)
    liste_av_mengder.append(unike_ord)
    return unike_ord


#Denne delen må programeres inn i finn_felles_element_i_flere_mengder


def finn_felles_ellement_i_flere_mengder(liste_av_mengder):
    #Lager en tom liste
    felles_element=[]
    for i in range(len(liste_med_dokumenter))
        finn_felles_ellement_i_flere_mengder(liste_med_dokumenter(i))
    for set1 in range (len(liste_av_mengder)):
        #felles for 1 og n
        midlertidig=liste_av_mengder[0].intersection(liste_av_mengder[set1])
        liste_av_mengder[0]=midlertidig
    felles_liste=midlertidig
    return felles_liste 

finn_felles_ellement_i_flere_mengder()

"""
def søkeindeks_med_mengde(mengde_av_søkeord):
    ord_som_søkes_etter=mengde_av_søkeord.split()
    mulige_bøker={}
    finn_felles_ellement_i_flere_mengder(liste_av_mengder)
    
    finn_unike_ord_i_streng()
    #søker om ordet er i en liste
    for i in range len(liste_av_mengder):
        indeks=(i)
        for x in len(ord_som_søkes_etter)
            if ord_som_søkes_etter(x) in liste_mengder(i) == True:
                mulige_bøker_append(indeks)
        
            

    return mulige_bøker
indeks=finn_felles_ellement_i_flere_mengder(HAHA)


søkeord=("hei")

søkeindeks_med_mengde(søkeord)
"""