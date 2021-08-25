# PÄÄOHJELMA

# Modulien ja kirjastojen lataukset
import Hetutarkistus as ht 

# Kysytään käyttäjältä henkilötunnus
kysytty_hetu = input('Anna henkilötunnus')

# Tarkistetaan onko hetu oikein
oli_oikein = ht.tarkista_hetu(kysytty_hetu)

# Ilmoitetaan käyttäjälle oliko hetu oikein
if oli_oikein == True:
  print('henkilötunnus OK')
else:
  print('Henkilötunnus väärin,tarkista!')