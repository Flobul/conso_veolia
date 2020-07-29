# conso_veolia
Based on Flobul/conso_veolia

Recupere la consomation d'eau sur le site Veolia IDF, puis injecte les données historiques dans jeedom.
L'insertion de données historiques n'est pas disponible dans l'api jsonrpc de jeedom, un appel a un script php est fait pour pouvoir effectuer l'insertion des données.

## Installation

```bash
git clone https://github.com/jbfuzier/conso_veolia.git
cd conso_veolia
apt-get install python3 xvfb iceweasel
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
64bit : wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz && tar xzfz geckodriver-v0.26.0-linux64.tar.gz && sudo mv geckodriver /usr/local/bin && rm geckodriver-v0.26.0-linux64.tar.gz
32bit : wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux32.tar.gz && tar xzfz geckodriver-v0.26.0-linux32.tar.gz && sudo mv geckodriver /usr/local/bin && rm geckodriver-v0.26.0-linux32.tar.gz
```

Adapter le fichier config.py

