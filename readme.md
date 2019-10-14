### Запуск тестов:
```(sh)
$ pytest --ds backend.settings
```

### Пример запроса:
```(sh)
$ curl 'http://172.24.0.4/api/products/' -X POST -H 'Cookie: sessionid=m250rxc4yl2kg2u1wi7m2g6hi5urfv4d' --data "name=test&weigth=1&width=2&height=3"
```

### Запуск nginx (+django):
```(sh)
$ sudo docker-compose up nginx
```

### Запуск django:
```(sh)
$ docker-compose run --rm web python3 manage.py runserver
```
