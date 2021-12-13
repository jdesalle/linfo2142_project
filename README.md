# \[LINFO2142\] Project : Comparing TCP and QUIC through a satellite link
Project for LINFO2142, by Samy Bettaieb and Jonathan de Salle

The report of the project can be found in `report.rst`

## Experimental set up

### Prerequisite
To reproduce our experience you need install the following tools with the corresponding versions (see the commit id) :
* https://github.com/cloudflare/quiche
    - commit id : c885a71fd58c0c610e9e209f210b1951db81d6c5
* https://github.com/curl/curl/blob/master/docs/HTTP3.md#quiche-version
    - commit id : c8a3046555378f81b22d51e3887df8a5cf1ab5bf
* https://github.com/quiclog/pcap2qlog 
    - commit id : 62dbd8be1d3a3a040d1f3afc400bebfaa79658d7
    - You have to apply a patch to make it work (Big thanks to [François Michel](https://github.com/francoismichel))

### Methodology

Client characteristics :
* Operating System: Ubuntu 20.04.3 LTS
* Kernel: Linux 5.11.0-41-generic
* Architecture: x86-64

To compare the performance of TCP and QUIC, we decided to download files from our NGINX server using `curl` with the HTTP3 integration (quiche version).

**Examples** : 

Download using QUIC : 
```
curl --http3 -w "@curl-format.txt" -X GET -k  https://130.104.229.21/files/empty_file -o test
```

Download using TCP : 
```
curl -w "@curl-format.txt" -X GET -k  https://130.104.229.21/files/empty_file -o test
```