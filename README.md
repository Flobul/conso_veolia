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
