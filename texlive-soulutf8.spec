Name:		texlive-soulutf8
Version:	53163
Release:	2
Summary:	Permit use of UTF-8 characters in soul
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/soulutf8
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soulutf8.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soulutf8.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/soulutf8.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package extends package soul and adds some support for
UTF-8. Namely the input encodings in 'utf8.def' from package
inputenc and 'utf8x.def' from package ucs are supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/soulutf8
%{_texmfdistdir}/tex/generic/soulutf8
%doc %{_texmfdistdir}/doc/latex/soulutf8

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
