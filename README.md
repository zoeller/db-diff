# db-diff

Small Python script to differentiate two database structures.

Stack: MySQL, Python 3.7, Docker

```
$ cp .env.dist .env
$ docker-compose -f docker-compose.yml -f dev.yml up
$ python dbdiff.py -H 172.50.99.8 source target
```

Automatic loads sql scripts with sample databases.

Open Adminer in Browser to see created databases: http://172.50.99.9:8080/

Database names to compare: 'source' and 'target'

## Mode 1 - Compare two existing databases

Databases on the same host with same credentials:

```bash
$ python dbdiff.py -u root -H localhost database1 database2
$ python dbdiff.py -u root -p pass -H localhost database1 database2
```

Databases on different hosts and/or credentials:

Not implemented yet!

```bash
$ python dbdiff.py -u root -p pass -H host1 database1 host2:database2
$ python dbdiff.py -u root -p pass -H host1 database1 root:anotherpass@host2:database2
```

## Mode 2 - Compare two dump files

Not implemented yet!
