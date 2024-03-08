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
end
