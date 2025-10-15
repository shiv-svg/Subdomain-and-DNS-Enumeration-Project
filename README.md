🌐 DNS Reconnaissance Toolset

This repository contains two Python scripts designed for quick and effective DNS enumeration and discovery. These tools are valuable for security testing, network analysis, and understanding a domain's public infrastructure.

⚠️ Disclaimer

These tools are intended for educational and authorized security testing purposes only. Always ensure you have explicit permission from the domain owner before running any network or DNS scanning tools against their property.

🛠️ Prerequisites

Both scripts rely on the dnspython library for performing DNS lookups.

Install Python 3 (if you don't have it already).

Install the required library:

pip install dnspython

1. DNS Record Enumeration (dnsenum.py)
   
This script queries a target domain for a comprehensive list of standard DNS records to gather information about its mail servers, name servers, IP addresses, and security configurations.

Features

Queries Standard Records: Checks for A, AAAA, CNAME, MX, NS, SOA, TXT, PTR, SRV, SPF, and CAA records.

Clean Output: Only displays records that are found, omitting records with "No Answer" errors.

Usage

The script requires the domain name as a command-line argument.

python .\dnsenum.py <domain>

Example:

python .\dnsenum.py example.com

Example Output Snippets
A Records
------------------------------
93.184.216.34

MX Records
------------------------------
50 mail.example.com.

NS Records
------------------------------
a.iana-servers.net.

b.iana-servers.net.

2. Subdomain Brute-Forcing (subdom.py)
   
This script performs a dictionary attack (brute-force) against a target domain using a massive built-in wordlist to find common subdomains.

Features

Large Wordlist: Contains over 300 common subdomain prefixes (e.g., www, mail, dev, ftp, api, admin).

A-Record Check: Confirms the existence of a subdomain by resolving its A record (IPv4 address).

Simple Status: Prints out the full subdomain name if a valid entry is found.

Usage

The script requires the domain name as a command-line argument.

python .\subdom.py <domain>

Example:

python .\subdom.py targetdomain.com

Example Output Snippet

[www.targetdomain.com]

(https://www.targetdomain.com) valid

mail.targetdomain.com valid

webmail.targetdomain.com valid

api.targetdomain.com valid
