"""Directory-tree helpers for the chapter 3 figures (archetype 3)."""
from matplotlib.textpath import TextPath
import look

MONO = 7.0
ITAL = 7.0


def tw(s, mono=False, italic=False, size=7.0):
    """Width of a string in points."""
    return TextPath((0, 0), s, size=size,
                    prop=look.fontprops(mono, italic, size=size)).get_extents().width


def row(c, x, y, name, note=None, right=316, box=0, dashed=False, pad=2.2):
    """Draw one name (mono) at (x, y centre) with an optional right-aligned
    italic annotation on a leader ending in a dot at the name's end.
    Returns the name's right edge."""
    w = tw(name, mono=True, size=MONO)
    if box or dashed:
        x0, x1 = x - pad, x + w + pad
        y0, y1 = y - 4.8, y + 4.8
        if box:
            c.box(x0, y0, x1 - x0, y1 - y0, kind="plain", fill=box)
        else:
            for a, b, d, e in ((x0, y0, x1, y0), (x1, y0, x1, y1),
                               (x1, y1, x0, y1), (x0, y1, x0, y0)):
                c.rule(a, b, d, e, dashed=True)
        end = x1
    else:
        end = x + w
    c.text(x, y, name, mono=True, size=MONO, align="left")
    if note:
        nw = tw(note, italic=True, size=ITAL)
        c.text(right, y, note, italic=True, size=ITAL, align="right")
        c.leader(right - nw - 4, y, end + 5, y)
    return end
