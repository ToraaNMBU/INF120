# -*- coding: utf-8 -*-

from ferdig_indeks import last_in_indeks  # Her laster vi inn en ferdig søkeindeks


def fjern_spesialtegn(streng):
   
    streng = streng.lower()
    erstatningsliste = [',', '.', '"', '\'', ':', ';', '(', ')', '-', '?', '!']
    for tegn in erstatningsliste:
        streng = streng.replace(tegn, " ")
    
    return streng

 
def finn_unike_ord_i_streng(streng):
   
    streng = fjern_spesialtegn(streng)
    streng = streng.strip()
    ord_liste = streng.split (" ")
    unike_ord = set(ord_liste)
       
    return unike_ord


def finn_felles_ellement_i_flere_mengder(liste_av_mengder):   
    """
    Lag en funksjon som finner felles element i en samling av mengder (set).
    
    Arguments
    ---------
    liste_av_mengder : List[Set]
        En liste hvor hvert element er en mengde (set på engelsk).
    
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
    
    Om vi tar snittet mellom en mengde og seg selv så endres ingen ting.

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
   
    felles_element = liste_av_mengder[0]
    for linje in liste_av_mengder:
        felles_element = felles_element.intersection(linje)
        
    return felles_element


def søk_i_indeks_med_mengde(indeks, mengde_av_søkeord): 
    """
    Finn alle dokumentene som inneholder alle søkeordene i ``mengde_av_søkeord``.

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
        Søkeindeksen.
    mengde_av_søkeord : Set[str]
        Mengden med søkeord.

    Returns
    -------
    relevante_bøker : Set[str]
        Mengden med bøker som inneholder alle ordene i ``mengde_av_søkeord``.

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
    >>> søk_i_indeks_med_streng(indeks, {"sherlock", "holmes", "scarlet")
    {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}
    >>> søk_i_indeks_med_streng(indeks, {"Dette", "er", "ikke", "i", "indeksen"})
    {}
    """
    #Om 'holmes' er i indeksen, ta den ut i en nøstet liste der jeg får ut alle bøkene med ordet " holmes"
    #Deretter sett inn forrige funksj
    
    #Lag en for-løkke som går gjennom hvert ord i mengde_av_søkeord
    
    #Dersom ordet er i den integrerte listen, legg til i tom liste med tilhørende bok
    mulige_bøker = []
    for ord_ in mengde_av_søkeord:
        if ord_ in indeks:
            mulige_bøker.append(indeks[ord_])
        else:
            return set() #Da har det ikke noe for seg å søke videre dersom et av ordene 
                         # ikke finnes i listen. 
                
    mulige_bøker = finn_felles_ellement_i_flere_mengder(mulige_bøker)
     
    return mulige_bøker

def klargjør_søkestreng(søkestreng):
    """
    Ta inn en søkestreng og klargjør den for å søke i en søkeindeks.

    Strengen skal behandles på samme måte som vi behandler nye strenger
    som skal indekseres. Store bokstaver skal gjøres om til små,
    spesialtegn skal fjernes og "whitespace" tegn på starten og slutten
    av strengen skal fjernes. Til slutt skal strengen splittes ved 
    alle mellomrom og duplikatord skal fjernes.

    Arguments
    ---------
    søkestreng : str
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
    >>> streng = "abc1, hei på deg. Hva heter du?"
    >>> klargjør_søkestreng(streng)
    "abc1 hei på deg Hva heter du"

    >>> streng = "  Hei på deg!!!\n"
    >>> klargjør_søkestreng(streng)
    "Hei på deg"
    """
         
    return finn_unike_ord_i_streng(søkestreng)


def søk_i_indeks_med_streng(indeks, søkestreng):
    """
    Finn alle dokument som inneholder alle søkeordene i ``søkestreng``.

    Denne funksjonen skal ta to argument som input, en søkeindeks og 
    en mengde med søkeord.

    Søkeindeksen er en dictionary med engelske ord som nøkler og mengden med alle
    dokument som inneholder det ordet som verdi.

    Søkestrengen skal først klargjøres. Dette gjøres ved å gjøre strengen til
    små bokstaver og å fjerne spesialtegn. I tillegg skal og whitespace på 
    starten og slutten av strengen fjernes. Deretter skal hvert ord i 
    søkestrengen hentes ut. Disse ordene brukes når det skal søkes i
    de indekserte dokumentene.

    Det som returneres er mengden med dokument som inneholder ALLE søkeordene.

    Arguments
    ---------
    indeks : dict
        Søkeindeksen.
    mengde_av_søkeord : str
        Mengden med søkeord.

    Returns
    -------
    relevante_bøker : Set[str]
        Mengden med bøker som inneholder alle ordene i ``mengde_av_søkeord``.

    Notes
    -----
    Husk ``søk_i_indeks_med_mengde`` og ``klargjør_søkestreng`` funksjonene
    dine.

    Examples
    --------
    >>> indeks = last_inn_indeks()
    >>> søk_i_indeks_med_streng(indeks, "Sherlock Holmes, scarlet")
    {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}
    >>> søk_i_indeks_med_streng(indeks, "Dette er ikke i indeksen")
    {}
    """

    #Klargjort_streng og søk_i_indeks_med_mengde
    for_søk = klargjør_søkestreng(søkestreng) 
    mulige_bøker = søk_i_indeks_med_mengde(indeks, for_søk)
    
    return mulige_bøker


if __name__ == "__main__":
    søkestreng = "Sherlock Holmes, scarlet"
    indeks = last_in_indeks()  # Jeg (Yngve) har allerede lagd en indeks dere kan søke i
                               # Den henter vi ut her.

    print(søk_i_indeks_med_streng(indeks, søkestreng))
    # Denne skal printe
    #  {'Chronicles_of_Martin_Hewitt.bok', 'The_Hound_of_the_Baskervilles.bok'}