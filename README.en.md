# DevrisDunggeunmo

LANG: EN / [KO](README.md)

Fork of NeoDunggeunmo Code, with ligatures modified to suits my taste.

[NeoDunggeunmo(Neo둥근모)](http://neodgm.dalgona.dev) is a general-purpose TrueType font
based on a famous Korean bitmap font "Dunggeunmo-kkol(둥근모꼴)",
which was designed for use in DOS.

<sub>Seriously, the official site of NeoDunggeunmo is awesome. You should check it.</sub>

## Difference from NeoDunggeunmo Code

WIP. Coming Soon™

## Manually Building Fonts from the Source Code

1. The source code of NeoDunggeunmo is written in Elixir programming language.
   Visit [the official Elixir website](https://elixir-lang.org) to install the
   appropriate version of Elixir for your operating system.

1. Clone this repository using Git.

    ```sh
    $ git clone https://github.com/ruby3141/DevrisDunggeunmo.git
    ```

1. Enter these commands to build TTF files.

    ```sh
    $ mix deps.get
    $ MIX_ENV=prod mix pixel_font.build --variant code
    ```

    It would fail to build without code ligature, as the corresponding nametable got removed.

1. A file named `DevrisDunggeunmo.ttf` will be created in your PWD.

1. run `postbuild.py` on ffpython, or python runtime with fontforge library installed.
   It generates bitmap glyphs.

1. run `postbuild2.py` on python runtime with fontTools library installed.
   It generates fake Bold/Italic TTF files, TTC collection file, and woff/woff2 compressed font files.
