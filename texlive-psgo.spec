Name:		texlive-psgo
Version:	15878
Release:	2
Summary:	Typeset go diagrams with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/psgo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psgo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psgo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive psgo package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/psgo/psgo.sty
%doc %{_texmfdistdir}/doc/latex/psgo/Changes
%doc %{_texmfdistdir}/doc/latex/psgo/README
%doc %{_texmfdistdir}/doc/latex/psgo/psgomanual.pdf
%doc %{_texmfdistdir}/doc/latex/psgo/psgomanual.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
