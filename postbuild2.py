from fontTools import ttLib

f = ttLib.TTFont("DevrisDunggeunmo.ttf")

# Fontforge automatically recalculate xAvgCharWidth value (it's totally normal),
# and it messes up horizontal advance (it isn't normal and not Fontforge's fault).
# To fix this, xAvgCharWidth need to be manually set to desired value.
# https://github.com/ruby3141/DevrisDunggeunmo/issues/8
f["OS/2"].xAvgCharWidth = 512

f.flavor = 'woff'
f.save("DevrisDunggeunmo.woff")

f.flavor = 'woff2'
f.save("DevrisDunggeunmo.woff2")

f.flavor = None
f.save("DevrisDunggeunmo.ttf")

# Generate Fake variations
# head macStyle: bit 0 for bold, bit 1 for italic.
# OS/2 fsSelection: bit 5 for bold, bit 0 for italic.

# For Mac name table entry Fonttools seems to add them.
# It's just a copy of Windows English(US) entry.

# Italic
f["head"].macStyle = 0b0000_0000_0000_0010
f["OS/2"].fsSelection = 0b0000_0000_0000_0001
# Windows - English (US)
[f["name"].setName(value, nameID, 3, 1, 0x409) for (value, nameID) in [
    ("Italic", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeItalic : 2024", 3), # Font identifier
    ("DevrisDunggeunmo FakeItalic", 4), # Font full name
    ("DevrisDunggeunmo-FakeItalic", 6), # PostScript name
]]
# Windows - Korean
[f["name"].setName(value, nameID, 3, 1, 0x412) for (value, nameID) in [
    ("기울임꼴", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeItalic : 2024", 3), # Font identifier
    ("Devris둥근모 가짜기울임꼴", 4), # Font full name
    ("DevrisDunggeunmo-FakeItalic", 6), # PostScript name
]]
# Macintosh - English
[f["name"].setName(value, nameID, 1, 0, 0x0) for (value, nameID) in [
    ("Italic", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeItalic : 2024", 3), # Font identifier
    ("DevrisDunggeunmo FakeItalic", 4), # Font full name
    ("DevrisDunggeunmo-FakeItalic", 6), # PostScript name
]]
f.save("DevrisDunggeunmo-Italic.ttf")

# Common for Bold and Bold Italic
f["OS/2"].panose.bWeight = 8 # Bold
f["OS/2"].usWeightClass = 700 # Bold

# Bold
f["head"].macStyle = 0b0000_0000_0000_0001
f["OS/2"].fsSelection = 0b0000_0000_0010_0000
# Windows - English (US)
[f["name"].setName(value, nameID, 3, 1, 0x409) for (value, nameID) in [
    ("Bold", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeBold : 2024", 3), # Font identifier
    ("DevrisDunggeunmo FakeBold", 4), # Font full name
    ("DevrisDunggeunmo-FakeBold", 6), # PostScript name
]]
# Windows - Korean
[f["name"].setName(value, nameID, 3, 1, 0x412) for (value, nameID) in [
    ("굵게", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeBold : 2024", 3), # Font identifier
    ("Devris둥근모 가짜굵게", 4), # Font full name
    ("DevrisDunggeunmo-FakeBold", 6), # PostScript name
]]
# Macintosh - English
[f["name"].setName(value, nameID, 1, 0, 0x0) for (value, nameID) in [
    ("Bold", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeBold : 2024", 3), # Font identifier
    ("DevrisDunggeunmo FakeBold", 4), # Font full name
    ("DevrisDunggeunmo-FakeBold", 6), # PostScript name
]]
f.save("DevrisDunggeunmo-Bold.ttf")

# Bold Italic
f["head"].macStyle = 0b0000_0000_0000_0011
f["OS/2"].fsSelection = 0b0000_0000_0010_0001
# Windows - English (US)
[f["name"].setName(value, nameID, 3, 1, 0x409) for (value, nameID) in [
    ("Bold Italic", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeBoldItalic : 2024", 3), # Font identifier
    ("DevrisDunggeunmo FakeBoldItalic", 4), # Font full name
    ("DevrisDunggeunmo-FakeBoldItalic", 6), # PostScript name
]]
# Windows - Korean
[f["name"].setName(value, nameID, 3, 1, 0x412) for (value, nameID) in [
    ("굵게 기울임", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeBoldItalic : 2024", 3), # Font identifier
    ("Devris둥근모 가짜굵게기울임", 4), # Font full name
    ("DevrisDunggeunmo-FakeBoldItalic", 6), # PostScript name
]]
# Macintosh - English
[f["name"].setName(value, nameID, 1, 0, 0x0) for (value, nameID) in [
    ("Bold Italic", 2), # Font Subfamily name
    ("CDnX : DevrisDunggeunmo FakeBoldItalic : 2024", 3), # Font identifier
    ("DevrisDunggeunmo FakeBoldItalic", 4), # Font full name
    ("DevrisDunggeunmo-FakeBoldItalic", 6), # PostScript name
]]
f.save("DevrisDunggeunmo-BoldItalic.ttf")

f.close()

# Build TTC file
ttc = ttLib.TTCollection()
ttc.fonts = [ttLib.TTFont(f"DevrisDunggeunmo{variation}.ttf") for variation in ["", "-Bold", "-Italic", "-BoldItalic"]]
ttc.save("DevrisDunggeunmo.ttc")
