# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/psgo
# catalog-date 2008-09-06 19:20:59 +0200
# catalog-license lppl
# catalog-version 0.17
Name:		texlive-psgo
Version:	0.17
Release:	8
Summary:	Typeset go diagrams with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/psgo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psgo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psgo.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.17-2
+ Revision: 755148
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.17-1
+ Revision: 719321
- texlive-psgo
- texlive-psgo
- texlive-psgo
- texlive-psgo

