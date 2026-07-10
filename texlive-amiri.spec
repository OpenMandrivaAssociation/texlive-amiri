%global tl_name amiri
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.000
Release:	%{tl_revision}.1
Summary:	A classical Arabic typeface, Naskh style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/amiri
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amiri.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amiri.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Amiri is a classical Arabic typeface in Naskh style for typesetting
books and other running text. It is a revival of the beautiful typeface
pioneered in the early 20th century by Bulaq Press in Cairo, also known
as Amiria Press, after which the font is named. The project aims at the
revival of the aesthetics and traditions of Arabic typesetting, and
adapting it to the era of digital typesetting, in a publicly available
form.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/truetype
%dir %{_datadir}/texmf-dist/doc/fonts/amiri
%dir %{_datadir}/texmf-dist/fonts/truetype/public
%dir %{_datadir}/texmf-dist/fonts/truetype/public/amiri
%doc %{_datadir}/texmf-dist/doc/fonts/amiri/Documentation-Arabic.html
%doc %{_datadir}/texmf-dist/doc/fonts/amiri/NEWS-Arabic.md
%doc %{_datadir}/texmf-dist/doc/fonts/amiri/NEWS.md
%doc %{_datadir}/texmf-dist/doc/fonts/amiri/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/amiri/README-Arabic.md
%doc %{_datadir}/texmf-dist/doc/fonts/amiri/README.md
%{_datadir}/texmf-dist/fonts/truetype/public/amiri/Amiri-Bold.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/amiri/Amiri-BoldItalic.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/amiri/Amiri-Italic.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/amiri/Amiri-Regular.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/amiri/AmiriQuran.ttf
%{_datadir}/texmf-dist/fonts/truetype/public/amiri/AmiriQuranColored.ttf
