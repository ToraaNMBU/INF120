nmea_streng="$GPGGA,172814.0,3723.46587704,N,12202.26957864,W,2,6,1.2,18.893,M,-25.669,M,2.0,0031*4F"

nmea_list=nmea_streng.split(",")

gga_breddegrad=nmea_list[2]

print(gga_breddegrad)

#Dette er på formatet ddmm.mmmmm D:degree(grad) M: minutt
#En grad er 60 min 
#Høydegrad_desimalgrad =høydegrad_grad + høydegrad_desimalminutt/60

breddegrad_grader= gga_breddegrad[:2]
breddegrad_grader=(float(breddegrad_grader))

breddegrad_minutt=float(gga_breddegrad[2:])

breddegrad_desimalgrader=breddegrad_grader+breddegrad_minutt/60

print(breddegrad_desimalgrader)


# Gjør om til en funksjon!

def gga_breddegrad_til_grader(gga_breddegrad):
    breddegrad_grader= float(gga_breddegrad[:2])
    breddegrad_minutt=float(gga_breddegrad[2:])
    breddegrad_desimalgrader=breddegrad_grader+breddegrad_minutt/60
    return(breddegrad_desimalgrader)
print(gga_breddegrad_til_grader(gga_breddegrad))

# Nå skal vi se på Lengdegrader
def gga_lengdegrad_til_grader(gga_lengdegrad):
    lengdegrad_grader= float(gga_lengdegrad[:3])
    lengdegrad_minutt=float(gga_lengdegrad[3:])
    return(lengdegrad_grader+lengdegrad_minutt/60)


print(nmea_list)
gga_breddegrad=nmea_list[2]
gga_lengdegrad=nmea_list[4]
breddegrad=gga_breddegrad_til_grader(gga_breddegrad)
lengdegrad=gga_lengdegrad_til_grader(gga_lengdegrad)

print(breddegrad, lengdegrad)

# Nå skal vi se på data fra togturen til Yngve
# Bruker open til å åpne filen.
# Når vi skriver open.(filnavn) as f
# Blir variabelen f lik filen som nettopp ble åpnet
with open ("ås_ski.nmea.txt") as f:
        nmea_list= f.readlines()
        #Her leser vi linjene fra f og lagrer de i en liste 
        
        
print(nmea_

#for #nmea_list in nmea_list:
    #if nmea_list.startswith("$GNGGA"):#nmea linjer sater med "$GNGGA"
     #   nmea_list= nmea_list.split(",")
      #  gga_breddegrad=nmea_list[2]
       # gga_lengdegrad=nmea_list[4]
        #breddegrad=gga_breddegrad_til_grader(gga_breddegrad)
        #lengdegrad=gga_lengdegrad_til_grader(gga_lengdegrad)
        #print(breddegrad, lengdegrad)

# La oss lagre det til en fil, da må vi åpne filen i skrivemode ("w")

with open("Ås-ski bredde-lengde.txt", "w") as lengdebreddefil:
    for nmea_list in nmea_list:
        if nmea_list.startswith("$GNGGA"):#nmea linjer sater med "$GNGGA"
            nmea_list= nmea_list.split(",")
            gga_breddegrad=nmea_list[2]
            gga_lengdegrad=nmea_list[4]
            breddegrad=gga_breddegrad_til_grader(gga_breddegrad)
            lengdegrad=gga_lengdegrad_til_grader(gga_lengdegrad)
            
            lengdebreddefil.write(f"{breddegrad}, {lengdegrad}\n")
    