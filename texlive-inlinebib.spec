Name:		texlive-inlinebib
Version:	20061212
Release:	1
Summary:	Citations in footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/inlinebib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinebib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinebib.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A BibTeX style and a LaTeX package that allow for a full
bibliography at the end of the document as well as citation
details in footnotes. The footnote details include "op. cit."
and "ibid." contractions.

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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
