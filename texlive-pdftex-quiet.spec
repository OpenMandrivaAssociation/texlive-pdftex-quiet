%global tl_name pdftex-quiet
%global tl_revision 49169

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	A bash wrapper for pdfTeX limiting its output to relevant errors
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/pdftex-quiet
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex-quiet.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex-quiet.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(pdftex-quiet.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a bash script aiming at reducing pdfTeX's output
to relevant errors, which are displayed in a red bold font. The project
originally started as a TeX StackExchange answer.

