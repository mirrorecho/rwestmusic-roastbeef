import abjad
from calliope import bubbles, tools, machines

class BeefScore(bubbles.Score):
        class Piano(bubbles.Piano):
            class Violin1(bubbles.Staff):
                instrument=abjad.instrumenttools.Violin(
                    instrument_name="Violin 1", short_instrument_name="vln.1")
            class Violin2(bubbles.Staff):
                instrument=abjad.instrumenttools.Violin(
                    instrument_name="Violin 2", short_instrument_name="vln.2")

        class Viola(bubbles.Staff):
            instrument=abjad.instrumenttools.Viola(
                instrument_name="Viola", short_instrument_name="vla.")

        class Cello(bubbles.Staff):
            instrument=abjad.instrumenttools.Cello(
                instrument_name="Cello", short_instrument_name="vc.")
            clef="bass"