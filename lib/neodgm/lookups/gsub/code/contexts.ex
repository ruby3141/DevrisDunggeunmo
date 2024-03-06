use PixelFont.OTFLayout

lookups NeoDGM.Lookups.GSUB.Code.Contexts, for: "GSUB" do
  module do
    defp scripts, do: %{"DFLT" => [:default], "latn" => [:default]}
  end

  lookup :chained_context, "Left arrow head" do
    feature "calt", scripts()

    context do
      backtrack '<'
      input '-', apply: "Arrow body"
    end

    context do
      backtrack '<'
      input '=', apply: "Arrow body"
      lookahead '-='
    end
  end

  lookup :chained_context, "Left arrow body" do
    feature "calt", scripts()

    context do
      backtrack ~w(hyphen.arrow equal.arrow)
      input '-=', apply: "Arrow body"
    end
  end

  lookup :chained_context, "Right arrow head" do
    feature "calt", scripts()

    context do
      input '-=', apply: "Arrow body"
      input '>', apply: "Right arrow head"
    end
  end

  lookup :chained_context, "Markup comment chain" do
    feature "calt", scripts()

    context do
      backtrack '<'
      input '!', apply: "Markup comment exclam"
      input '-', apply: "Markup comment hyphen body"
      input '-', apply: "Markup comment hyphen tail"
    end
  end

  lookup :reverse_chaining_context, "Right arrow body" do
    feature "calt", scripts()

    context do
      lookahead ~w(hyphen.arrow equal.arrow)
      substitute ?-, "hyphen.arrow"
      substitute ?=, "equal.arrow"
    end
  end

  lookup :chained_context, "Pipe operator chain" do
    feature "calt", scripts()

    context do
      input '<', apply: "Pipe operator"
      input '|', apply: "Pipe operator"
    end

    context do
      backtrack ~w(bar.pipeoperator)
      input '|', apply: "Pipe operator"
    end

    context do
      input '|', apply: "Pipe operator"
      input '>', apply: "Pipe operator"
    end

    context do
      backtrack ~w(bar.pipeoperator)
      input '>', apply: "Pipe operator"
    end
  end

  lookup :reverse_chaining_context, "Right pipe operator chain" do
    feature "calt", scripts()

    context do
      lookahead ~w(bar.pipeoperator)
      substitute ?|, "bar.pipeoperator"
    end
  end

  lookup :chained_context, "Equality operators chain" do
    feature "calt", scripts()

    # 3-glyph sequences

    context do
      backtrack '!'
      input '=', apply: "Equals, 2px longer"
      input '=', apply: "Equals, 2px longer"
    end

    context do
      input '=', apply: "Slashed equals, left"
      input '/', apply: "Slashed equals, left"
      input '=', apply: "Slashed equals, right"
    end

    context do
      input '=', apply: "Equals, 2px longer"
      input ':', apply: "Colon between equals"
      input '=', apply: "Equals, 2px longer"
    end

    # 2-glyph sequences

    context do
      input '=', apply: "Equals, 1px longer"
      input '=', apply: "Equals, 1px longer"
    end

    context do
      backtrack '!'
      input '=', apply: "Equals, 3px longer"
    end

    context do
      input ':', apply: "Colon between equals"
      input '=', apply: "Equals, 3px longer"
    end

    context do
      input '/', apply: "Slashed equals, left"
      input '=', apply: "Slashed equals, right"
    end

    # Equals sequence continuation

    context do
      backtrack ~w(equal.1px)
      input '=', apply: "Equals, 1px longer"
    end
  end
end
