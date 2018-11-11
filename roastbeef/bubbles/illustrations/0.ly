% 2017-03-30 00:05

\version "2.19.54"
\language "english"

\header {}

\layout {}

\paper {}

\score {
    \new Score <<
        \new Staff {
            \set Staff.instrumentName = \markup { BaseLine0 }
            \set Staff.shortInstrumentName = \markup { BaseLine0 }
            {
            }
        }
        \new Staff {
            \set Staff.instrumentName = \markup { Cello }
            \set Staff.shortInstrumentName = \markup { Cello }
            {
                \accidentalStyle modern-cautionary
                d'2
            }
        }
        \new Staff {
            \set Staff.instrumentName = \markup { Piano2 }
            \set Staff.shortInstrumentName = \markup { Piano2 }
            {
                \accidentalStyle modern-cautionary
                d'2
            }
        }
        \new Staff {
            \set Staff.instrumentName = \markup { Piano1 }
            \set Staff.shortInstrumentName = \markup { Piano1 }
            {
                \accidentalStyle modern-cautionary
                d'2
            }
        }
    >>
}