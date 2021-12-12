import numpy as np
def bin_media(s):
    media = np.mean(s)
    serie_bin_media = []
    for i in s:
        if i > media:
            serie_bin_media.append(1)
        else:
            serie_bin_media.append(0)             
    return serie_bin_media,media
