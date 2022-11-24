#!/bin/bash

sudo apt update

sudo apt -y upgrade

sudo apt install python3 -y

sudo apt install python3-pip -y

pip3 install pycall

sudo add-apt-repository universe

sudo apt -y install git curl wget libnewt-dev libssl-dev libncurses5-dev subversion libsqlite3-dev build-essential libjansson-dev libxml2-dev  uuid-dev -y

wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-18-current.tar.gz

tar xvf asterisk-18-current.tar.gz

cd asterisk-18*/

contrib/scripts/get_mp3_source.sh

sudo contrib/scripts/install_prereq install

./configure

make

sudo make install

sudo make progdocs

sudo make samples

sudo make config

sudo ldconfig

sudo groupadd asterisk

sudo useradd -r -d /var/lib/asterisk -g asterisk asterisk

sudo usermod -aG audio,dialout asterisk

sudo chown -R asterisk.asterisk /etc/asterisk

sudo chown -R asterisk.asterisk /var/{lib,log,spool}/asterisk

sudo chown -R asterisk.asterisk /usr/lib/asterisk

sudo chmod -R 750 /var/{lib,log,run,spool}/asterisk /usr/lib/asterisk /etc/asterisk

echo 'AST_USER="asterisk"' >> /etc/default/asterisk
echo 'AST_GROUP="asterisk"' >> /etc/default/asterisk

echo 'runuser = asterisk' >> /etc/asterisk/asterisk.conf
echo 'rungroup = asterisk ' >> /etc/asterisk/asterisk.conf

echo 'enable=yes' >> /etc/asterisk/cdr.conf
echo 'safeshutdown=yes ' >> /etc/asterisk/cdr.conf


sudo systemctl restart asterisk

sudo systemctl enable asterisk

cp install/sip.conf /etc/asterisk/

cp install/extensions.conf /etc/asterisk/

clear

service asterisk restart 
asterisk -rx 'reload'
asterisk -rx 'dialplan reload'

echo "COMPLETED SUCCESS"