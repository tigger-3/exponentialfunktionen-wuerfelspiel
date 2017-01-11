def combine(colormatrix):
    i = 0
    l = colormatrix.__len__()
    colall = [0, 0, 0]
    while i < l:
        active = list(colormatrix[i])
        colall[0] = colall[0] + active[0]
        colall[1] = colall[1] + active[1]
        colall[2] = colall[2] + active[2]
        i += 1
    i = 0
    out = [0, 0, 0]
    while i < 3:
        helpvar = colall[i]
        helpvar = int(helpvar / l)
        out[i] = helpvar
        i += 1
    return tuple(out)
