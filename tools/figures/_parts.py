"""Small shared drawing helpers for the chapter 1 and 2 figures."""
import look


def folder(c, x, y, w, h, label, mono=True):
    """A folder icon (tab on a rectangle) with its label below."""
    t = 6.0
    c._poly([(x, y), (x + w * 0.4, y), (x + w * 0.4 + 3, y + 3.5),
             (x + w, y + 3.5), (x + w, y + h), (x, y + h)], 0)
    c.text(x + w / 2, y + h + 3, label, mono=mono, size=7, align="center",
           va="top")


def file_icon(c, cx, cy, label, w=20, h=16, mono=True):
    """A dog-eared file icon centred on (cx, cy), label below."""
    return c.box(cx - w / 2, cy - h / 2, w, h, label, kind="file",
                 label_below=True, mono=mono, size=7)
