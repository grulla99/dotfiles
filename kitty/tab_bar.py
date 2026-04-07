"""Cyberpunk neon tab bar — minimal, sharp, glowing."""

from kitty.fast_data_types import Screen
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    TabBarData,
    as_rgb,
    draw_title,
)

# ── Neon palette ──────────────────────────────────────
NEON = [
    "#00F0FF",  # Cyan
    "#FF2E97",  # Hot pink
    "#BD00FF",  # Electric purple
    "#39FF14",  # Neon green
    "#FFE500",  # Cyber yellow
    "#FF6B35",  # Neon orange
    "#00FF9F",  # Mint
    "#FF44CC",  # Magenta
    "#4D9FFF",  # Electric blue
    "#FF3333",  # Neon red
]

VOID = "#1B2C3D"         # Match terminal background
DIM_TEXT = "#4A5A6D"     # Ghost text for inactive
ACTIVE_FG = "#E8E8F0"   # Bright white-blue


def _hex(h: str) -> int:
    r, g, b = int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)
    return as_rgb((r << 16) | (g << 8) | b)


def _mix(h: str, target: str, t: float) -> str:
    """Lerp between two hex colors."""
    r1, g1, b1 = int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)
    r2, g2, b2 = int(target[1:3], 16), int(target[3:5], 16), int(target[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02X}{g:02X}{b:02X}"


# Pre-compute
_void = _hex(VOID)
_dim = _hex(DIM_TEXT)
_bright = _hex(ACTIVE_FG)
_neon = [_hex(c) for c in NEON]
# Subtle glow bg = neon mixed 88% toward void
_glow_bg = [_hex(_mix(c, VOID, 0.88)) for c in NEON]
# Inactive neon = neon mixed 75% toward void
_neon_dim = [_hex(_mix(c, VOID, 0.75)) for c in NEON]


def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_tab_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:
    i = (index - 1) % len(NEON)

    if tab.is_active:
        # ▎neon accent bar
        screen.cursor.fg = _neon[i]
        screen.cursor.bg = _glow_bg[i]
        screen.draw("▎")

        # tab number in neon
        screen.cursor.fg = _neon[i]
        screen.cursor.bg = _glow_bg[i]
        screen.draw(f"{index}")

        # separator dot
        screen.cursor.fg = _hex(_mix(NEON[i], VOID, 0.5))
        screen.cursor.bg = _glow_bg[i]
        screen.draw(":")

        # title in bright white
        screen.cursor.fg = _bright
        screen.cursor.bg = _glow_bg[i]
        draw_title(draw_data, screen, tab, index, max_title_length=max_tab_length - 6)
        screen.cursor.fg = _neon[i]
        screen.cursor.bg = _glow_bg[i]
        screen.draw(" ")

        # right edge fade
        screen.cursor.fg = _glow_bg[i]
        screen.cursor.bg = _void
        screen.draw("▌")
    else:
        # inactive: visible but subdued
        screen.cursor.fg = _void
        screen.cursor.bg = _void
        screen.draw(" ")

        # number in dimmed neon
        screen.cursor.fg = _neon_dim[i]
        screen.cursor.bg = _void
        screen.draw(f"{index}")

        screen.cursor.fg = _hex(_mix(NEON[i], VOID, 0.6))
        screen.cursor.bg = _void
        screen.draw(":")

        # title in neon (dimmed 50% toward bg)
        screen.cursor.fg = _hex(_mix(NEON[i], VOID, 0.5))
        screen.cursor.bg = _void
        draw_title(draw_data, screen, tab, index, max_title_length=max_tab_length - 6)
        screen.cursor.fg = _void
        screen.cursor.bg = _void
        screen.draw("  ")

    # gap between tabs
    screen.cursor.fg = _void
    screen.cursor.bg = _void
    screen.draw(" ")

    return screen.cursor.x
