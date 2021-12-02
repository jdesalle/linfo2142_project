#!/bin/bash
for FILENAME in empty_file file_1MB file_100MB file_250MB file_500MB #for each file size
do
	curl -k https://linfo2142.serv/files/$FILENAME -o $FILENAME	
done
