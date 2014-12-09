# -- autopull repos

lines = [line.strip() for line in open('%s/sources/.repos' % (os.path.dirname(os.path.realpath(__file__))))]

for line in lines:
    os.system("cd sources; git clone %s" % (line))
