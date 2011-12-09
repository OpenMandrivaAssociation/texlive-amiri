# revision 24783
# category Package
# catalog-ctan /fonts/amiri
# catalog-date 2011-12-06 08:35:17 +0100
# catalog-license ofl
# catalog-version 1.0
Name:		texlive-amiri
Version:	1.0
Release:	1
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

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
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
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/amiri-regular.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/amiri-regular.sfd
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/basic.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/classes.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/contextuals.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/enclosing.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/kashida.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/kerning.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/lang.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/lellah.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/local.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/quran.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/rtlm.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/sources/stylisticsets.fea
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/basic.test
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/extendedmeem.test
%doc %{_texmfdistdir}/doc/fonts/amiri/test-suite/lellah.test
%doc %{_texmfdistdir}/doc/fonts/amiri/tools/build.py
%doc %{_texmfdistdir}/doc/fonts/amiri/tools/runtest.py
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
