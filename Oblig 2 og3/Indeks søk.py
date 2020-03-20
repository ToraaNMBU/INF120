# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:34:22 2020

@author: Tor Erik
"""

# -*-coding: utf-8 -*-

from ferdig_indeks import last_in_indeks  # Her laster vi inn en ferdig sÃ¸keindeks

liste_av_mengder=[]

def fjern_spesialtegn(streng):
    """Denne koden yeeter spesialtegn"""
    #[',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']``
    
    steng=streng.translate({ord(i): None for i in ',."\:;()-?!'})
    return streng


def finn_unike_ord_i_streng(streng):
    
    streng=fjern_spesialtegn(streng)
    streng=streng.lower()
    streng=streng.strip()
    streng=streng.split()
    unike_ord=set(streng)
    liste_av_mengder.append(unike_ord)
    return unike_ord

    

def finn_felles_ellement_i_flere_mengder(liste_av_mengder):
    """
    Lag en funksjon som finner felles element i en samling av mengder (set).
    
    Arguments
    ---------
    liste_av_mengder : List[Set]
        En liste hvor hvert element er en mengde (set pÃ¥ engelsk).
    
    Returns
    -------
    snitt_av_mengder : Set[str]
        En mengde som kun inneholder de elementene som er del av ALLE
        mengdene i ``liste_av_mengder``.
    
    Notes
    -----
    Vi kan finne snittet mellom to mengder med ``intersection`` funksjonen.

    >>> mengde1 = {1, 2, 3}
    >>> mengde2 = {2, 3, 4}
    >>> mengde1.intersection(mengde2)
    {2, 3}
    
    Om vi tar snittet mellom en mengde og seg selv sÃ¥ endres ingen ting.

    >>> mengde1 = {1, 2, 3}
    >>> mengde1 = mengde1.intersection(mengde1)
    >>> print(mengde1)
    {1, 2, 3}

    Examples
    -------
    >>> mengde1 = {1, 2, 3}
    >>> mengde2 = {2, 3, 4}
    >>> liste_av_mengder = [mengde1, mengde2]
    >>> finn_felles_element_i_flere_mengder(liste_av_mengder)
    {2, 3}
    >>> mengde3 = {3, 4, 5}
    >>> liste_av_mengder = [mengde1, mengde2, mengde3]
    >>> finn_felles_element_i_flere_mengder(liste_av_mengder)
    {3}
    """
    
    #Lager en tom liste
    felles_element=[]
    for set1 in range (len(liste_av_mengder)):
        #felles for 1 og n
        midlertidig=liste_av_mengder[0].intersection(liste_av_mengder[set1])
        liste_av_mengder[0]=midlertidig
    felles_liste=midlertidig
    return felles_liste 

    
    


def søkeindeks_med_mengde(indeks, mengde_av_søkeord):
    """
    Finn alle dokument som inneholder alle søkeordene i ``mengde_søkeord``.

    Denne funksjonen skal ta to argument som input, en søkeindeks og 
    en mengde med søkeord.

    Søkeindeksen er en dictionary med engelske ord som nøkler og mengden med alle
    dokument som inneholder det ordet som verdi.

    Mengden med søkeord er en mengde (set på Engelsk) som beskriver hva
    som søkes etter.

    Det som returneres er mengden med dokument som inneholder ALLE søkeordene.

    Arguments
    ---------
    indeks : dict[str] -> Set[str]
        SÃ¸keindeksen.
    mengde_av_sÃ¸keord : Set[str]
        Mengden med sÃ¸keord.

    Returns
    -------
    relevante_bøker : Set[str]
        Mengden med bøker som inneholder alle ordene i ``mengde_av_sÃ¸keord``.

    Notes
    -----
    Husk ``finn_felles_ellement_i_flere_mengder`` funksjonen din.

    Vi kan teste om et element er en nøkkel i en dictionary med ``in`` nøkkelordet

    >>> d = {'a': 1, 'b': 2}
    >>> 'a' in d
    True
    >>> 1 in d
    False

    Vi kan lage en tom mengde med ``set`` funksjonen.

    >>> tom_mengde = set()
    >>> print(tom_mengde)
    {}

    Examples
    --------
    >>> indeks = last_inn_indeks()
    >>> søkeindeks_med_streng(indeks, {"sherlock", "holmes", "scarlet")
    {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}
    >>> søkeindeks_med_streng(indeks, {"Dette", "er", "ikke", "i", "indeksen"})
    {}
    """
    mulige_bøker={}
    
    finn_felles_ellement_i_flere_mengder(liste_av_mengder):
    

    return mulige_bÃ¸ker


def klargjÃ¸r_sÃ¸kestreng(sÃ¸kestreng):
    r"""
    Ta inn en sÃ¸kestreng og klargjÃ¸r den for Ã¥ sÃ¸ke i en sÃ¸keindeks.

    Strengen skal behandles pÃ¥ samme mÃ¥te som vi behandler nye strenger
    som skal indekseres. Store bokstaver skal gjÃ¸res om til smÃ¥,
    spesialtegn skal fjernes og "whitespace" tegn pÃ¥ starten og slutten
    av strengen skal fjernes. Til slutt skal strengen splittes ved 
    alle mellomrom og duplikatord skal fjernes.

    Arguments
    ---------
    sÃ¸kestreng : str
        Strengen vi vil finne unike tegn i.
    
    Returns
    -------
    ord_i_streng : Set[str]
        Mengden med unike ord i strengen.
    
    Notes
    -----
    Kan du gjenbruke en funksjon du lagde tidligere i obligen?

    Examples
    --------
    >>> streng = "abc1, hei pÃ¥ deg. Hva heter du?"
    >>> klargjÃ¸r_sÃ¸kestreng(streng)
    "abc1 hei pÃ¥ deg Hva heter du"

    >>> streng = "  Hei pÃ¥ deg!!!\n"
    >>> klargjÃ¸r_sÃ¸kestreng(streng)
    "Hei pÃ¥ deg"
    """
    klargjort_streng = None  # Slett denne linja
    # Skriv kode her

    return klargjort_streng


def sÃ¸k_i_indeks_med_streng(indeks, sÃ¸kestreng):
    """
    Finn alle dokument som inneholder alle sÃ¸keordene i ``sÃ¸kestreng``.

    Denne funksjonen skal ta to argument som input, en sÃ¸keindeks og 
    en mengde med sÃ¸keord.

    SÃ¸keindeksen er en dictionary med engelske ord som nÃ¸kler og mengden med alle
    dokument som inneholder det ordet som verdi.

    SÃ¸kestrengen skal fÃ¸rst klargjÃ¸res. Dette gjÃ¸res ved Ã¥ gjÃ¸re strengen til
    smÃ¥ bokstaver og Ã¥ fjerne spesialtegn. I tillegg skal og whitespace pÃ¥ 
    starten og slutten av strengen fjernes. Deretter skal hvert ord i 
    sÃ¸kestrengen hentes ut. Disse ordene brukes nÃ¥r det skal sÃ¸kes i
    de indekserte dokumentene.

    Det som returneres er mengden med dokument som inneholder ALLE sÃ¸keordene.

    Arguments
    ---------
    indeks : dict
        SÃ¸keindeksen.
    mengde_av_sÃ¸keord : str
        Mengden med sÃ¸keord.

    Returns
    -------
    relevante_bÃ¸ker : Set[str]
        Mengden med bÃ¸ker som inneholder alle ordene i ``mengde_av_sÃ¸keord``.

    Notes
    -----
    Husk ``sÃ¸k_i_indeks_med_mengde`` og ``klargjÃ¸r_sÃ¸kestreng`` funksjonene
    dine.

    Examples
    --------
    >>> indeks = last_inn_indeks()
    >>> sÃ¸k_i_indeks_med_streng(indeks, "Sherlock Holmes, scarlet")
    {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}
    >>> sÃ¸k_i_indeks_med_streng(indeks, "Dette er ikke i indeksen")
    {}
    """
    mulige_bÃ¸ker = None  # Slett denne linja
    # Skriv kode her

    return mulige_bÃ¸ker


if __name__ == "__main__":
    sÃ¸kestreng = "Sherlock Holmes, scarlet"
    indeks = last_in_indeks()  # Jeg (Yngve) har allerede lagd en indeks dere kan sÃ¸ke i
                               # Den henter vi ut her.

    print(sÃ¸k_i_indeks_med_streng(indeks, sÃ¸kestreng))
    # Denne skal printe
    #  {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}