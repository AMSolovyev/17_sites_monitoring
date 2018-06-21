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
Domain: devman.org is True and it has 67 paid days
Domain: www.rbc.ru is True and it has 40 paid days
Domain: vk.com is True and it has 366 paid days
Domain: ecfor.ru is True and it has 247 paid days
Domain: kremlin.ru is True and it has 405 paid days
Domain: ok.ru is True and it has 162 paid days
Domain: vkusvill.ru is True and it has 215 paid days
Domain: hh.ru is False and it has 283 paid days
Domain: www.superjob.ru is True and it has 252 paid days
Domain: www.python.org is True and it has 279 paid days
Domain: favorit-motors.ru is True and it has 271 paid days

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
