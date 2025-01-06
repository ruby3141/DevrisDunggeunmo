import fontforge

font = fontforge.open("DevrisDunggeunmo.ttf")
s = font.selection.all()
# Normal integer tuple doesn't work for fontforge. IDK why.
# https://github.com/fontforge/fontforge/issues/5029
font.bitmapSizes = ((16,), (32,), (48,))
# regenBitmap is even weirder. Documentation said it takes TUPLE but you can only toss single integer in it.
font.regenBitmaps((16,))
font.regenBitmaps((32,))
font.regenBitmaps((48,))
font.generate("DevrisDunggeunmo.ttf", bitmap_type="ttf")
