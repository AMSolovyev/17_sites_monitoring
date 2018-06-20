# Sites Monitoring Utility

The script ```check_sites_health.py``` checks urls in the file and shows a site condition.
If the site has a response 200 it is OK. The script ```check_sites_health.py```
also checks paid days.

# How to use
```
1. virtualenv -p python3 env
2. source env/bin/activate
3. pip install -r requirements.txt
4. python check_sites_health.py -f -f sites.txt
```

You can output data like this:
```
OK: domain: devman.org has 68 paid days
OK: domain: www.rbc.ru has 40 paid days
OK: domain: vk.com has 367 paid days
OK: domain: ecfor.ru has 247 paid days
OK: domain: kremlin.ru has 405 paid days
OK: domain: ok.ru has 162 paid days
OK: domain: vkusvill.ru has 216 paid days
OK: domain: hh.ru has 283 paid days
OK: domain: www.superjob.ru has 252 paid days
OK: domain: www.python.org has 280 paid days
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
