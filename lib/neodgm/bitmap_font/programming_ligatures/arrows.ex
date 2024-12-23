use PixelFont.GlyphSource

glyph_source NeoDGM.BitmapFont.ProgrammingLigatures.Arrows do
  bmp_glyph "hyphen.arrow" do
    advance 8
    bounds 0..7, 4..5

    data """
    1111111
    """
  end

  bmp_glyph "equal.arrow" do
    advance 8
    bounds 0..7, 3..6

    data """
    1111111
    0000000
    1111111
    """
  end

  bmp_glyph "greater.left1px" do
    advance 8
    bounds 0..6, 0..9

    data """
    110000
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
