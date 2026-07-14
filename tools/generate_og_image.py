"""
Regenerates assets/og-image.png (the social-share preview image).

Run this after changing your name/role/school so the OG image matches the
site. Requires Pillow: pip3 install --user Pillow

    python3 tools/generate_og_image.py
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "og-image.png")

# EDIT ME: text shown on the preview card
NAME = "Finn Wilson-Devane"
LINE1 = "Chemical Engineering Student · University of Ottawa"
LINE2 = "Production Eng Summer Student @ Gran Tierra Energy"
INITIALS = "FW"

img = Image.new("RGB", (W, H), "#2f3d52")
draw = ImageDraw.Draw(img)

# --- vertical sky gradient ---
stops = [
    (0.00, (47, 61, 82)),
    (0.42, (107, 122, 154)),
    (0.68, (217, 154, 114)),
    (1.00, (246, 201, 154)),
]


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


for y in range(H):
    t = y / H
    for i in range(len(stops) - 1):
        t0, c0 = stops[i]
        t1, c1 = stops[i + 1]
        if t0 <= t <= t1:
            local_t = (t - t0) / (t1 - t0) if t1 > t0 else 0
            draw.line([(0, y), (W, y)], fill=lerp(c0, c1, local_t))
            break

# --- soft warm glow near horizon ---
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gdraw = ImageDraw.Draw(glow)
gdraw.ellipse([200, 250, 1000, 650], fill=(255, 227, 179, 90))
glow = glow.filter(ImageFilter.GaussianBlur(60))
img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))
draw = ImageDraw.Draw(img)


# --- mountain silhouette layers ---
def ridge(points, color, opacity):
    pts = list(points) + [(W, H), (0, H)]
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(layer).polygon(pts, fill=color + (opacity,))
    img.paste(Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB"), (0, 0))


back = [(0,370),(90,300),(190,335),(290,265),(390,320),(500,275),(610,330),(720,285),(830,335),(940,290),(1050,340),(1200,310)]
mid  = [(0,430),(110,375),(230,410),(350,355),(470,400),(590,365),(710,405),(830,370),(950,410),(1080,380),(1200,415)]
front= [(0,500),(120,450),(250,485),(380,440),(510,480),(630,450),(750,485),(880,450),(1000,490),(1120,455),(1200,480)]

ridge(back, (91, 108, 134), 140)
ridge(mid, (61, 74, 94), 200)
ridge(front, (34, 43, 56), 255)
draw = ImageDraw.Draw(img)

# --- pine cluster ---
pines = [
    [(1000, 505), (1025, 430), (1050, 505)],
    [(1030, 515), (1060, 420), (1090, 515)],
    [(1070, 510), (1100, 435), (1130, 510)],
    [(1110, 520), (1145, 425), (1180, 520)],
]
for p in pines:
    draw.polygon(p, fill=(26, 33, 43))
draw.rectangle([1025, 505, 1031, 530], fill=(26, 33, 43))
draw.rectangle([1100, 510, 1106, 535], fill=(26, 33, 43))

# --- dark overlay gradient so text stays legible ---
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
odraw = ImageDraw.Draw(overlay)
for y in range(H):
    t = y / H
    a = int(20 + (15 - 20) * (t / 0.45)) if t < 0.45 else int(15 + (185 - 15) * ((t - 0.45) / 0.55))
    odraw.line([(0, y), (W, y)], fill=(10, 14, 20, a))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
draw = ImageDraw.Draw(img)

# --- avatar badge ---
draw.ellipse([72, 232, 168, 328], fill=(194, 112, 63))
font_avatar = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 38)
bbox = draw.textbbox((0, 0), INITIALS, font=font_avatar)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text((120 - tw / 2 - bbox[0], 280 - th / 2 - bbox[1]), INITIALS, font=font_avatar, fill="white")

# --- title text ---
font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 54)
font_sub = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 26)

draw.text((200, 225), NAME, font=font_title, fill=(253, 246, 238))
draw.text((200, 300), LINE1, font=font_sub, fill=(240, 228, 216))
draw.text((200, 336), LINE2, font=font_sub, fill=(240, 228, 216))

img.save(OUT_PATH, "PNG")
print(f"saved {img.size} -> {OUT_PATH}")
