==================================================
 Comparing TCP and QUIC through a satellite link
==================================================
----------------------------------------
by Samy Bettaieb and Jonathan de Salle
----------------------------------------

1) Introduction
====================

The objective of this project is to compare the performance of TCP and one QUIC implementation with real servers on the Internet through a satellite link. 
The measurements should be scripted and automatically analyzed to be easily performed and reproduced.

We decided to restrict ourselves to measuring the performance of both protocols in the case of a download from the satellite link, and will not measure the performances on the upload.  

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

4) Configuration of the server
==============================

5) Results
==========

6) Conclusions
=================
