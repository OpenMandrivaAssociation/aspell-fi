%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 0.7-0
%define fname aspell6-%{languagecode}
%define aspell_ver 0.60
%define languageenglazy Finnish
%define languagecode fi
%define lc_ctype fi_FI

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       0.60.0
Release:       %mkrel 15
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:		   http://aspell.sourceforge.net/
License:	   GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
BuildRequires: aspell >= %{aspell_ver}
BuildRequires: make
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
Provides:      aspell-dictionary
Provides:	   aspell-%{lc_ctype}
Provides:      spell-%{languagecode}
# old ispell is repalced with aspell
Obsoletes:	   ispell-%{languagecode}

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

mv -f README README.%{languagecode}
chmod 644 Copyright README.%{languagecode} 

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.%{languagecode} Copyright doc/*
%{_libdir}/aspell-%{aspell_ver}/*




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-13mdv2011.0
+ Revision: 662812
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-12mdv2011.0
+ Revision: 603207
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-11mdv2010.1
+ Revision: 518921
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-10mdv2010.0
+ Revision: 413064
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.60.0-9mdv2009.1
+ Revision: 350022
- 2009.1 rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.60.0-8mdv2009.0
+ Revision: 267914
+ rebuild (emptylog)

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.60.0-7mdv2009.0
+ Revision: 220376
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 0.60.0-6mdv2008.1
+ Revision: 182422
- provide enchant-dictionary

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-5mdv2008.1
+ Revision: 178857
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-3mdv2007.0
+ Revision: 123251
- Import aspell-fi

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-3mdv2007.1
- use the mkrel macro
- disable debug packages

* Mon Feb 13 2006 Pablo Saratxaga <pablo@mandrakesoft.com> 0.60.0-3mdk
- cleaning rpm and standardizing with other aspell-* ones
- including doc files in package

* Thu Feb 02 2006 Stefan van der Eijk <stefan@eijk.nu> 0.60.0-1mdk
- drop BuildRequires ispell: it's a contrib package + doesn't seem
  to be needed to build the package
- %%mkrel

* Mon Nov 28 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.60.0-1mdk
- new release (real aspell dict, not old ispell one being recycled)
  (thus saving 20Mb on the CDs)
- build for new aspell

* Tue Jul 20 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.0-1mdk
- first version for aspell (wordlist taken from ispell Finnish dictionnary;
  none of the aspell niceties is used for now)

