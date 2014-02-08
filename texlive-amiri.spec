# revision 27114
# category Package
# catalog-ctan /fonts/amiri
# catalog-date 2012-07-19 13:24:09 +0200
# catalog-license ofl
# catalog-version 0.104
Name:		texlive-amiri
Epoch:		1
Version:	0.104
Release:	2
Summary:	A classical Arabic typeface, Naskh style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/amiri
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amiri.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amiri.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a beta-release of the font, though it is believed to be
largely usable. (The author retains the right to make
incompatible changes in the future.) The font covers the Arabic
and Arabic Supplement blocks of Unicode 6.0, which means it
essentially covers any language written in Arabic script and
supported by Unicode.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/truetype/public/amiri/amiri-bold.ttf
%{_texmfdistdir}/fonts/truetype/public/amiri/amiri-boldslanted.ttf
%{_texmfdistdir}/fonts/truetype/public/amiri/amiri-regular.ttf
%{_texmfdistdir}/fonts/truetype/public/amiri/amiri-slanted.ttf
%doc %{_texmfdistdir}/doc/fonts/amiri/Makefile
%doc %{_texmfdistdir}/doc/fonts/amiri/OFL-FAQ.txt
%doc %{_texmfdistdir}/doc/fonts/amiri/OFL.txt
%doc %{_texmfdistdir}/doc/fonts/amiri/README
%doc %{_texmfdistdir}/doc/fonts/amiri/documentation/NEWS-Arabic.txt
%doc %{_texmfdistdir}/doc/fonts/amiri/documentation/NEWS.txt
%doc %{_texmfdistdir}/doc/fonts/amiri/documentation/README-Arabic.txt
%doc %{_texmfdistdir}/doc/fonts/amiri/documentation/README.txt
%doc %{_texmfdistdir}/doc/fonts/amiri/documentation/amiri-table.pdf
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/amiri-bold.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/amiri-regular.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/amiri-regular.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/amiri-slanted.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/basic.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/classes.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/contextuals.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/Crimson-Bold.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/Crimson-BoldItalic.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/Crimson-Italic.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/Crimson-Roman-edits.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/Crimson-Roman.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/Crimson-Semibold.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/Crimson-SemiboldItalic.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/calt.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/calt_italic.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/crimson.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/crimson_italic.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/fractions.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/italic_glyphclasses.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/ligatures.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/locl.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/numbers.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/numbers_italic.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/roman_glyphclasses.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/smallcaps.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/subs_sups.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/variants.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/crimson/sources/OT-featurefiles/variants_italic.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/enclosing.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/italic_classes.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/italic_ltra.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/italic_proportional.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/italic_rtla.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/kashida.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/kerning.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/lang.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/lang_arabic.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/lang_latin.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/latin_gsub.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/lellah.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/local.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/proportional.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/quran.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/rtlm.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/stylisticsets.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/basic.test
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/enclosing.ptest
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/extendedmeem.test
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/high_baa.test
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/lellah.test
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/local.test
%doc %{_texmfdistdir}/doc/fonts/amiri/tools/build.py
%doc %{_texmfdistdir}/doc/fonts/amiri/tools/runtest.py

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
