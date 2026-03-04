import sqlite3

conn = sqlite3.connect("cryptora.db")
cur = conn.cursor()

questions = [
("Networking","What is IP?","Internet Protocol","Internal Process","Input Port","Internet Path","Internet Protocol","IP Addressing"),
("Networking","Port 80 is used for?","HTTP","FTP","SSH","DNS","HTTP","Ports"),
("Linux","Which command lists files?","ls","dir","show","list","ls","Linux Commands"),
("Cryptography","AES is?","Hashing","Encryption","Firewall","Protocol","Encryption","Encryption Types"),
("Ethical Hacking","Which tool scans network?","Nmap","Wireshark","Burp","Hydra","Nmap","Reconnaissance")
]

cur.executemany("""
INSERT INTO questions(topic,question,option1,option2,option3,option4,answer,concept)
VALUES(?,?,?,?,?,?,?,?)
""",questions)

conn.commit()
conn.close()

print("Questions Added Successfully")