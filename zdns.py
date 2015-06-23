__author__ = 'secbrain'
import dns.resolver
import sys

if len(sys.argv) != 4:
    sys.exit("USAGE: $ python " + sys.argv[0]+" words.txt output.txt domain.com")

rfile = sys.argv[1]
wfile = sys.argv[2]
domain = sys.argv[3]

rfileres = open(rfile, 'r')
wfileres = open(wfile, 'w')

words = rfileres.read().splitlines()
rfileres.close()

for cname in words:
    try:
        answers = dns.resolver.query(cname+"."+domain, 'CNAME')
    except BaseException:
        continue
    subdomain = str(answers.qname)[:-1]
    print "Found:", subdomain
    wfileres.writelines(subdomain+"\n")

wfileres.close()