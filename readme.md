
# Сервис, позволяющий узнать текущую загрузку ЦПУ, ОЗУ, ГПУ.
web-сервис позволяющий узнать текущую загрузку ЦПУ, ОЗУ, ГПУ(при наличии), а также сохраняющий время запроса(MM:DD:hh:mm:ss), метод запроса и отправляемые данные в Redis.

## Получение всех видов загрузки (ЦПУ, ОЗУ, ГПУ)
**Request: 
```jsonfrom django.db.models.fields import FieldDoesNotExist

GET api/v1/stats/current

```
**Response **
```
HTTP 200 OK

{
    "06:25:10:11:53": "GET; CPU:0.0, RAM:57.3, GPU:None"
}
```
## Получение определенных видов загрузки 
```jsonfrom django.db.models.fields import FieldDoesNotExist

POST api/v1/stats/current

Body:
{
    "usage_types":"CPU,RAM"
}

```
**Response **
```
HTTP 200 OK

{
    "06:25:10:11:53": "GET; CPU:0.0, RAM:57.3"
}
```
## Получения всех записей из Redis в формате JSON, где ключ - это время запроса, а значение – метод и отправленные данные.

```jsonfrom django.db.models.fields import FieldDoesNotExist

GET api/v1/stats/history

```
**Response **
```
HTTP 200 OK

{
    "06:25:09:58:30": "GET; CPU:0.0, RAM:57.2, GPU:None",
    "06:25:09:59:07": "GET; RAM:57.0, GPU:None",
    "06:25:09:58:23": "GET; CPU:0.0, RAM:57.1, GPU:None",
    "06:25:09:58:25": "GET; CPU:0.0, RAM:57.3, GPU:None",
    "06:25:09:59:48": "POST; CPU:2.0; RAM:56.7; ",
    "06:25:09:59:29": "GET; CPU:0.0, RAM:56.9, GPU:None",
    "06:25:09:58:29": "GET; RAM:57.1, GPU:None"
}
```
## Очистки записей в Redis

* Вместе с запросом может посылаться JSON с промежутком по времени (MM:DD:hh:mm:ss), в таком случае удаление производится в заданном диапазоне, иначе удаляются все записи.
```jsonfrom django.db.models.fields import FieldDoesNotExist

POST api/v1/stats/clear

Body:
{
    "range_from": "01:24:12:50:47",
    "range_to": "06:25:09:59:08"
}

```
**Response **
```
HTTP 204 OK

{
    "message": "11 keys successfully deleted"
}
```