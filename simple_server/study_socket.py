import socket
import urlparse


#print 'HOST_NAME: {}'.format(socket.gethostname())

'''
for host in ['homer', 'www', 'www.python.org', 'nosuchname']:
    try:
        print '%15s : %s' % (host, socket.gethostbyname(host))
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)
'''

'''
host = 'ltstxdc4.lts.local'
print '%15s : %s' % (host, socket.gethostbyname(host))
'''

'''
for host in ['homer', 'www', 'www.python.org', 'nosuchname']:
    print host
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print '  Hostname:', hostname
        print '  Aliases :', aliases
        print ' Addresses:', addresses
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)
    print
'''

# Use getfqdn() to convert a partial name to a fully qualified domain name.
'''
for host in ['homer', 'www']:
    print '%6s : %s' % (host, socket.getfqdn(host))
'''

'''
hostname, aliases, addresses = socket.gethostbyaddr('192.168.109.21')
print 'Hostname :', hostname
print 'Aliases  :', aliases
print 'Addresses:', addresses
'''

'''
urls = [
    'http://www.python.org',
    'https://www.mybank.com',
    'ftp://prep.ai.mit.edu',
    'gopher://gopher.micro.umn.edu',
    'smtp://mail.example.com',
    'imap://mail.example.com',
    'imaps://mail.example.com',
    'pop3://pop.example.com',
    'pop3s://pop.example.com',
]
for url in urls:
    parsed_url = urlparse(url)
    port = socket.getservbyname(parsed_url.scheme)
    print '%6s : %s' % (parsed_url.scheme, port)
'''

'''
for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    # print socket.getservbyport(port)
    print urlparse.urlunparse((socket.getservbyport(port), 'example.com', '/', '', '', ''))
'''

def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    attr_map = [(getattr(socket, n), n) for n in dir(socket) if n.startswith(prefix)]
    return dict(attr_map)


'''
protocols = get_constants('IPPROTO_')
for name in ['icmp', 'udp', 'tcp']:
    proto_num = socket.getprotobyname(name)
    const_name = protocols[proto_num]
    print '%4s -> %2d (socket.%-12s = %2d)' % \
        (name, proto_num, const_name, getattr(socket, const_name))
'''

'''
families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

print socket.getaddrinfo('www.python.org', 'http')
for response in socket.getaddrinfo('www.python.org', 'http'):

    # Unpack the response tuple
    family, socktype, proto, canonname, sockaddr = response

    print 'Family        :', families[family]
    print 'Type          :', types[socktype]
    print 'Protocol      :', protocols[proto]
    print 'Canonical name:', canonname
    print 'Socket address:', sockaddr
    print
'''


import binascii
import struct
import sys

string_address = sys.argv[1]

packed = socket.inet_aton(string_address)

print 'Original:', string_address
print 'Packed  :', binascii.hexlify(packed)
print 'Unpacked:', socket.inet_ntoa(packed)
























