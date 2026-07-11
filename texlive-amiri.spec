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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Amiri is a classical Arabic typeface in Naskh style for typesetting
books and other running text. It is a revival of the beautiful typeface
pioneered in the early 20th century by Bulaq Press in Cairo, also known
as Amiria Press, after which the font is named. The project aims at the
revival of the aesthetics and traditions of Arabic typesetting, and
adapting it to the era of digital typesetting, in a publicly available
form.

