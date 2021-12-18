This folder is used to host the certs used to configure our server, and script to create your owns.

In the local_CA folder, you will find the files for our local CA:

	- cert_info correspond to the values we gave to our cert
	- myCA.key is the private key that is used to sign server certs.
	- MyCa.pem and My_CA.cert both are the actual cert, in different format depending on the usage. 
	
In the server_cert folder, you'll find files for the actual certificate of ou server:
	
	- cert_info correspond to the values we gave to our cert
	- linfo2142_serv.key  is the private key that corresponf to our certificate
	- linfo2142_serv.crt is the actual cert
	- linfo2142_serv.csr is the certificate request
	- generate_serv_cert is the command that allow us to create a server certificate from our local CA certificate 
