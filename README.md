# Devris둥근모

LANG: [EN](README.en.md) / KO

Neo둥근모 Code 폰트의 ligature를 제 입맛대로 수정한 포크입니다.

[Neo둥근모](http://neodgm.dalgona.dev)는 DOS용 비트맵 한글 글꼴인 "둥근모꼴"을
모든 환경에서 사용할 수 있도록 트루타입 글꼴로 변환하여 만든 글꼴입니다.

<sub>Neo둥근모 공식 사이트가 정말 멋집니다. 꼭 한 번 확인해보세요.</sub>

## Neo둥근모 Code와의 차이점

WIP. Coming Soon™

## 직접 빌드하기

1. Devris둥근모의 소스는 Elixir 프로그래밍 언어로 작성되어 있습니다. [Elixir
  웹 사이트](https://elixir-lang.org)에서 여러분이 사용하고 있는 운영 체제에
  맞는 Elixir 버전을 설치하세요.

1. Git을 사용하여 이 저장소를 복제하세요.

    ```sh
    $ git clone https://github.com/ruby3141/DevrisDunggeunmo.git
    ```

1. 아래 명령을 입력하여 TTF 파일을 빌드하세요.

    ```sh
    $ mix deps.get
    $ MIX_ENV=prod mix pixel_font.build --variant code
    ```

    Code ligature가 없는 버전은 네임테이블을 들어내버려서 빌드가 안 될 겁니다.

1. 현재 작업 디렉토리에 `DevrisDunggeunmo.ttf` 파일이 생성됩니다.

1. ffpython, 혹은 fontforge 라이브러리가 설치된 python 환경에서 `postbuild.py`를 실행합니다.
   Bitmap glyph, 가짜 Bold/Italic TTF 파일과 TTC 컬렉션 파일, woff/woff2 압축된 폰트 파일을 생성하는 스크립트입니다.
