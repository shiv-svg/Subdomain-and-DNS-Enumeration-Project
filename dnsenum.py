import dns.resolver
import sys

record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'SOA', 'TXT', 'PTR', 'SRV', 'SPF', 'CAA']
try:
    domain = sys.argv[1]
except IndexError:
    print('Syntax Error - python dnsenum.py <domain>')
    quit()
for records in record_types: 
    try:
        answer = dns.resolver.resolve(domain, records)
        print(f'\n{records} Records')
        print('-' * 30)
        for server in answer:
            print(server.to_text())
    except dns.resolver.NoAnswer:
    #    print('No record found.')
        pass
    except dns.resolver.NXDOMAIN:
        print(f'{domain} does not exist.')
    except KeyboardInterrupt:
        quit()