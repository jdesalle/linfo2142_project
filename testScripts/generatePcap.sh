#!/bin/bash
for FILENAME in empty_file file_1MB file_100MB file_250MB file_500MB #for each file size
do
	for i in [1..10] #make each mesure 10 time
	do
		echo "$FILENAME,essais $i,TCP"
		curl -k -L -w "@curl-format.txt" https://linfo2142.serv/files/${FILENAME} -o test
		echo "$FILENAME,essais $i,QUIC"
		curl -k ---http3 -L -w "@curl-format.txt" https://linfo2142.serv/files/${FILENAME} -o test
	done
done

