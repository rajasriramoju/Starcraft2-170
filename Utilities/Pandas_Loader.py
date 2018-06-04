import sys

def parse_file(x):
  collection = {}
  with open(x) as f:
    for line in f:
      if line in collection:
        collection[line] += 1
      else:
        collection[line] = 1
      nextline = f.next()
  f.close()
  with open('stats.txt', 'w') as f:
    f.write(str(collection))
  f.close()

parse_file(sys.argv[1])
