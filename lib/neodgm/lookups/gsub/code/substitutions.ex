use PixelFont.OTFLayout

lookups NeoDGM.Lookups.GSUB.Code.Substitutions, for: "GSUB" do
  lookup :single_substitution, "Arrow body" do
    substitutions do
      substitute ?-, "hyphen.arrow"
      substitute ?=, "equal.arrow"
    end
  end

  lookup :single_substitution, "Right arrow head" do
    substitutions do
      substitute ?>, "greater.arrow"
    end
  end

  lookup :single_substitution, "Markup comment exclam" do
    substitutions do
      substitute ?!, "exclam.markupcomment"
    end
  end

  lookup :single_substitution, "Markup comment hyphen body" do
    substitutions do
      substitute ?-, "hyphen.markupcomment.body"
    end
  end

  lookup :single_substitution, "Markup comment hyphen tail" do
    substitutions do
      substitute ?-, "hyphen.markupcomment.tail"
    end
  end

  lookup :single_substitution, "Pipe operator" do
    substitutions do
      substitute ?<, "less.pipeoperator"
      substitute ?>, "greater.pipeoperator"
      substitute ?|, "bar.pipeoperator"
    end
  end

  lookup :single_substitution, "Colon between equals" do
    substitutions do
      substitute ?:, "colon.eq"
    end
  end

  for len <- 1..3 do
    lookup :single_substitution, "Equals, #{len}px longer" do
      substitutions do
        substitute ?=, "equal.#{len}px"
      end
    end
  end

  lookup :single_substitution, "Slashed equals, left" do
    substitutions do
      substitute ?=, "equal.slashed.left"
      substitute ?/, "slash.noteq"
    end
  end

  lookup :single_substitution, "Slashed equals, right" do
    substitutions do
      substitute ?=, "equal.slashed.right"
    end
  end
end
