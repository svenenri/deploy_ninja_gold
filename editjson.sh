curl -SLO "https://s3.amazonaws.com/codeship-jet-releases/1.18.0/jet-linux_amd64_1.18.0.tar.gz"
sudo tar -xaC /usr/local/bin -f jet-linux_amd64_1.18.0.tar.gz
sudo chmod +x /usr/local/bin/jet
jet decrypt jsonvars.env.encrypted jsonvars.env.encrypted
python editjson.py
jet encrypt jsonvars.env.encrypted jsonvars.env.encrypted
