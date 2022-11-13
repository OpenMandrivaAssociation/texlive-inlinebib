Name:		texlive-inlinebib
Version:	22018
Release:	1
Summary:	Citations in footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/inlinebib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinebib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinebib.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A BibTeX style and a LaTeX package that allow for a full
bibliography at the end of the document as well as citation
details in footnotes. The footnote details include "op. cit."
and "ibid." contractions.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/inlinebib/inlinebib.bst
%{_texmfdistdir}/tex/latex/inlinebib/inlinebib.sty
%{_texmfdistdir}/tex/latex/inlinebib/pageranges.sty
%doc %{_texmfdistdir}/doc/bibtex/inlinebib/MANIFEST
%doc %{_texmfdistdir}/doc/bibtex/inlinebib/inlinebib.htm
%doc %{_texmfdistdir}/doc/bibtex/inlinebib/inlinebib.txt
%doc %{_texmfdistdir}/doc/bibtex/inlinebib/inlinebib1.gif
%doc %{_texmfdistdir}/doc/bibtex/inlinebib/inlinebib2.gif

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
