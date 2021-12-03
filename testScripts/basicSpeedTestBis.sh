#!/bin/bash

rm -f basicSpeedTestBis.csv

printf '%s\n' file version iter time_namelookup time_connect time_appconnect time_pretransfer time_redirect time_starttransfer time_total | paste -sd ',' >> basicSpeedTestBis.csv

for FILENAME in empty_file #file_1MB file_100MB file_250MB file_500MB #for each file size
do
	for i in {1..100}; #make each mesure 10 time
	do
		
		output=$(~/curl/src/curl -L -w "@curl-format-for-csv.txt" -X GET -k -s https://130.104.229.21/files/${FILENAME} -o test | tail -n 1)
        printf '%s\n' $FILENAME tcp $i $output | paste -sd ',' >> basicSpeedTestBis.csv

	done
done

for FILENAME in empty_file #file_1MB file_100MB file_250MB file_500MB #for each file size
do
	for i in {1..100}; #make each mesure 10 time
	do
		
		output=$(~/curl/src/curl --http3 -L -w "@curl-format-for-csv.txt" -X GET -k -s https://130.104.229.21/files/${FILENAME} -o test | tail -n 1)
        printf '%s\n' $FILENAME quic $i $output | paste -sd ',' >> basicSpeedTestBis.csv

	done
done
