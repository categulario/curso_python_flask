# CRUD

* Create
* Read
* Update
* Delete

## HTTP 1.1

## verbos

* GET
* POST
* DELETE
* PATCH
* PUT
* HEAD
* OPTION

## Status codes

200, # ok
201, # creado
202, # accepted
204, # no content
400, # error del cliente
401, # unauthorized
403, # forbidden
404, # not found
500, # everything went to the chingada

## Ejemplos de peticiones

```
curl http://localhost:5000/api/dog
curl http://localhost:5000/api/dog/1
curl -X POST http://localhost:5000/api/dog
curl -X PUT http://localhost:5000/api/dog/1
curl -X DELETE http://localhost:5000/api/dog/1
```
