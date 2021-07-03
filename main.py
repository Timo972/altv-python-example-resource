import alt
import sys

import events.player

alt.log("Hello World!")

alt.log(sys.path)

def explosion(source, expType, pos, fx, target):
    alt.log("Explosion of type {0} caused by player {1} at position {2}".format(expType, source, pos))

alt.on("explosion", explosion)