Name:		texlive-amiri
Epoch:		1
Version:	55403
Release:	1
Summary:	A classical Arabic typeface, Naskh style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/amiri
License:	OFL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amiri.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amiri.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/fonts/truetype/public/amiri
%doc %{_texmfdistdir}/doc/fonts/amiri

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
