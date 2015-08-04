from base import *
import sys

reponame = sys.argv[1]
url = sys.argv[2]
ind = Index(reponame, url)
CACHE = reponame
for n,p in ind.packages.items():
    print n
    p.fetch()
