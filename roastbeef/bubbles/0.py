import abjad
from calliope import bubbles, tools, machines


class BaseLine0(bubbles.Line):
    # metrical_durations=ID1({
    #     1:((3,4),),
    #     },
    #     limit = 12
    #     )
    pass

# class Violin1(BaseLine0, bubbles.Arrange):
class Cello(BaseLine0):
    music = bubbles.Line(""" d'2 """)

class Piano2(BaseLine0):
    music = bubbles.Line(""" d'2 """)

class Piano1(BaseLine0):
    music = bubbles.Line(""" d'2 """)


# -------------------------------

tools.illustrate_me( )

