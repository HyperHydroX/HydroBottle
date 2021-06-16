# Getting things ready for Project One 🎉 🎊

- [Getting things ready for Project One 🎉 🎊](#getting-things-ready-for-project-one--)
  - [Installatie](#installatie)
    - [Downloaden van de image ⏳](#downloaden-van-de-image-)
    - [Terugzetten van de image ⏳](#terugzetten-van-de-image-)
    - [RasPi koppelen](#raspi-koppelen)
    - [Raspi klaarmaken voor verder gebruik](#raspi-klaarmaken-voor-verder-gebruik)
  - [Configuratie](#configuratie)
    - [⚠️ ZELF doen: **Wifitoegang** voorzien op de RasPi voor thuis:](#️-zelf-doen-wifitoegang-voorzien-op-de-raspi-voor-thuis)
    - [Reeds gedaan: **Full update**/upgrade op 26 april, wil je upgraden, volg dan onderstaande lijstje:](#reeds-gedaan-full-updateupgrade-op-26-april-wil-je-upgraden-volg-dan-onderstaande-lijstje)
    - [Reeds gedaan: **Apache** installeren](#reeds-gedaan-apache-installeren)
    - [Reeds gedaan: **MariaDB**](#reeds-gedaan-mariadb)
      - [Reeds gedaan: **MariaDB** Installeren](#reeds-gedaan-mariadb-installeren)
      - [Reeds gedaan: **MariaDB** Beveiligen](#reeds-gedaan-mariadb-beveiligen)
      - [Reeds gedaan: **MariaDB Gebruiker** aanmaken](#reeds-gedaan-mariadb-gebruiker-aanmaken)
    - [⚠️ ZELF doen: **MySQLWorkbench** configureren](#️-zelf-doen-mysqlworkbench-configureren)
    - [⚠️ ZELF doen: **Visual Studio** Configureren:](#️-zelf-doen-visual-studio-configureren)
    - [⚠️ ZELF doen: **GitHub** repo clonen:](#️-zelf-doen-github-repo-clonen)
    - [Reeds gedaan: **Python** klaarzetten:](#reeds-gedaan-python-klaarzetten)
    - [Reeds gedaan: **Database** importeren:](#reeds-gedaan-database-importeren)
    - [⚠️ ZELF te doen: app.py runnen:](#️-zelf-te-doen-apppy-runnen)
    - [⚠️ ZELF te doen: Frontend weergeven in Apache.](#️-zelf-te-doen-frontend-weergeven-in-apache)
    - [⚠️ ZELF doen: Als je project af is, automatisch opstarten.](#️-zelf-doen-als-je-project-af-is-automatisch-opstarten)
    - [Veel succes!](#veel-succes)

## Installatie

> Tijdens deze installatie zal je de image voor ProjectOne downloaden, installeren en configureren.
> Hierna zal je een preinstalled project configureren, zodat je op het einde een volledig werkende frontend en backend hebt.

### Downloaden van de image ⏳

- Download _[RasPiProjectOne.zip](https://studenthowest-my.sharepoint.com/personal/dieter_roobrouck_howest_be/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fdieter%5Froobrouck%5Fhowest%5Fbe%2FDocuments%2FOneDrive%20%2D%20Hogeschool%20West%2DVlaanderen%2FProjectOne&originalPath=aHR0cHM6Ly9zdHVkZW50aG93ZXN0LW15LnNoYXJlcG9pbnQuY29tLzpmOi9nL3BlcnNvbmFsL2RpZXRlcl9yb29icm91Y2tfaG93ZXN0X2JlL0VrOUxsQVR5d0xKUGt2YmNhS2tLX3BRQmxvb2lQQ1JIdGFXRjgtUU96S05xa2c%5FcnRpbWU9VFRxb2Zsc2IyVWc)_ naar je lokale computer.

### Terugzetten van de image ⏳

- ⚠ Unzip het bestand ⚠
- Plaats het bestand op een SD-kaartje van minstens 8GB met Win32 Imager of Balena Etcher.
- Nadat de image geschreven is, kan je het SD-kaartje verwijderen en in je RasPi steken.

### RasPi koppelen

- Boot je RasPi.
- Koppel de RasPi aan je computer dmv een netwerkkabel en maak een SSH-connectie in _Putty_ naar 192.168.168.168 voor de user \_student\* met als paswoord \_W8w00rd\*.

> PAS OP: De image is in AZERTY gemaakt (in tegenstelling tot die van Sensors & Interfacing!)  
> Mocht het inloggen niet lukken, probeer dan in qwerty _Z!zààrd_.

### Raspi klaarmaken voor verder gebruik
- Na het inloggen tik je sudo rapsi-config.
- In het menu kies je voor (6) Advanced > (1) Expand Filesystem
- ⚠ REBOOT de Raspi

- Aangezien je in de lessen Sensors en Interfacing reeds een SSH-conncetie gemaakt hebt, moet je een aantal zaken in Windows aanpassen:
    - Ga in de map c:\\Users\\<gebruikernaam\>\\.ssh op zoek naar het bestand *known_hosts*. Zoek in dat bestand naar de lijn waar het adres 192.168.168.168 staat en sla daarna het bestand opnieuw op.
    - Zoek in dezelfde map het bestand *config* en zoek naar het blokje waar 192.168.168.168 bijstaat en wis dit. Sla het bestand op en ga verder.
---

## Configuratie

### ⚠️ ZELF doen: **Wifitoegang** voorzien op de RasPi voor thuis:

- `sudo -i` om administratorrechten te krijgen
- `wpa_passphrase <your_SSID@Home> <your_wifi-password> >> /etc/wpa_supplicant/wpa_supplicant.conf`  
  Vervang hier \<your_SSID@Home\> door de naam van je thuisnetwerk en \<your_wifi-pasword\> door het bijhorende paswoord.
- `wpa_cli -i wlan0 reconfigure` om je draadloze netwerkkaart in de RasPi te herladen.
- `wget www.google.com` om te zien of het draadloos internet werkt.

### Reeds gedaan: **Full update**/upgrade op 26 april, wil je upgraden, volg dan onderstaande lijstje:

- `apt update` om na te gaan welke updates beschikbaar zijn.  
  (je hebt nog sudo rechten uit de vorige stap, dus hoeft geen `sudo` te zetten)
- `apt upgrade` om de beschikbare updates te installeren.
- `Y` indien je de vraag krijgt of je zeker bent.
- Wachten, wachten, wachten, ...

### Reeds gedaan: **Apache** installeren

- `apt install apache2 -y` om Apache, de webserver, te installeren. Dit pakket neemt voor Full Stack Web Developlent / ProjectOne de opdracht over van de _Live Server_ in Visual Studio Code.
- Aangezien we in deze oefening met Github werken zullen we het ons gemakkelijk maken door alle materiaal in één map je zetten, zowel frontend als backend, zoals we gewoon zijn in de lessen Full Stack Web Development.
  Hiervoor zullen we de standaardmap van Apache moeten aanpassen, samen met de map- en bestandsrechten, maar dit zullen we pas doen als we onze mappenstructuur aangemaakt hebben.

### Reeds gedaan: **MariaDB**

#### Reeds gedaan: **MariaDB** Installeren

- `apt install mariadb-server mariadb-client -y` om MariaDB, de fork van MySQL te installeren

#### Reeds gedaan: **MariaDB** Beveiligen

- `mysql_secure_installation` om de MariaDB beter te beveiligen
- Eerst wordt er gevraagd om het huidige root paswoord in te geven voor MariaDB. Aangezien er nog geen is kan je hier gewoon op _Enter_ drukken.
- Vervolgens kan je het paswoord wijzigen. Kies een paswoord dat je **zeker** kan onthouden! Standaard werd hier gekozen voor het wachtwoord _W8w00rd_
- Een volgende stap is anonieme gebruikers verwijderen. Kies hier voor `y`
- Verbied root om remote in te loggen. Kies hier voor `y`.
- Vervolgens remove test database and access? Kies `y`.
- Tenslotte reload privilege databases: `y`

#### Reeds gedaan: **MariaDB Gebruiker** aanmaken

- Hierna configureren we de user _student_ met wachtwoord _W8w00rd_ op de MariaDB-server
- `mysql -u root -p` om toegang te krijgen tot de MariaDB-server
- `grant all on *.* to 'student'@'localhost' identified by 'W8w00rd'; grant grant option on *.* to 'student'@'localhost';` Maakt een nieuwe user _student_ met wachtwoord _W8w00rd_ aan die rechten krijgt op alle databases.
- `flush privileges` Herlaadt de rechten
- `exit` Verlaat de MariaDB-server

---

### ⚠️ ZELF doen: **MySQLWorkbench** configureren

- Start MySQLWorkBench op je laptop
- Maak een nieuwe connectie.
  - Kies bij Connection Method voor Standard TCP/IP over SSH
  - SSH Hostname: `192.168.168.168`
  - SSH Username: `student`
  - SSH Password: `W8w00rd`  
    Sla dit indien mogelijk op.
  - MySQL Hostname: `127.0.0.1`
  - MySQL Server Port: `3306`
  - Username: `student`
  - Password: `W8w00rd` Sla dit indien mogelijk op.

### ⚠️ ZELF doen: **Visual Studio** Configureren:

- Open Visual Studio
- Installeer de extensie _Remote-SSH_
- Druk F1 en tik SSH.  
  Kies voor de optie _Remote-SSH: Add New SSH Host_
- Tik `ssh student@192.168.168.168 -A`
- Kies een mogelijkheid om het bestand op te slaan.
- Druk F1 en tik SSH.  
  Kies voor de optie _Remote-SSH: Connect To Host_
- Kies de optie _192.168.168.168_
- Er zal een nieuw window openen en het paswoord voor de RasPi zal gevraagd worden.
- Tik `W8w00rd`
- Hierna zal Visual Studio Codede connectie openen en een aantal zaken installeren op de RasPi.
  > Wees geduldig. De eerste keer duurt dit wat langer.

### ⚠️ ZELF doen: **GitHub** repo clonen:

- Druk op het logo van de _Source Control_ aan de linkerkant en kies voor Clone Repository.
- Ga in een browser naar de GitHub Classroom [https://classroom.github.com/a/0er4bOXy] en accepteer de invitation. Refresh de pagina en ga naar de aangemaakte repo. Klik op de knop _Code_ en kopieer de git-link.
- Plak de gekopieerde link in Visual Studio Code en druk op enter.
- Plaats de repo in de map `/home/student/`
- Visual Studio Code zal daarna vragen om deze repo te openen, klik _Yes_
- Open daarna het bestand Code/Backend/app.py en geef Visual Studio Code even de tijd om alle nodige zaken in te laden.

### Reeds gedaan: **Python** klaarzetten:

- Voor we de app.py kunnen runnen moeten we een aantal packages installeren voor python.
- We gebruiken hier op de RasPi GEEN venv. Open een Terminal en tik volgende code:
  - `pip3 install flask-cors`
  - `pip3 install flask-socketio`
  - `pip3 install mysql-connector-python`
  - `pip3 install gevent`
  - `pip3 install gevent-websocket`

### Reeds gedaan: **Database** importeren:

- Importeer de database in MariaDB via MySQLWorkbench.

---

### ⚠️ ZELF te doen: app.py runnen:

- Probeer _app.py_ te runnen. Indien je in het venster niet op Play (het groene driehoekje) kan drukken, kijk dan in de extensies bij de Python extensie en klik op _install on 192.168.168.168_ en wacht. Reload indien dit gevraagd wordt.
- Als alles goed gegaan is zou de backend nu moeten runnen.

### ⚠️ ZELF te doen: Frontend weergeven in Apache.

- Surf op je pc naar http://192.168.168.168.
- Normaalgezien zie je nu de _Apache2 Debian Default Page_, dit is de standaardpagina van Apache die momenteel in de map _/var/www/html/_ staat op de RasPi. Wij zullen deze standaardmap niet gebruiken, maar zullen wel gebruik maken vande Frontend map uit de repo die je zonet gecloned hebt.
- Indien je geen sudo meer bent:
  `sudo -i`
- `nano /etc/apache2/sites-available/000-default.conf`
- Gebruik pijltje naar beneden om naar regel te gaan waar nu staat _DocumentRoot /var/www/html_ of `DocumentRoot /home/student/<naam_van_je_repo>/Code/Frontend` en wijzig dit in `DocumentRoot /home/student/<naam_van_je_repo>/Code/Frontend`
- Opslaan doe je door _Ctrl + x_ te doen, gevolgd door `Y` en _Enter_
- Daarna herstarten we Apache door `service apache2 restart ` te doen
- Nu moeten we nog de rechten op de root folder juist zetten.

  - open `nano /etc/apache2/apache2.conf` en gebruik het pijltje naar beneden om op zoek te gaan naar volgende regels:  
    _\<Directory />\
     Options FollowSymLinks\
     AllowOverride All\
     Require all denied\
     \</Directory>_

    en die te wijzigen naar:

    _\<Directory />\
     Options Indexes FollowSymLinks Includes ExecCGI\
     AllowOverride All\
     Require all granted\
     \</Directory>_\

  - Opslaan doe je door _Ctrl + x_ te doen, gevolgd door `Y` en _Enter_
  - Daarna herstarten we Apache door `service apache2 restart ` te doen

### ⚠️ ZELF doen: Als je project af is, automatisch opstarten.

- Maak een bestand aan met de naam _mijnproject.service_
- Plaats volgende code in het bestand:  
  `[Unit]`  
  `Description=ProjectOne Project`  
  `After=network.target`  
  `[Service]`  
  `ExecStart=/usr/bin/python3 -u /home/student/<naam_van_je_repo>/Code/Backend/app.py`  
  `WorkingDirectory=/home/student/<naam_van_je_repo>/Code/Backend/app.py`  
  `StandardOutput=inherit`  
  `StandardError=inherit`  
  `Restart=always`  
  `User=student`  
  `[Install]`  
  `WantedBy=multi-user.target`
- Kopieer dit bestand als root user naar _/etc/systemd/system_ met het commando `sudo cp mijnproject.service /etc/systemd/system/mijnproject.service`
- Nu kan je het bestand testen door het op te starten:
  `sudo systemctl start mijnproject.service`
- Het bestand stoppen kan met door het commando:
  `sudo systemctl stop mijnproject.service` in te geven
- Indien alles goed werkt kan je het script automatisch laten opstarten na het booten:
  `sudo systemctl enable mijnproject.service`

### Veel succes!

> Vergeet niet als alles werkt een selfie te nemen en deze in te dienen bij de juiste opdracht!
