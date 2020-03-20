# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:48:40 2020

@author: Tor Erik
"""

from ferdig_indeks import last_in_indeks  # Her laster vi inn en ferdig søkeindeks
import webbrowser


def fjern_spesialtegn(streng):
    liste_med_tegn=[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']
    for i in liste_med_tegn:
        streng=streng.replace(i, " ")
    return streng

def finn_unike_ord_i_streng(streng):
    streng=fjern_spesialtegn(streng)
    streng=streng.lower()
    streng=streng.strip()
    streng=streng.split()
    unike_ord=set(streng)
    return unike_ord

def finn_felles_ellement_i_flere_mengder(liste_av_mengder):
    #Lager en tom liste for felles elementer og en for liste_av_megnder
    felles_element=liste_av_mengder[0]
    for antall in liste_av_mengder:
        felles_element=felles_element.intersection(antall)
    return felles_element 
k=webbrowser.open('https://www.fhi.no/globalassets/dokumenterfiler/tema/koronavirussykdom/2871--cdc-alissa-eckert-ms_modifisert.png?preset=mainbodywidth')
h=("DU har fått koronavirus!")
def søk_i_indeks_med_mengde(indeks, mengde_av_søkeord):
    """Denne Funkjsonen har som formål å søke opp alle bøker som inneholder søkeordene"""
    mulige_bøker = []
    for ord_ in mengde_av_søkeord:
        if ord_ in indeks:
                mulige_bøker.append(indeks[ord_])
        else:
            return set()
        
    mulige_bøker = finn_felles_ellement_i_flere_mengder(mulige_bøker)
    return mulige_bøker

def klargjør_søkestreng(søkestreng):
    return finn_unike_ord_i_streng(søkestreng)

def søk__indeks_med_streng(indeks, søkestreng):
    for_søk =klargjør_søkestreng(søkestreng)
    mulige_bøker = søk_i_indeks_med_mengde(indeks, for_søk)
    return mulige_bøker

if __name__ == "__main__":
    søkestreng = "Sherlock Holmes scarlet"
    indeks = last_in_indeks()  # Jeg (Yngve) har allerede lagd en indeks dere kan sø¸ke i
                               # Den henter vi ut her.
    k
    
    print(søk__indeks_med_streng(indeks, søkestreng))
    print(h)
    
    