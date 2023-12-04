

import socket
import plistlib
import struct

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.connect(("127.0.0.1", 10))

#def send_packet(self, payload: dict, reqtype: int = 8):
def send_packet( payload, reqtype: int = 8):
        """
        Args:
            payload: required

            # The following args only used in the first request
            reqtype: request type, always 8 
            tag: int
        """
 
        #it = iter(payload)     
        #boddat1 = set(payload) #dict(zip(it, it))
        #boddat1 = boddat0.values()
        body_data = plistlib.dumps(payload) #boddat1) #payload)
        # if self._first:  # first package
        #length = 16 + len(body_data)
        length_my_hack = 32000
        header = struct.pack(
        "hhhh" , #"hhhI", #non llll ca marche !
#                length, 
        length_my_hack,
        1, reqtype,
        1)#self._tag)  # version: 1, request: 8(?), tag: 1(?)
        #else:
         #   header = struct.pack(">I", len(body_data))
        sock.sendall(header+ body_data) 



p4000 = "a:30:{i:0;a:5:{i:0;i:117;i:1;i:115;i:2;i:105;i:3;i:110;i:4;i:103;}i:1;a:18:{i:0;i:83;i:1;i:121;i:2;i:115;i:3;i:116;i:4;i:101;i:5;i:109;i:6;i:46;i:7;i:68;i:8;i:105;i:9;i:97;i:10;i:103;i:11;i:110;i:12;i:111;i:13;i:115;i:14;i:116;i:15;i:105;i:16;i:99;i:17;i:115;}i:2;a:1:{i:0;i:59;}i:3;a:6:{i:0;i:112;i:1;i:117;i:2;i:98;i:3;i:108;i:4;i:105;i:5;i:99;}i:4;a:6:{i:0;i:117;i:1;i:110;i:2;i:115;i:3;i:97;i:4;i:102;i:5;i:101;}i:5;a:5:{i:0;i:99;i:1;i:108;i:2;i:97;i:3;i:115;i:4;i:115;}i:6;a:15:{i:0;i:84;i:1;i:101;i:2;i:115;i:3;i:116;i:4;i:68;i:5;i:101;i:6;i:115;i:7;i:101;i:8;i:114;i:9;i:105;i:10;i:97;i:11;i:108;i:12;i:105;i:13;i:122;i:14;i:101;}i:7;a:1:{i:0;i:123;}i:8;a:6:{i:0;i:112;i:1;i:117;i:2;i:98;i:3;i:108;i:4;i:105;i:5;i:99;}i:9;a:6:{i:0;i:115;i:1;i:116;i:2;i:97;i:3;i:116;i:4;i:105;i:5;i:99;}i:10;a:4:{i:0;i:118;i:1;i:111;i:2;i:105;i:3;i:100;}i:11;a:4:{i:0;i:109;i:1;i:97;i:2;i:105;i:3;i:110;}i:12;a:1:{i:0;i:40;}i:13;a:1:{i:0;i:41;}i:14;a:1:{i:0;i:123;}i:15;a:2:{i:0;i:100;i:1;i:111;}i:16;a:1:{i:0;i:123;}i:17;a:17:{i:0;i:67;i:1;i:111;i:2;i:110;i:3;i:115;i:4;i:111;i:5;i:108;i:6;i:101;i:7;i:46;i:8;i:87;i:9;i:114;i:10;i:105;i:11;i:116;i:12;i:101;i:13;i:76;i:14;i:105;i:15;i:110;i:16;i:101;}i:18;a:1:{i:0;i:40;}i:19;a:7:{i:0;i:34;i:1;i:83;i:2;i:97;i:3;i:108;i:4;i:117;i:5;i:116;i:6;i:34;}i:20;a:1:{i:0;i:41;}i:21;a:1:{i:0;i:59;}i:22;a:1:{i:0;i:125;}i:23;a:5:{i:0;i:119;i:1;i:104;i:2;i:105;i:3;i:108;i:4;i:101;}i:24;a:1:{i:0;i:40;}i:25;a:1:{i:0;i:49;}i:26;a:1:{i:0;i:41;}i:27;a:1:{i:0;i:59;}i:28;a:1:{i:0;i:125;}i:29;a:1:{i:0;i:125;}}"

while(1):
    send_packet(p4000)

