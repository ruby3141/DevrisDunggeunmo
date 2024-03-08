use PixelFont.GlyphSource

glyph_source NeoDGM.BitmapFont.ProgrammingLigatures.Markup do
  bmp_glyph "exclam.markupcomment" do
    advance 8
    bounds 1..3, 0..9

    data """
    11
    11
    11
    11
    11
    11
    00
    11
    11
    """
  end

  bmp_glyph "hyphen.markupcomment" do
    advance 8
    bounds -2..7, 4..5

    data """
    111111111
    """
  end

  bmp_glyph "less.markuptag" do
    advance 8
    bounds 1..7, 0..9

    data """
    000011
    000110
    001100
    011000
    110000
    011000
    001100
    000110
    000010
    """
  end

  bmp_glyph "slash.markuptag" do
    advance 8
    bounds -1..7, 0..9

    data """
    00000001
    00000011
    00000110
    00001100
    00011000
    00110000
    01100000
    11000000
    10000000
    """
  end

  bmp_glyph "greater.markuptag" do
    advance 8
    bounds 1..7, 0..9

    data """
    010000
    011000
    001100
    000110
    000011
    000110
    001100
    011000
    110000
    """
  end
end
