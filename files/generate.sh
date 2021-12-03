#!/bin/bash

touch empty_file

for FILESIZE in 1M 100M 250M 500M 
do
	head -c $FILESIZE </dev/urandom > file_$FILESIZE
done
