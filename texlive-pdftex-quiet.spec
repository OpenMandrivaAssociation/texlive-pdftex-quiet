Name:		texlive-pdftex-quiet
Version:	49169
Release:	1
Summary:	A bash wrapper for pdfTeX limiting its output to relevant errors
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pdftex-quiet
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex-quiet.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftex-quiet.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a bash script aiming at reducing pdfTeX's
output to relevant errors, which are displayed in a red bold
font. The project originally started as a TeX StackExchange
answer.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/scripts/pdftex-quiet
%doc %{_texmfdistdir}/texmf-dist/doc/support/pdftex-quiet

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
