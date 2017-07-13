!#/bin/bash

jet decrypt jsonvars.env.encrypted jsonvars.env.encrypted
python editjson.py
jet encrypt jsonvars.env.encrypted jsonvars.env.encrypted
