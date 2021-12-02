==================================================
 Comparing TCP and QUIC through a satellite link
==================================================
----------------------------------------
by Samy Bettaieb and Jonathan de Salle
----------------------------------------

1) Introduction
====================

The objective of this project is to compare the performance of TCP [1] and one QUIC [2] implementation with real servers on the Internet through a satellite link. 
The measurements should be scripted and automatically analyzed to be easily performed and reproduced.

We decided to restrict ourselves to measuring the performance of both protocols in the case of a download from the satellite link, and will not measure the performances on the upload.  

You can find the different files created for project at the link https://github.com/jdesalle/linfo2142_project . 

[1] https://datatracker.ietf.org/doc/html/rfc793

[2] https://datatracker.ietf.org/doc//html/rfc9000/

2) Tools
==========
To perform the measurements, we use several tools, which will be described in this section .

We have chosen to use cloudflare's implementation of QUIC: *Quiche* [1]  . We opted for that implementation, since it is compatible with a version of  *cURL* [2], which we use to perform our measurements.

To have a better control over our measurements, we implemented a web server using *Nginx 1.16*. The choice of the specific 1.16 version is because a patch for this version exist to use it with Quiche, which is the QUIC implementation we are using through this project. While Nginx has it's own implementation of QUIC, we choosed to keep a same implementation for the whole project. 

We use *Wireshark* to capture QUIC packets and analyze their different characteristics. We will also use *QUIClog* [3] to analyze theses packets.


[1] https://github.com/cloudflare/quiche 

[2] https://github.com/curl/curl/blob/master/docs/HTTP3.md#quiche-version

[3] https://github.com/quiclog

3) Methodology
===============
We will use a computer connected though a satellite link (starlink) to our web server to perform our measurement. During each measurement process, Wireshark will be monitoring the traffic to allow us to observe the negotiation of the bandwidth and other interesting information about the protocol directly.

During each mesurement, we will check the time needed for different things: 

* time for the namelookup 
* time to connect
* time to start  the transfer
* total time

We will study only the downloads, since it's more relevant than uploads for a satellite connection users.

We will repeat each measurement 10 times. We will first try to download a simple blank web page, then we will try to download files with a size ranging form 10kB to 500MB, to see if the size of a file downloaded through the satellite link will impact the performance of the said connection.


1) Configuration of the server
==============================
The first step of our configuration is to add your serve in the /etc/host file , and use the domain name linfo2142.serv for our scripts to work. In our case, the ip of our server is 130.104.229.21, the command to do this is  *$ sudo echo "130.104.229.21    linfo2142" >> /etc/hosts*

The next step is to proceed to the installation of our version of nginx. The basic explanation for building a nginx 1.16 server with quiche can be found online [1]. You may have to install some dependencies using your preferred package manager. 


After building nginx, you will have to add it to your path variable. There is multiple way to do this, we choosed to add it in /etc/environement.

You will have to add the files [2] for the measurements in the /var/www/files folder, so that they will be accessible by the server. This repository mus be accessible by any user.

To run nginx, you wil have to add our nginx.conf [3] file in your nginx repository. You'll also need to put the SSL key [4] and certificate [5] of our server in a folder named "certs" created in the same directory. 
When that is done, you can run the command  *$ nginx -c nginx.conf* to launch the server.

[1] https://blog.cloudflare.com/experiment-with-http-3-using-nginx-and-quiche/ 

[2]

[3] https://github.com/jdesalle/linfo2142_project/blob/main/nginx.conf

[4] https://github.com/jdesalle/linfo2142_project/blob/main/certs/server_cert/linfo2142_serv.key

[5] https://github.com/jdesalle/linfo2142_project/blob/main/certs/server_cert/linfo2142_serv.crt

5) Results
==========

6) Conclusions
=================
