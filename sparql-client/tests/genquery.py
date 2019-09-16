import urllib2

from urllib.parse import urlencode

statement = open("code.rq").read()
query = { 'query': statement,
 'format':'xml' }

qs = urlencode(query)
print(qs)
url = "http://dbpedia.org/sparql?" + urlencode(query)

opener = urllib2.build_opener(urllib2.HTTPHandler)
urllib2.install_opener(opener)
req = urllib2.Request(url)
#req.add_header("Accept", "application/xml")

try:
    conn = urllib2.urlopen(req, timeout=10)
except Exception:
    conn = None

if not conn:
    raise IOError, "Failure in open"

data = conn.read()
conn.close()
print(data)
