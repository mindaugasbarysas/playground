# -- autopull repos



lines = [line.strip() for line in open('%s/sources/.repos' % (os.path.dirname(os.path.realpath(__file__))))]

for line in lines:
    os.system("cd sources; mkdir %s && cd %s; git init; git remote add –f origin %s; git config core.sparsecheckout true; echo "Resources/" >> .git/info/sparse-checkout; git pull;" % (line.split("/")[-1], line.split("/")[-1], line)

