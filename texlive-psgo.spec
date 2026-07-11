%global tl_name psgo
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.17
Release:	%{tl_revision}.1
Summary:	Typeset go diagrams with PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/psgo
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psgo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psgo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Typeset go diagrams with PSTricks

