# db-diff

Tiny software project to differentiate multiple database structures.

Stack: MySQL, Python 3.7, Docker

```
$ cp .env.dist .env
$ docker-compose -f docker-compose.yml -f dev.yml up
$ python dbdiff.py -H 172.50.99.8 source target
```

Automatic loads sql scripts with sample databases.

Database names to compare: 'source' and 'target'

## Mode 1 - Compare two existing databases

```bash
$ python dbdiff.py -u root -H localhost database1 database2
$ python dbdiff.py -u root -p pass -H localhost database1 database2
```

Databases with different credentials and/or hosts

Not implemented yet!

```bash
$ python dbdiff.py -u root -p pass -H host1 database1 host2:database2
$ python dbdiff.py -u root -p pass -H host1 database1 root:anotherpass@host2:database2
```

## Mode 2 - Compare two dump files

Not implemented yet!
