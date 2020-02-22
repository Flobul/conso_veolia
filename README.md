# conso_veolia
Script python pour télécharger le fichier de consommation

## Installation

```bash
sudo apt-get install python3 xvfb iceweasel
sudo pip install selenium pyvirtualdisplay urllib3
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux32.tar.gz && tar xzfz geckodriver-v0.26.0-linux32.tar.gz && sudo mv geckodriver /usr/local/bin && rm geckodriver-v0.26.0-linux32.tar.gz
git clone -b master https://github.com/Flobul/conso_veolia.git
```

Remplissez votre identifiant et mot de passe dans le champ :

```#Informations de connexion
veolia_login = 'mon.adresse@email.com'
veolia_password = 'M-eau2P@ss'
```


## Résultat

```
$ python3 get_veolia_idf_consommation.py
2020-02-22 15:44:12,918 :: INFO :: Successfully started X with display ":1164".
2020-02-22 15:44:15,139 :: INFO :: Page de login
2020-02-22 15:44:27,472 :: INFO :: Page de consommation
2020-02-22 15:44:43,565 :: INFO :: Téléchargement du fichier
2020-02-22 15:44:44,775 :: INFO :: Fichier: /home/toto/Documents/historique_jours_litres.csv
```
