import fontforge

font = fontforge.open("DevrisDunggeunmo.ttf")
s = font.selection.all()
# Normal integer tuple doesn't work for fontforge. IDK why.
# https://github.com/fontforge/fontforge/issues/5029
# font.bitmapSizes = ((16,), (32,), (48,))
# regenBitmap is even weirder. Documentation said it takes TUPLE but you can only toss single integer in it.
# font.regenBitmaps((16,))
# font.regenBitmaps((32,))
# font.regenBitmaps((48,))

# There are issue with 32px and 48px bitmap glyph.
# Until finding why, only 16px will be included and shipped.
# See https://github.com/ruby3141/DevrisDunggeunmo/issues/8 for detail.
font.bitmapSizes = ((16,),)
font.regenBitmaps((16,))

font.appendSFNTName("Korean", "SubFamily", "보통")
font.appendSFNTName("English (US)", "SubFamily", "Regular")
font.appendSFNTName("Korean", "Fullname", "Devris둥근모")
font.appendSFNTName("English (US)", "Fullname", "DevrisDunggeunmo")
font.generate("DevrisDunggeunmo.ttf", bitmap_type="ttf")

# Bold
font.macstyle = 1
font.os2_stylemap = 32
font.appendSFNTName("Korean", "SubFamily", "가짜볼드")
font.appendSFNTName("English (US)", "SubFamily", "FakeBold")
font.appendSFNTName("Korean", "Fullname", "Devris둥근모-가짜볼드")
font.appendSFNTName("English (US)", "Fullname", "DevrisDunggeunmo-FakeBold")
font.generate("DevrisDunggeunmo-Bold.ttf", bitmap_type="ttf")

# Italic
font.macstyle = 2
font.os2_stylemap = 1
font.appendSFNTName("Korean", "SubFamily", "가짜이탤릭")
font.appendSFNTName("English (US)", "SubFamily", "FakeItalic")
font.appendSFNTName("Korean", "Fullname", "Devris둥근모-가짜이탤릭")
font.appendSFNTName("English (US)", "Fullname", "DevrisDunggeunmo-FakeItalic")
font.generate("DevrisDunggeunmo-Italic.ttf", bitmap_type="ttf")

# Bold Italic
font.macstyle = 3
font.os2_stylemap = 33
font.appendSFNTName("Korean", "SubFamily", "가짜볼드이탤릭")
font.appendSFNTName("English (US)", "SubFamily", "FakeBoldItalic")
font.appendSFNTName("Korean", "Fullname", "Devris둥근모-가짜볼드이탤릭")
font.appendSFNTName("English (US)", "Fullname", "DevrisDunggeunmo-FakeBoldItalic")
font.generate("DevrisDunggeunmo-BoldItalic.ttf", bitmap_type="ttf")

# Back to normal
font.revert()

variations = [fontforge.open(f"DevrisDunggeunmo-{variation}.ttf") for variation in ["Bold", "Italic", "BoldItalic"]]
# bitmap_type is not specified in official documentation, but it is there. Seriously?
# https://github.com/fontforge/fontforge/blob/9af60edefc61d1f9244601802067c33fd221db69/fontforge/python.c#L17382
font.generateTtc("DevrisDunggeunmo.ttc", variations, bitmap_type="ttf", ttcflags=("merge"), layer=font.activeLayer)

font.generate("DevrisDunggeunmo.woff", bitmap_type="ttf")
font.generate("DevrisDunggeunmo.woff2", bitmap_type="ttf")
