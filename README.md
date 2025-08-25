SMS Forwarder
=========
### Introduction
Python implementation to forward SMS from your extra SIM cards. \
Uses SMS Server Tools 3 https://smstools3.kekekasvi.com/ \
Requires a physical device to slot in SIM card.

### Setup
Default configuration location is at /etc/smsd.conf as per current documentation. \
\
Change the following lines \
```eventhandler = file_path/receive_forward.py``` \
where the file_path is to be changed.\
\
If your messages are not in ASCII, switch on the PDU storage to convert it \
```store_received_pdu = 3```
