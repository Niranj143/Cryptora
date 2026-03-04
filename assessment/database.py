import sqlite3

conn = sqlite3.connect("assessment/cryptora.db")
cur = conn.cursor()

# Create questions table
cur.execute("""
CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    level TEXT,
    question TEXT,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    answer TEXT
)
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT,
    score INTEGER,
    total INTEGER,
    percentage REAL,
    status TEXT
)

""")
# Clear old wrong questions
cur.execute("DELETE FROM questions")

# ---------------- NETWORKING BEGINNER QUESTIONS ----------------

questions = [
("Networking","Beginner","What does IP stand for?","Internal Protocol","Internet Protocol","Interior Post","Instant Path","B"),
("Networking","Beginner","Which OSI layer handles routing?","Physical","Data Link","Network","Transport","C"),
("Networking","Beginner","HTTP default port?","21","80","443","25","B"),
("Networking","Beginner","Device connecting networks?","Hub","Switch","Router","Repeater","C"),
("Networking","Beginner","IPv4 size?","32 bits","64 bits","128 bits","48 bits","A"),
("Networking","Beginner","Secure remote login protocol?","Telnet","FTP","SSH","HTTP","C"),
("Networking","Beginner","DNS purpose?","Encrypt data","Translate domain names","Route packets","Assign IP","B"),
("Networking","Beginner","Connectionless protocol?","TCP","FTP","UDP","HTTP","C"),
("Networking","Beginner","MAC address is?","Logical","Physical","IP","Port","B"),
("Networking","Beginner","Top OSI layer?","Application","Presentation","Session","Transport","A"),
("Networking","Beginner","DHCP stands for?","Data Hub","Dynamic Host Configuration Protocol","Direct Host","Digital Host","B"),
("Networking","Beginner","Layer 2 device?","Router","Switch","Firewall","Gateway","B"),
("Networking","Beginner","Loopback IP?","192.168.1.1","127.0.0.1","10.0.0.1","8.8.8.8","B"),
("Networking","Beginner","Email sending protocol?","POP3","IMAP","SMTP","SNMP","C"),
("Networking","Beginner","LAN means?","Long Area","Local Area Network","Light Access","Logical Array","B"),
("Networking","Beginner","Private IP range?","8.8.4.4","172.16.0.0","1.1.1.1","208.67.222.222","B"),
("Networking","Beginner","Subnet mask purpose?","Hide IP","Identify network/host","Speed internet","Block hackers","B"),
("Networking","Beginner","TCP/IP layers?","7","5","4","3","C"),
("Networking","Beginner","Bus topology uses?","Single cable","Ring cable","Mesh","Wireless","A"),
("Networking","Beginner","Cat5e max speed?","10 Mbps","100 Mbps","1000 Mbps","10 Gbps","C"),
# -------- NETWORKING INTERMEDIATE --------

("Networking", "Intermediate", "Which OSI layer ensures reliable data delivery?", 
 "Application", "Transport", "Network", "Session", "B"),

("Networking", "Intermediate", "Which protocol uses port 443?", 
 "HTTP", "HTTPS", "FTP", "SMTP", "B"),

("Networking", "Intermediate", "What device filters traffic using rules?", 
 "Switch", "Router", "Firewall", "Repeater", "C"),

("Networking", "Intermediate", "Which command checks network connectivity?", 
 "ping", "mkdir", "copy", "dir", "A"),

("Networking", "Intermediate", "Which protocol resolves IP to MAC address?", 
 "DNS", "ARP", "DHCP", "ICMP", "B"),

("Networking", "Intermediate", "What does NAT primarily do?", 
 "Encrypt data", "Translate private IP to public IP", "Increase bandwidth", "Block malware", "B"),

("Networking", "Intermediate", "Which layer handles encryption in OSI?", 
 "Presentation", "Transport", "Network", "Physical", "A"),

("Networking", "Intermediate", "Which protocol is used for network diagnostics?", 
 "ICMP", "FTP", "SMTP", "POP3", "A"),

("Networking", "Intermediate", "Which topology provides highest redundancy?", 
 "Bus", "Star", "Mesh", "Ring", "C"),

("Networking", "Intermediate", "Which port is used by SSH?", 
 "21", "22", "25", "110", "B"),

("Networking", "Intermediate", "Which protocol dynamically assigns IP addresses?", 
 "ARP", "DNS", "DHCP", "HTTP", "C"),

("Networking", "Intermediate", "What is subnetting used for?", 
 "Increase cable length", "Divide networks into smaller networks", "Speed internet", "Encrypt packets", "B"),

("Networking", "Intermediate", "Which protocol transfers files securely?", 
 "FTP", "SFTP", "HTTP", "SNMP", "B"),

("Networking", "Intermediate", "Which OSI layer handles routing decisions?", 
 "Transport", "Network", "Session", "Data Link", "B"),

("Networking", "Intermediate", "Which address uniquely identifies a device hardware?", 
 "IP address", "MAC address", "Port number", "Subnet", "B"),

("Networking", "Intermediate", "Which protocol translates domain names?", 
 "DNS", "ICMP", "ARP", "SMTP", "A"),

("Networking", "Intermediate", "What is the default subnet mask of Class C?", 
 "255.0.0.0", "255.255.0.0", "255.255.255.0", "255.255.255.255", "C"),

("Networking", "Intermediate", "Which protocol is connection-oriented?", 
 "UDP", "TCP", "ICMP", "ARP", "B"),

("Networking", "Intermediate", "Which command displays IP configuration in Windows?", 
 "ipconfig", "ifconfig", "netstat", "ping", "A"),

("Networking", "Intermediate", "Which layer controls data framing?", 
 "Physical", "Data Link", "Network", "Application", "B"),
 # -------- NETWORKING ADVANCED --------

("Networking", "Advanced", "Which protocol prevents switching loops?", 
 "STP", "ARP", "ICMP", "RIP", "A"),

("Networking", "Advanced", "Which routing protocol is link-state?", 
 "RIP", "OSPF", "BGP", "EIGRP", "B"),

("Networking", "Advanced", "What does CIDR stand for?", 
 "Classless Inter-Domain Routing", "Central IP Data Routing", "Controlled Internet Domain Routing", "Class IP Dynamic Routing", "A"),

("Networking", "Advanced", "Which protocol is used for secure web communication?", 
 "HTTP", "HTTPS", "FTP", "Telnet", "B"),

("Networking", "Advanced", "Which device operates at Layer 3?", 
 "Hub", "Switch", "Router", "Repeater", "C"),

("Networking", "Advanced", "Which protocol monitors network devices?", 
 "SNMP", "SMTP", "SSH", "ARP", "A"),

("Networking", "Advanced", "Which attack floods a network with traffic?", 
 "Phishing", "DoS", "Spoofing", "Sniffing", "B"),

("Networking", "Advanced", "Which command shows active connections?", 
 "netstat", "ping", "mkdir", "route", "A"),

("Networking", "Advanced", "Which protocol uses three-way handshake?", 
 "UDP", "TCP", "ICMP", "ARP", "B"),

("Networking", "Advanced", "Which routing protocol is used on the internet backbone?", 
 "RIP", "OSPF", "BGP", "IGRP", "C"),

("Networking", "Advanced", "Which technology separates broadcast domains?", 
 "VLAN", "Hub", "Repeater", "Bridge", "A"),

("Networking", "Advanced", "Which protocol provides time synchronization?", 
 "FTP", "NTP", "SNMP", "SMTP", "B"),

("Networking", "Advanced", "Which port does DNS primarily use?", 
 "21", "53", "80", "110", "B"),

("Networking", "Advanced", "Which security method verifies device identity?", 
 "Authentication", "Compression", "Routing", "Fragmentation", "A"),

("Networking", "Advanced", "Which attack intercepts communication secretly?", 
 "MITM", "DoS", "Phishing", "Brute force", "A"),

("Networking", "Advanced", "Which protocol encrypts remote connections?", 
 "Telnet", "SSH", "HTTP", "SNMP", "B"),

("Networking", "Advanced", "Which IPv6 address represents loopback?", 
 "::1", "127.0.0.1", "::FFFF", "FE80::1", "A"),

("Networking", "Advanced", "Which firewall filters by IP and port?", 
 "Packet-filtering firewall", "Proxy firewall", "Application firewall", "Stateful inspection firewall", "A"),

("Networking", "Advanced", "Which protocol maps IP to MAC address?", 
 "ARP", "DNS", "DHCP", "ICMP", "A"),

("Networking", "Advanced", "Which OSI layer manages sessions?", 
 "Session Layer", "Transport Layer", "Network Layer", "Physical Layer", "A"),
 # -------- ETHICAL HACKING BEGINNER --------

("Ethical Hacking","Beginner","What is ethical hacking?","Legal security testing","Illegal hacking","Data stealing","Spamming","A"),

("Ethical Hacking","Beginner","Who is an ethical hacker?","Authorized security tester","Cyber criminal","Spammer","Anonymous user","A"),

("Ethical Hacking","Beginner","What is the goal of ethical hacking?","Improve security","Destroy systems","Steal passwords","Spread malware","A"),

("Ethical Hacking","Beginner","Which tool scans open ports?","Nmap","Photoshop","Excel","Chrome","A"),

("Ethical Hacking","Beginner","Which attack guesses passwords repeatedly?","Brute force","Phishing","Sniffing","Spoofing","A"),

("Ethical Hacking","Beginner","What is phishing?","Fake message to steal data","Network repair","Firewall setup","Encryption","A"),

("Ethical Hacking","Beginner","Which tool is used for penetration testing OS?","Kali Linux","Windows Media Player","Notepad","Paint","A"),

("Ethical Hacking","Beginner","What does VPN do?","Encrypts connection","Deletes files","Boosts CPU","Blocks RAM","A"),

("Ethical Hacking","Beginner","Which attack overloads servers?","DoS","SQL","ARP","DNS","A"),

("Ethical Hacking","Beginner","Which tool captures network packets?","Wireshark","Word","PowerPoint","VLC","A"),

("Ethical Hacking","Beginner","What is malware?","Malicious software","Backup software","Antivirus","Driver","A"),

("Ethical Hacking","Beginner","Which attack pretends to be trusted source?","Spoofing","Routing","Switching","Scanning","A"),

("Ethical Hacking","Beginner","Which is a strong password?","P@ssw0rd!23","123456","password","abc","A"),

("Ethical Hacking","Beginner","Firewall purpose?","Block unauthorized access","Increase storage","Speed CPU","Install apps","A"),

("Ethical Hacking","Beginner","What is vulnerability?","Security weakness","Backup file","Network cable","Protocol","A"),

("Ethical Hacking","Beginner","Which attack listens to traffic secretly?","Sniffing","Routing","Hashing","Encoding","A"),

("Ethical Hacking","Beginner","Penetration testing means?","Testing system security","Installing OS","Coding","Gaming","A"),

("Ethical Hacking","Beginner","Which tool cracks passwords?","John the Ripper","Excel","Chrome","Zoom","A"),

("Ethical Hacking","Beginner","Social engineering targets?","Humans","Routers","Cables","Servers","A"),

("Ethical Hacking","Beginner","Ethical hacking requires?","Permission","Anonymous access","Illegal entry","No rules","A"),
# -------- ETHICAL HACKING INTERMEDIATE --------

("Ethical Hacking","Intermediate","Which phase identifies targets?","Reconnaissance","Exploitation","Reporting","Cleanup","A"),

("Ethical Hacking","Intermediate","Active information gathering involves?","Direct interaction","Offline research","Documentation","Encryption","A"),

("Ethical Hacking","Intermediate","Which scan detects open ports?","TCP scan","Ping sweep","ARP scan","DNS lookup","A"),

("Ethical Hacking","Intermediate","SQL Injection targets?","Databases","RAM","GPU","Keyboard","A"),

("Ethical Hacking","Intermediate","XSS attack injects?","Scripts","Images","Drivers","Updates","A"),

("Ethical Hacking","Intermediate","Metasploit is used for?","Exploitation framework","Antivirus","Firewall","Backup","A"),

("Ethical Hacking","Intermediate","Privilege escalation means?","Gain higher access","Delete logs","Scan ports","Encrypt files","A"),

("Ethical Hacking","Intermediate","Hashing is used for?","Password storage","Routing","Switching","Compression","A"),

("Ethical Hacking","Intermediate","Dictionary attack uses?","Wordlist","Encryption key","Firewall","Router","A"),

("Ethical Hacking","Intermediate","Which tool performs vulnerability scanning?","OpenVAS","Paint","Excel","Zoom","A"),

("Ethical Hacking","Intermediate","MITM stands for?","Man in the Middle","Machine Internet Mode","Main Transfer Method","Multi Input Model","A"),

("Ethical Hacking","Intermediate","Footprinting gathers?","Target information","Passwords only","Logs only","Images","A"),

("Ethical Hacking","Intermediate","Reverse shell gives?","Remote command access","Encryption","Backup","Firewall rules","A"),

("Ethical Hacking","Intermediate","Which attack modifies DNS response?","DNS Spoofing","ARP scanning","SMTP relay","Port forwarding","A"),

("Ethical Hacking","Intermediate","Password salting prevents?","Rainbow attacks","Scanning","Routing","Compression","A"),

("Ethical Hacking","Intermediate","Hydra tool is used for?","Password cracking","Packet routing","Firewall setup","Coding","A"),

("Ethical Hacking","Intermediate","Enumeration phase collects?","Users and services","Images","Videos","Logs only","A"),

("Ethical Hacking","Intermediate","Burp Suite tests?","Web applications","Drivers","Hardware","Memory","A"),

("Ethical Hacking","Intermediate","Session hijacking steals?","Session tokens","RAM","CPU","Files","A"),

("Ethical Hacking","Intermediate","Ethical hacker final step?","Reporting","Deleting system","Rebooting","Encrypting","A"),
# -------- ETHICAL HACKING ADVANCED --------

("Ethical Hacking","Advanced","Zero-day vulnerability means?","Unknown flaw","Patched bug","Firewall rule","Encrypted data","A"),

("Ethical Hacking","Advanced","Buffer overflow affects?","Memory","CPU speed","Network cable","Keyboard","A"),

("Ethical Hacking","Advanced","Which attack poisons ARP cache?","ARP Spoofing","DNS Query","HTTP Flood","Port Scan","A"),

("Ethical Hacking","Advanced","Pivoting allows?","Access deeper networks","Delete logs","Encrypt disks","Scan emails","A"),

("Ethical Hacking","Advanced","Rootkit hides?","Malicious activity","Passwords","Images","Drivers","A"),

("Ethical Hacking","Advanced","Which framework automates exploits?","Metasploit","Wireshark","Nmap","Tcpdump","A"),

("Ethical Hacking","Advanced","Rainbow table attacks break?","Hashes","Firewalls","Routers","Protocols","A"),

("Ethical Hacking","Advanced","Privilege escalation vulnerability occurs due to?","Improper permissions","Encryption","Routing","Compression","A"),

("Ethical Hacking","Advanced","Command injection executes?","System commands","Images","Packets","Drivers","A"),

("Ethical Hacking","Advanced","Which attack steals cookies?","Session hijacking","DoS","Spoofing","Scanning","A"),

("Ethical Hacking","Advanced","Persistence ensures?","Continued access","Faster internet","Encryption","Backup","A"),

("Ethical Hacking","Advanced","Which attack modifies packets in transit?","MITM","DoS","Phishing","Brute force","A"),

("Ethical Hacking","Advanced","Exploit payload means?","Code executed after exploit","Firewall","Patch","Driver","A"),

("Ethical Hacking","Advanced","Post exploitation phase involves?","Maintaining access","Scanning","Recon","Enumeration","A"),

("Ethical Hacking","Advanced","Lateral movement spreads through?","Network systems","Keyboard","Mouse","Printer","A"),

("Ethical Hacking","Advanced","Credential dumping extracts?","Passwords","Logs","Images","Drivers","A"),

("Ethical Hacking","Advanced","Which attack abuses trust relationships?","Pass-the-Hash","Ping sweep","ARP scan","DNS lookup","A"),

("Ethical Hacking","Advanced","Sandbox evasion avoids?","Detection","Encryption","Routing","Compression","A"),

("Ethical Hacking","Advanced","Red teaming simulates?","Real attacks","Backup","Updates","Monitoring","A"),

("Ethical Hacking","Advanced","Blue team focuses on?","Defense","Attacks","Scanning","Spoofing","A"),
("Linux","Beginner","Which command lists files in Linux?","ls","dir","show","list","A"),
("Linux","Beginner","Which command changes directory?","cd","move","change","dir","A"),
("Linux","Beginner","Linux is based on which OS concept?","Unix","Windows","DOS","Android","A"),
("Linux","Beginner","Which command shows current directory?","pwd","where","path","dir","A"),
("Linux","Beginner","Which symbol represents root directory?","/","\\","#","~","A"),
("Linux","Beginner","Which command creates a folder?","mkdir","make","create","newdir","A"),
("Linux","Beginner","Which command deletes a file?","rm","delete","removefile","del","A"),
("Linux","Beginner","Which command displays file content?","cat","show","read","open","A"),
("Linux","Beginner","Which user has highest privileges?","root","admin","user","guest","A"),
("Linux","Beginner","Linux kernel manages?","Hardware resources","Only files","Only users","Internet","A"),
("Linux","Beginner","Which command clears terminal?","clear","cls","reset","wipe","A"),
("Linux","Beginner","Which command copies files?","cp","copy","clone","mv","A"),
("Linux","Beginner","Which command moves files?","mv","move","transfer","shift","A"),
("Linux","Beginner","Which command shows manual pages?","man","help","info","guide","A"),
("Linux","Beginner","Which file stores users info?","/etc/passwd","/users","/home","/root","A"),
("Linux","Beginner","Linux is mainly used for?","Servers","Gaming","Office only","Design only","A"),
("Linux","Beginner","Which command shows username?","whoami","user","name","iduser","A"),
("Linux","Beginner","Hidden files start with?","Dot (.)","Hash (#)","Star (*)","Dash (-)","A"),
("Linux","Beginner","Which command edits files (basic editor)?","nano","paint","edit","writer","A"),
("Linux","Beginner","Linux is?","Open source","Paid only","Closed system","Mobile OS only","A"),
("Linux","Intermediate","Which command changes file permissions?","chmod","chperm","perm","setperm","A"),
("Linux","Intermediate","Which command changes file ownership?","chown","own","owner","setown","A"),
("Linux","Intermediate","Permission 755 means?","Owner full, others read & execute","Everyone full access","Read only","Execute only","A"),
("Linux","Intermediate","Which command shows running processes?","ps","process","run","jobs","A"),
("Linux","Intermediate","Which command displays real-time processes?","top","pslive","monitor","watch","A"),
("Linux","Intermediate","Which command searches text inside files?","grep","search","findtext","lookup","A"),
("Linux","Intermediate","Which command downloads files from internet?","wget","download","fetch","get","A"),
("Linux","Intermediate","Which command checks disk usage?","df","disk","usage","du","A"),
("Linux","Intermediate","Which command shows folder size?","du","df","size","space","A"),
("Linux","Intermediate","Which directory stores system configs?","/etc","/config","/system","/var","A"),
("Linux","Intermediate","Which command archives files?","tar","zip","archive","pack","A"),
("Linux","Intermediate","Which command compresses files using gzip?","gzip","compress","zip","pack","A"),
("Linux","Intermediate","Which command displays network interfaces?","ifconfig","netshow","ipview","network","A"),
("Linux","Intermediate","Modern replacement for ifconfig?","ip","net","route","config","A"),
("Linux","Intermediate","Which file stores hostname?","/etc/hostname","/hostname","/host","/etc/hosts","A"),
("Linux","Intermediate","Which command schedules tasks?","cron","schedule","timer","task","A"),
("Linux","Intermediate","Cron jobs stored in?","crontab","cronfile","tasks","schedule","A"),
("Linux","Intermediate","Which command installs packages (Ubuntu)?","apt","install","pkg","dpkg","A"),
("Linux","Intermediate","Which log directory stores logs?","/var/log","/logs","/system/log","/etc/log","A"),
("Linux","Intermediate","Which command shows memory usage?","free","memory","ram","mem","A"),
("Linux","Advanced","Which command grants temporary root privileges?","sudo","root","admin","suuser","A"),
("Linux","Advanced","Which file stores user account information?","/etc/passwd","/etc/users","/users","/home/passwd","A"),
("Linux","Advanced","Which file stores encrypted passwords?","/etc/shadow","/etc/passwd","/shadow","/secure","A"),
("Linux","Advanced","Which command switches user?","su","switch","userchange","login","A"),
("Linux","Advanced","Which command manages services in systemd?","systemctl","servicectl","sysmanage","daemonctl","A"),
("Linux","Advanced","Start a service command?","systemctl start","service run","start service","runservice","A"),
("Linux","Advanced","Which command checks open ports?","netstat","portcheck","openports","listen","A"),
("Linux","Advanced","Modern replacement for netstat?","ss","netinfo","ipstat","ports","A"),
("Linux","Advanced","Which command captures packets?","tcpdump","packetcap","sniff","capture","A"),
("Linux","Advanced","Which shell scripting symbol stores variable?","=","==",":=","->","A"),
("Linux","Advanced","Which command edits files in terminal?","nano","edit","write","change","A"),
("Linux","Advanced","Powerful Linux editor used by hackers?","vim","nano","edit","code","A"),
("Linux","Advanced","Which command finds files system-wide?","find","search","lookup","scan","A"),
("Linux","Advanced","Which command shows active connections?","ss","connect","net","link","A"),
("Linux","Advanced","Which command kills a process?","kill","stop","terminate","end","A"),
("Linux","Advanced","Force kill process signal?","-9","-1","-5","-2","A"),
("Linux","Advanced","Which directory contains boot files?","/boot","/startup","/init","/system","A"),
("Linux","Advanced","Which command checks kernel version?","uname -r","kernel","version","sysinfo","A"),
("Linux","Advanced","Which log shows authentication events?","auth.log","login.log","secure.log","user.log","A"),
("Linux","Advanced","Which tool analyzes system logs?","journalctl","logview","syslog","analyze","A"),
("Cryptography","Beginner","What is cryptography?","Protecting information using codes","Breaking hardware","Speeding internet","Data deletion","A"),
("Cryptography","Beginner","Plain text means?","Original readable data","Encrypted data","Binary data","Compressed file","A"),
("Cryptography","Beginner","Cipher text is?","Encrypted message","Plain message","Password","Hash value","A"),
("Cryptography","Beginner","Which is symmetric encryption?","AES","RSA","ECC","Diffie-Hellman","A"),
("Cryptography","Beginner","Which is asymmetric encryption?","RSA","AES","DES","Blowfish","A"),
("Cryptography","Beginner","Encryption converts?","Plaintext to ciphertext","Ciphertext to plaintext","Data to image","Password to hash","A"),
("Cryptography","Beginner","Decryption converts?","Ciphertext to plaintext","Plaintext to cipher","Hash to text","Binary to text","A"),
("Cryptography","Beginner","Secret key encryption is called?","Symmetric","Asymmetric","Public","Hashing","A"),
("Cryptography","Beginner","Public key is used in?","Asymmetric encryption","Symmetric encryption","Hashing","Compression","A"),
("Cryptography","Beginner","AES stands for?","Advanced Encryption Standard","Automatic Encryption System","Advanced Electronic Security","Applied Encryption Service","A"),
("Cryptography","Beginner","DES is?","Encryption algorithm","Operating system","Firewall","Protocol","A"),
("Cryptography","Beginner","Hashing is used for?","Integrity verification","Speed increase","Network routing","Compression","A"),
("Cryptography","Beginner","Which is a hash algorithm?","SHA-256","AES","RSA","DES","A"),
("Cryptography","Beginner","MD5 produces how many bits?","128 bits","64 bits","256 bits","512 bits","A"),
("Cryptography","Beginner","Digital signature ensures?","Authentication","Compression","Speed","Routing","A"),
("Cryptography","Beginner","SSL is used for?","Secure communication","File storage","Backup","Compression","A"),
("Cryptography","Beginner","HTTPS uses?","Encryption","Compression","Caching","Routing","A"),
("Cryptography","Beginner","Key used to decrypt in symmetric crypto?","Same key","Public key","Different key","Hash key","A"),
("Cryptography","Beginner","Brute force attack means?","Trying many passwords","Deleting files","Network scanning","Packet routing","A"),
("Cryptography","Beginner","Cryptography mainly provides?","Confidentiality","Storage","Speed","Design","A"),
("Cryptography","Intermediate","Which algorithm is commonly used for key exchange?","Diffie-Hellman","AES","DES","MD5","A"),
("Cryptography","Intermediate","RSA encryption uses?","Public and private keys","Single key","Hash value","Password only","A"),
("Cryptography","Intermediate","Block cipher operates on?","Fixed-size blocks","Single bits","Characters","Packets","A"),
("Cryptography","Intermediate","Stream cipher encrypts?","One bit at a time","Blocks","Files","Packets","A"),
("Cryptography","Intermediate","Which AES key size is valid?","128 bits","40 bits","32 bits","16 bits","A"),
("Cryptography","Intermediate","Digital certificates are issued by?","Certificate Authority","Firewall","Router","Switch","A"),
("Cryptography","Intermediate","PKI stands for?","Public Key Infrastructure","Private Key Internet","Protected Key Interface","Public Kernel Integration","A"),
("Cryptography","Intermediate","Hash functions provide?","Integrity","Confidentiality","Compression","Routing","A"),
("Cryptography","Intermediate","Collision in hashing means?","Two inputs same hash","Encryption failure","Wrong password","Network error","A"),
("Cryptography","Intermediate","Which protocol secures email?","PGP","FTP","HTTP","ARP","A"),
("Cryptography","Intermediate","TLS is successor of?","SSL","SSH","IPSec","HTTPS","A"),
("Cryptography","Intermediate","Which mode hides repeating patterns?","CBC","ECB","ASCII","RAW","A"),
("Cryptography","Intermediate","ECB mode weakness?","Pattern visibility","Slow speed","Key loss","Packet drop","A"),
("Cryptography","Intermediate","Nonce means?","Number used once","Encryption key","Hash output","Certificate","A"),
("Cryptography","Intermediate","Salting passwords prevents?","Rainbow table attacks","Phishing","Spoofing","Scanning","A"),
("Cryptography","Intermediate","Which algorithm is asymmetric?","RSA","AES","DES","RC4","A"),
("Cryptography","Intermediate","Message authentication ensures?","Integrity and authenticity","Speed","Compression","Routing","A"),
("Cryptography","Intermediate","MAC stands for?","Message Authentication Code","Media Access Control","Memory Access Code","Main Access Channel","A"),
("Cryptography","Intermediate","Which algorithm replaced DES?","AES","RSA","MD5","SHA1","A"),
("Cryptography","Intermediate","Key length increase results in?","Stronger security","Faster encryption","Less storage","Smaller keys","A"),
("Cryptography","Advanced","Which attack tries all possible keys?","Brute force","Phishing","Spoofing","Sniffing","A"),
("Cryptography","Advanced","RSA security depends on difficulty of?","Prime factorization","Sorting","Compression","Routing","A"),
("Cryptography","Advanced","Elliptic Curve Cryptography provides?","Strong security with smaller keys","Faster internet","Compression","Packet filtering","A"),
("Cryptography","Advanced","Forward secrecy ensures?","Past sessions remain secure","Faster encryption","Key reuse","Data backup","A"),
("Cryptography","Advanced","TLS handshake establishes?","Secure session keys","IP addresses","Routing tables","Passwords","A"),
("Cryptography","Advanced","Which attack targets hash collisions?","Birthday attack","MITM","DoS","Phishing","A"),
("Cryptography","Advanced","Digital signature uses?","Private key for signing","Public key only","Hash only","Password only","A"),
("Cryptography","Advanced","Verification of signature uses?","Public key","Private key","Hash key","Session key","A"),
("Cryptography","Advanced","Perfect forward secrecy uses?","Ephemeral keys","Static keys","Weak keys","Shared passwords","A"),
("Cryptography","Advanced","Side-channel attacks exploit?","Physical implementation leaks","Network speed","Routing errors","Packets","A"),
("Cryptography","Advanced","Which algorithm supports digital signatures?","RSA","AES","DES","RC4","A"),
("Cryptography","Advanced","HMAC combines hash with?","Secret key","Public key","Certificate","Router","A"),
("Cryptography","Advanced","Which attack modifies encrypted traffic secretly?","MITM","DoS","Brute force","Scanning","A"),
("Cryptography","Advanced","Quantum computing threatens?","RSA encryption","AES slightly","Firewalls","Switches","A"),
("Cryptography","Advanced","Which protocol secures VPN tunnels?","IPSec","FTP","SMTP","ARP","A"),
("Cryptography","Advanced","Key escrow means?","Third party holds keys","Key deletion","Encryption failure","Hash storage","A"),
("Cryptography","Advanced","Zero knowledge proof allows?","Verification without revealing secret","Password sharing","Key exchange","Compression","A"),
("Cryptography","Advanced","Entropy in cryptography measures?","Randomness","Speed","Storage","Latency","A"),
("Cryptography","Advanced","Replay attack repeats?","Captured valid messages","Passwords","Packets randomly","Logs","A"),
("Cryptography","Advanced","Post-quantum cryptography protects against?","Quantum attacks","Network attacks","DoS","Malware","A"),
("OS & Security","Beginner","What is an Operating System?","Software managing hardware","Antivirus","Application","Network device","A"),
("OS & Security","Beginner","Which OS is open source?","Linux","Windows","macOS","iOS","A"),
("OS & Security","Beginner","Authentication means?","Verifying identity","Deleting files","Encrypting data","Routing traffic","A"),
("OS & Security","Beginner","Authorization decides?","Access permissions","Login name","Password length","Network speed","A"),
("OS & Security","Beginner","Strong password should include?","Letters numbers symbols","Only numbers","Only letters","Only symbols","A"),
("OS & Security","Beginner","Firewall protects against?","Unauthorized access","Power failure","Hardware damage","Overheating","A"),
("OS & Security","Beginner","Malware is?","Malicious software","Backup software","System update","Driver","A"),
("OS & Security","Beginner","Antivirus detects?","Malware","Hardware errors","Network cables","Drivers","A"),
("OS & Security","Beginner","User account control limits?","Unauthorized changes","Internet speed","Disk space","RAM usage","A"),
("OS & Security","Beginner","Which OS component manages processes?","Kernel","Browser","Application","Printer","A"),
("OS & Security","Beginner","Boot process starts with?","BIOS/UEFI","Application","Browser","Firewall","A"),
("OS & Security","Beginner","Access control restricts?","System resources","CPU speed","Graphics","Battery","A"),
("OS & Security","Beginner","Patch updates fix?","Security vulnerabilities","Hardware","Keyboard","Network cables","A"),
("OS & Security","Beginner","Which attack tricks users?","Phishing","Routing","Switching","Hashing","A"),
("OS & Security","Beginner","Backup protects against?","Data loss","Malware creation","Routing errors","Compression","A"),
("OS & Security","Beginner","Login password provides?","Authentication","Encryption","Compression","Routing","A"),
("OS & Security","Beginner","Which OS feature isolates apps?","Sandboxing","Routing","Switching","Hashing","A"),
("OS & Security","Beginner","Administrator account has?","Highest privileges","Lowest privileges","Guest rights","No rights","A"),
("OS & Security","Beginner","System logs record?","System activities","Games","Images","Videos","A"),
("OS & Security","Beginner","Security updates should be?","Regularly installed","Ignored","Deleted","Disabled","A"),
("OS & Security","Intermediate","What does least privilege principle mean?","Users get minimal access","Full access","No access","Admin rights","A"),
("OS & Security","Intermediate","Which mechanism isolates processes?","Memory protection","Routing","Switching","Compression","A"),
("OS & Security","Intermediate","Virtual memory uses?","Disk as RAM extension","CPU cache","GPU memory","Network storage","A"),
("OS & Security","Intermediate","Which attack exploits buffer overflow?","Memory overwrite","Password guessing","Phishing","Scanning","A"),
("OS & Security","Intermediate","File permissions control?","Access rights","CPU speed","Network traffic","Graphics","A"),
("OS & Security","Intermediate","Which OS security logs login attempts?","Authentication logs","Media logs","Video logs","Backup logs","A"),
("OS & Security","Intermediate","Multi-factor authentication requires?","Multiple verification methods","Single password","Username only","IP address","A"),
("OS & Security","Intermediate","Which component handles scheduling?","Scheduler","Firewall","Router","Browser","A"),
("OS & Security","Intermediate","Process isolation prevents?","Unauthorized access","Faster boot","More storage","Compression","A"),
("OS & Security","Intermediate","Which attack escalates privileges?","Privilege escalation","Phishing","Sniffing","Spoofing","A"),
("OS & Security","Intermediate","Secure boot verifies?","System integrity","Internet speed","Applications","Drivers only","A"),
("OS & Security","Intermediate","Which protects memory from execution attacks?","DEP","DNS","ARP","FTP","A"),
("OS & Security","Intermediate","ASLR randomizes?","Memory addresses","Passwords","Files","Logs","A"),
("OS & Security","Intermediate","Which control tracks user actions?","Audit logs","Firewall","Encryption","Routing","A"),
("OS & Security","Intermediate","Kernel mode has?","Full hardware access","Limited access","Guest rights","No access","A"),
("OS & Security","Intermediate","User mode restricts?","Hardware access","Internet access","File names","Passwords","A"),
("OS & Security","Intermediate","Patch management prevents?","Known vulnerabilities","Hardware damage","Power loss","Overheating","A"),
("OS & Security","Intermediate","Which attack records keystrokes?","Keylogger","DoS","ARP spoofing","MITM","A"),
("OS & Security","Intermediate","Secure OS design includes?","Access control","Gaming","Graphics","Streaming","A"),
("OS & Security","Intermediate","System hardening means?","Reducing attack surface","Adding apps","Increasing RAM","Deleting logs","A"),
("OS & Security","Advanced","Kernel operates in which mode?","Kernel mode","User mode","Guest mode","Safe mode","A"),
("OS & Security","Advanced","Mandatory Access Control is implemented by?","SELinux","Firewall","Router","Browser","A"),
("OS & Security","Advanced","SELinux primarily provides?","Access control policies","Encryption","Compression","Routing","A"),
("OS & Security","Advanced","Sandboxing prevents?","Application system access","Internet usage","File creation","Login attempts","A"),
("OS & Security","Advanced","Rootkits aim to?","Hide malicious activity","Improve performance","Backup files","Encrypt disks","A"),
("OS & Security","Advanced","Which attack modifies kernel behavior?","Kernel exploit","Phishing","Spoofing","Scanning","A"),
("OS & Security","Advanced","Secure boot ensures?","Trusted OS startup","Faster boot","Disk cleanup","Memory boost","A"),
("OS & Security","Advanced","Which protection prevents stack overflow attacks?","Stack canaries","Routing tables","Compression","Caching","A"),
("OS & Security","Advanced","System call interface connects?","User programs and kernel","Network devices","Applications only","Drivers only","A"),
("OS & Security","Advanced","Which security isolates containers?","Namespaces","Routing","Switching","Hashing","A"),
("OS & Security","Advanced","Cgroups manage?","Resource limits","Passwords","Encryption keys","Routing","A"),
("OS & Security","Advanced","Which tool checks system integrity?","Tripwire","Wireshark","Nmap","Hydra","A"),
("OS & Security","Advanced","File integrity monitoring detects?","Unauthorized changes","Network speed","Disk errors","Memory leaks","A"),
("OS & Security","Advanced","Which attack abuses race conditions?","TOCTOU","MITM","DoS","Phishing","A"),
("OS & Security","Advanced","Address space separation prevents?","Process interference","Slow boot","Disk failure","Network errors","A"),
("OS & Security","Advanced","Which mechanism limits program capabilities?","Capabilities","Routing","Encryption","Compression","A"),
("OS & Security","Advanced","Auditd in Linux is used for?","Security auditing","Gaming","Backup","Networking","A"),
("OS & Security","Advanced","Hardening disables?","Unnecessary services","Security logs","Firewall","Kernel","A"),
("OS & Security","Advanced","Which attack injects malicious code into memory?","Code injection","Phishing","Sniffing","Spoofing","A"),
("OS & Security","Advanced","Defense in depth means?","Multiple security layers","Single firewall","Password reuse","Network reset","A"),
("Cybersecurity Concepts","Beginner","What is cybersecurity?","Protection of systems and data","Internet browsing","Programming","Gaming","A"),
("Cybersecurity Concepts","Beginner","CIA triad stands for?","Confidentiality Integrity Availability","Control Internet Access","Cyber Intelligence Agency","Central Information Access","A"),
("Cybersecurity Concepts","Beginner","Confidentiality ensures?","Data secrecy","Data speed","Data storage","Data deletion","A"),
("Cybersecurity Concepts","Beginner","Integrity ensures?","Data accuracy","Fast internet","Backup","Compression","A"),
("Cybersecurity Concepts","Beginner","Availability means?","Systems accessible when needed","Data encrypted","Files deleted","Users blocked","A"),
("Cybersecurity Concepts","Beginner","Which attack steals user information using fake sites?","Phishing","DoS","Scanning","Routing","A"),
("Cybersecurity Concepts","Beginner","Malware refers to?","Malicious software","Backup file","Driver","Application","A"),
("Cybersecurity Concepts","Beginner","Firewall mainly protects?","Network access","CPU","Monitor","Keyboard","A"),
("Cybersecurity Concepts","Beginner","Antivirus detects?","Malicious programs","Hardware faults","Network cables","Drivers","A"),
("Cybersecurity Concepts","Beginner","Strong authentication uses?","Multiple factors","Password only","Username only","IP address","A"),
("Cybersecurity Concepts","Beginner","Password reuse is?","Security risk","Best practice","Encryption","Backup method","A"),
("Cybersecurity Concepts","Beginner","Social engineering targets?","Human behavior","Hardware","Servers","Switches","A"),
("Cybersecurity Concepts","Beginner","Which attack floods servers?","DoS","Hashing","Encryption","Routing","A"),
("Cybersecurity Concepts","Beginner","VPN provides?","Secure connection","Faster CPU","Extra storage","Graphics boost","A"),
("Cybersecurity Concepts","Beginner","Security policy defines?","Rules for protection","Internet speed","File size","Software updates","A"),
("Cybersecurity Concepts","Beginner","Patch management fixes?","Vulnerabilities","Hardware","Network cables","Displays","A"),
("Cybersecurity Concepts","Beginner","Backup helps recover from?","Data loss","Encryption","Routing","Compression","A"),
("Cybersecurity Concepts","Beginner","Cyber attack means?","Attempt to damage systems","System update","Backup","Optimization","A"),
("Cybersecurity Concepts","Beginner","Authentication verifies?","User identity","File size","Network speed","Disk usage","A"),
("Cybersecurity Concepts","Beginner","Authorization controls?","Access permissions","Internet speed","Encryption","Compression","A"),
("Cybersecurity Concepts","Intermediate","Risk in cybersecurity equals?","Threat × Vulnerability","Speed × Data","Users × Devices","Firewall × Router","A"),
("Cybersecurity Concepts","Intermediate","Threat means?","Potential danger","System update","Backup file","Encryption key","A"),
("Cybersecurity Concepts","Intermediate","Vulnerability is?","Security weakness","Firewall rule","Strong password","Patch update","A"),
("Cybersecurity Concepts","Intermediate","IDS stands for?","Intrusion Detection System","Internet Data Service","Internal Defense Setup","Integrated Device Security","A"),
("Cybersecurity Concepts","Intermediate","IPS primarily does?","Prevents attacks automatically","Only monitors","Stores data","Encrypts files","A"),
("Cybersecurity Concepts","Intermediate","Which attack listens to traffic secretly?","Sniffing","Routing","Switching","Hashing","A"),
("Cybersecurity Concepts","Intermediate","MITM attack stands for?","Man in the Middle","Machine Internet Mode","Main Transfer Method","Memory Interface Module","A"),
("Cybersecurity Concepts","Intermediate","Security awareness reduces?","Human errors","CPU usage","Disk space","Network speed","A"),
("Cybersecurity Concepts","Intermediate","Least privilege principle means?","Minimum access rights","Full access","Guest access","No access","A"),
("Cybersecurity Concepts","Intermediate","Zero Trust model assumes?","No implicit trust","All users trusted","Only admins trusted","Internal safe network","A"),
("Cybersecurity Concepts","Intermediate","Security auditing checks?","Compliance and activities","Internet speed","Graphics","Drivers","A"),
("Cybersecurity Concepts","Intermediate","Incident response handles?","Security breaches","Software updates","File backup","System installation","A"),
("Cybersecurity Concepts","Intermediate","Threat modeling identifies?","Potential risks","Passwords","Hardware errors","Network cables","A"),
("Cybersecurity Concepts","Intermediate","Encryption ensures?","Confidentiality","Availability","Speed","Compression","A"),
("Cybersecurity Concepts","Intermediate","Security control types include?","Preventive Detective Corrective","CPU GPU RAM","Input Output Storage","Hardware Software Network","A"),
("Cybersecurity Concepts","Intermediate","Penetration testing simulates?","Real attacks","System backup","Updates","Maintenance","A"),
("Cybersecurity Concepts","Intermediate","Vulnerability scanning finds?","Security weaknesses","Passwords","Logs","Images","A"),
("Cybersecurity Concepts","Intermediate","Access control lists define?","Permissions","Speed","Encryption","Routing","A"),
("Cybersecurity Concepts","Intermediate","Security baseline means?","Minimum protection standard","Maximum speed","Network layout","Hardware type","A"),
("Cybersecurity Concepts","Intermediate","Security monitoring detects?","Suspicious activities","Hardware failure","File size","Compression errors","A"),
("Cybersecurity Concepts","Advanced","Defense in depth strategy means?","Multiple security layers","Single firewall","Strong password only","Fast network","A"),
("Cybersecurity Concepts","Advanced","Zero-day vulnerability is?","Unknown unpatched flaw","Old bug","Firewall error","Login failure","A"),
("Cybersecurity Concepts","Advanced","Threat intelligence provides?","Attack insights","Faster internet","Backup storage","Compression","A"),
("Cybersecurity Concepts","Advanced","Security Information and Event Management (SIEM) does?","Log analysis and monitoring","Encryption","Routing","Compression","A"),
("Cybersecurity Concepts","Advanced","False positive means?","Normal activity flagged as attack","Attack missed","Correct detection","Patch update","A"),
("Cybersecurity Concepts","Advanced","False negative means?","Attack not detected","Correct alert","System update","Network failure","A"),
("Cybersecurity Concepts","Advanced","Red team focuses on?","Offensive testing","Defense monitoring","Backup","Updates","A"),
("Cybersecurity Concepts","Advanced","Blue team focuses on?","Defense and monitoring","Attacking","Scanning only","Routing","A"),
("Cybersecurity Concepts","Advanced","Purple team combines?","Red and Blue teams","Network devices","Encryption keys","Protocols","A"),
("Cybersecurity Concepts","Advanced","Attack surface refers to?","All possible entry points","Firewall rules","Passwords","Logs","A"),
("Cybersecurity Concepts","Advanced","Security orchestration automates?","Incident response","Hardware repair","Compression","Gaming","A"),
("Cybersecurity Concepts","Advanced","Data exfiltration means?","Unauthorized data transfer","Backup process","Encryption","Routing","A"),
("Cybersecurity Concepts","Advanced","Insider threat originates from?","Authorized users","External hackers","Routers","Servers only","A"),
("Cybersecurity Concepts","Advanced","Kill chain describes?","Stages of cyber attack","Network routing","Encryption steps","Backup process","A"),
("Cybersecurity Concepts","Advanced","Honeypot is used to?","Trap attackers","Encrypt data","Speed network","Store backups","A"),
("Cybersecurity Concepts","Advanced","Security posture describes?","Overall security strength","Internet speed","Hardware type","Disk usage","A"),
("Cybersecurity Concepts","Advanced","Risk mitigation reduces?","Impact or likelihood","Storage","Bandwidth","CPU load","A"),
("Cybersecurity Concepts","Advanced","Compliance ensures?","Following regulations","Faster systems","Encryption only","Routing","A"),
("Cybersecurity Concepts","Advanced","Incident containment aims to?","Limit damage","Delete logs","Restart system","Increase traffic","A"),
("Cybersecurity Concepts","Advanced","Cyber resilience focuses on?","Recovery and continuity","Attack creation","Data deletion","Compression","A")
]

cur.executemany("""
INSERT INTO questions
(topic, level, question, option_a, option_b, option_c, option_d, answer)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", questions)

conn.commit()
conn.close()

print("✅ Database created with 20 questions!")
