from os import system, listdir

system("rm txt/*")
system("rm fb2/*")

for fname in listdir('zip'):
    system("unzip zip/%s -d fb2" % fname)

for fname in listdir('fb2'):
    system("unoconv -f txt fb2/%s" % fname)
    new_fname = fname[:-3] + "txt"
    system("mv fb2/%s txt/%s" % (new_fname, new_fname))

system("cat txt/* >lenin.txt")
