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
Domain: devman.org responds OK: True and it has 66 paid days
Domain: www.rbc.ru responds OK: True and it has 39 paid days
Domain: vk.com responds OK: True and it has 365 paid days
Domain: ecfor.ru responds OK: True and it has 246 paid days
Domain: kremlin.ru responds OK: True and it has 404 paid days
Domain: ok.ru responds OK: True and it has 161 paid days
Domain: vkusvill.ru responds OK: True and it has 214 paid days
Domain: hh.ru responds OK: False and it has 282 paid days
Domain: www.superjob.ru responds OK: True and it has 251 paid days
Domain: www.python.org responds OK: True and it has 278 paid days
Domain: favorit-motors.ru responds OK: True and it has 270 paid days
Domain: ckbtm.org responds OK: True and it has 356 paid days

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
