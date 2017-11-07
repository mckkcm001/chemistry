import pickle

k = 2
n = k**5
x = []
y = []

def pickleLoader(pklFile):
    try:
        while True:
            yield pickle.load(pklFile)
    except EOFError:
        pass

with open('euler411set' + str(k) + '.pkl', "rb") as f:
    for i in pickleLoader(f):
        if i[0] not in x:
            x.append(i[0])
        else:
            x.append(len(x)-x.index(i[0]))
            break   
  



print x, len(x)

    
print y, len(y)