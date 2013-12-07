# revision 22018
# category Package
# catalog-ctan /biblio/bibtex/contrib/inlinebib
# catalog-date 2006-12-12 00:29:31 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-inlinebib
Version:	20061212
Release:	6
Summary:	Citations in footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/inlinebib
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinebib.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inlinebib.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061212-2
+ Revision: 752793
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061212-1
+ Revision: 718719
- texlive-inlinebib
- texlive-inlinebib
- texlive-inlinebib
- texlive-inlinebib

