use PixelFont.NameTable

ver = Version.parse!(Mix.Project.config()[:version])
patch_str = ver.patch |> to_string() |> String.pad_leading(2, "0")
version_str = "#{ver.pre}, based on NeoDunggeunmo #{ver.major}.#{ver.minor}#{patch_str}"

copyright_en = """
Original font was released under the public domain by Jungtae Kim \
in 1990s. \
Conversion and additional character design by Dalgona. \
<me@dalgona.dev> \
Customized code ligatures by CDnX. \
<ruby3141@gmail.com>\
"""

copyright_ko = """
원본 글꼴은 1990년대에 김중태 한글문화원 원장에 의해 퍼블릭 \
도메인으로 공개되었습니다. \
변환 및 추가적인 문자 디자인: Dalgona. <me@dalgona.dev> \
코드 ligature 수정: CDnX. <ruby3141@gmail.com>\
"""

license_en = """
This font software may be used, studied, modified, embedded and \
redistributed under the SIL Open Font License 1.1.\
"""

license_ko = """
이 폰트 소프트웨어는 SIL Open Font License 1.1에서 허용하는 범위 내에서 \
사용, 연구, 수정, 임베드 및 재배포될 수 있습니다.\
"""

name_table NeoDGM.NameTable.Code do
  name_records language: "en-US" do
    copyright copyright_en
    family "DevrisDunggeunmo"
    subfamily "Regular"
    unique_id "CDnX : DevrisDunggeunmo : 2024"
    full_name "DevrisDunggeunmo"
    version version_str
    postscript_name "DevrisDunggeunmo"
    license license_en
    license_url "https://scripts.sil.org/OFL"
  end

  name_records language: "ko-KR" do
    copyright copyright_ko
    family "Devris둥근모"
    subfamily "보통"
    full_name "Devris둥근모"
    version version_str
    postscript_name "DevrisDunggeunmo"
    license license_ko
    license_url "https://scripts.sil.org/OFL"
  end
end
