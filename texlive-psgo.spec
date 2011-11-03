# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/psgo
# catalog-date 2008-09-06 19:20:59 +0200
# catalog-license lppl
# catalog-version 0.17
Name:		texlive-psgo
Version:	0.17
Release:	1
Summary:	Typeset go diagrams with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/psgo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psgo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psgo.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive psgo package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
