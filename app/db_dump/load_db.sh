#!/bin/bash

cd /docker-entrypoint-initdb.d/dump && mysql -uroot < employees.sql