import os

import pygame

import colorcombiner

if not os.path.exists("data"):
    os.mkdir("data")


# if not os.path.exists("data/intern"):
#    os.mkdir("data/intern")

def get_codec():
    colcodec = dict()
    colcodec[str(1)] = (0, 0, 255)
    colcodec[str(2)] = (255, 0, 255)
    colcodec[str(5)] = (255, 255, 0)
    colcodec[str(6)] = (0, 255, 0)
    colcodec[str(4)] = (255, 127, 0)
    colcodec[str(3)] = (255, 0, 0)
    colcodec[str(7)] = (255, 255, 255)
    colcodec[str(True)] = (127, 127, 127)
    colcodec[str(False)] = (0, 0, 0)
    return colcodec


def setup_folder(num_o_dices):
    i = 1
    while os.path.exists("data/" + str(num_o_dices) + " dices - try " + str(i)):
        i += 1
    folder = "data/" + str(num_o_dices) + " dices - try " + str(i)
    os.mkdir(folder)

    os.mkdir(folder + "/Legende Farbe")
    for tvar in range(1, 8):
        j = color(str(tvar))
        s = pygame.Surface((100, 100))
        s.fill(j)
        if tvar <= 6:
            tvar2 = str(tvar)
        else:
            tvar2 = "frühere 6"
        save(s, folder + "/Legende Farbe", tvar2)

    os.mkdir(folder + "/Legende Grau")
    s = pygame.Surface((100, 100))
    s.fill(color(False))
    save(s, folder + "/Legende Grau", "keine 6")
    s = pygame.Surface((100, 100))
    s.fill(color(True))
    save(s, folder + "/Legende Grau", "neue 6")
    s = pygame.Surface((100, 100))
    s.fill(color(7))
    save(s, folder + "/Legende Grau", "frühere 6")
    return folder


def save(bild, folder, name):
    path = folder + "/" + name + ".png"
    pygame.image.save(bild, path)


def convertmatrix(datain, folder, name, width, height):
    # if width > 1000:
    #    wfactor=width/1000
    #    if type(wfactor)==int:
    #        nwidth=1000
    #    else:
    #        return
    # else:
    #    nwidth=width
    #    wfactor=1

    if height > 1000:
        if height % 1000 == 0:
            hfactor = int(height / 1000)
            nheight = 1000
        else:
            return
    else:
        nheight = height
        hfactor = 1

    surface = pygame.Surface((width, nheight))
    pxlist = pygame.PixelArray(surface)
    i = 0
    while i < width:
        j = 0
        hd = height - datain[i].__len__()
        hd = int(hd % hfactor)
        n = 0
        di = datain[i]
        while j < nheight:
            if i < width:
                if j <= di.__len__() + hd / hfactor:
                    hj = 0
                    cl = []
                    while hj < hfactor:
                        if (di.__len__()) - (n * hfactor + hj) > 0:
                            dbval = (di.__len__()) - (n * hfactor + hj) - 1
                            d = di[dbval]
                            c = color(d)
                            cl.append(c)
                            hj += 1
                        else:
                            c = color(7)
                            cl.append(c)
                            hj += 1
                    c = colorcombiner.combine(cl)
                    pxlist[i, nheight - 1 - j] = c
                    n += 1
                else:
                    pxlist[i, nheight - 1 - j] = color(7)
            else:
                print("error")
            j += 1
        i += 1
    pic = pxlist.make_surface()
    save(pic, folder, name)


colorcodec = get_codec()


def color(data):
    sdata = str(data)
    return colorcodec[sdata]
