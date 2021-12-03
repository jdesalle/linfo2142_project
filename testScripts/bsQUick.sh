#!/bin/bash


for FILENAME in  file_1MB file_100MB file_250MB file_500MB #for each file size
do
	for i in {3..10}; #make each mesure 10 time
	do
		
		output=$(~/curl/src/curl --http3 -L -w "@curl-format-for-csv.txt" -X GET -k -s https://130.104.229.21/files/${FILENAME} -o test | tail -n 1)
        printf '%s\n' $FILENAME quic $i $output | paste -sd ',' >> basicSpeedTest.csv

	done
done
