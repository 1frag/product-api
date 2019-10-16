### Запуск тестов:
```(sh)
$ pytest --ds backend.settings
```

### Запуск nginx (+django):
```(sh)
$ sudo docker-compose up nginx
```

### Запуск django:
```(sh)
$ docker-compose run --rm web python3 manage.py runserver
```

### Пример запроса:
```(sh)
curl 'http://172.31.0.2/api/products/' -X POST -H 'AUTHORIZATION: basic cm9vdDpyb290' -H "Content-Type: application/json" -H 'Accept: text/plain' --data '{"name":"test77", "weigth": 12, "width": 32, "height": 32}' --compressed --insecure
```
