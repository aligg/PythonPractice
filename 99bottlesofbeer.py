
bottlenumber= 99
bottlenumbernext=98
while bottlenumber >= 1:
    print("%d bottles of beer on the wall, %d bottles of beer. Take one down, pass it around, %d bottles of beer on the wall" % (bottlenumber, bottlenumber, bottlenumbernext))
    bottlenumber = bottlenumber -1
    bottlenumbernext = bottlenumbernext -1
