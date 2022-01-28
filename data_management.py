def save(fname, key, value):
    ret = {}
    for line in open(fname, "rt"):
        k, v = line.strip().split("=", 1)
        ret[k] = eval(v)
    f = open(fname, "wt")
    #if data.items():
    f.write("%s=%s\n" % (key, repr(value)))
    for old_k, old_v in ret.items():
        if not old_k == key:
            f.write("%s=%s\n" % (old_k, repr(old_v)))
    #else:
        #for k, v in data.items():
            #f.write("%s=%s\n" % (k, repr(v)))

    f.close()


def load(fname):
    ret = {}
    for line in open(fname, "rt"):
        k, v = line.strip().split("=", 1)
        ret[k] = eval(v)
    return ret