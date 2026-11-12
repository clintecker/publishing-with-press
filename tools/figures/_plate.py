"""Plate compositing helpers for the chapter 11 figures (alpha master onto grounds)."""
import numpy as np
from PIL import Image
import look

PLATE = look.repo_root() / "assets/woodcuts/the-engravers-bench.png"
G = {0: 255, 10: 230, 20: 204, 40: 153}


def plate_rgba(px):
    im = Image.open(PLATE).convert("RGBA").resize((px, px), Image.LANCZOS)
    a = np.asarray(im).astype(float)
    return a[..., 0] * 0 + a[..., :3].mean(axis=2), a[..., 3] / 255.0


def checker(h, w, sq, a=G[20], b=G[0]):
    yy, xx = np.indices((h, w))
    return np.where(((yy // sq) + (xx // sq)) % 2 == 0, b, a).astype(float)


def flat(h, w, v):
    return np.full((h, w), float(v))


def over(ground, ink, alpha, off=(0, 0)):
    """Composite the plate (ink, alpha) onto the ground at offset (y, x)."""
    out = ground.copy()
    h, w = ink.shape
    y, x = off
    reg = out[y:y + h, x:x + w]
    out[y:y + h, x:x + w] = ink * alpha + reg * (1 - alpha)
    return out


def show(c, arr, x, y, w, h, z=None):
    c.ax.imshow(np.clip(arr, 0, 255).astype(np.uint8), cmap="gray", vmin=0,
                vmax=255, extent=(x, x + w, y + h, y), interpolation="nearest",
                zorder=z or c._zo(), aspect="auto")
    c.ax.set_xlim(0, c.W)
    c.ax.set_ylim(c.H, 0)


def px(pt):
    return int(round(pt * look.PX_PER_PT))


def outline(c, x, y, w, h, lw=look.BOX_PT, edge="black"):
    from matplotlib.patches import Rectangle
    c.ax.add_patch(Rectangle((x, y), w, h, facecolor="none", edgecolor=edge,
                             linewidth=lw, zorder=c._zo()))
