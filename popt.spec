Summary:	C library for parsing command line parameters
Summary(de):	C-Library zum Parsen von Befehlszeilenparametern 
Summary(fr):	Bibliothèque C pour analyser les paramètres de la ligne de commande
Summary(pl):	Biblioteka C do przetwarzania parametrów przekazywanych do programów w linii poleceñ
Summary(tr):	Komut satýrý parametrelerini ayrýþtýrýmak için C arþivi
Name:		popt
Version:	1.3
Release:	2
Copyright:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.redhat.com/pub/redhat/code/popt/%{name}-%{version}.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
Popt is a C library for pasing command line parameters. It was heavily
influenced by the getopt() and getopt_long() functions, but it allows
more powerfull argument expansion. It can parse arbitrary argv[] style
arrays and automatically set variables based on command line arguments.
It also allows command line arguments to be aliased via configuration
files and includes utility functions for parsing arbitrary strings into
argv[] arrays using shell-like rules. 

%description -l de
Popt ist eine C-Library zum Parsen von Befehlszeilenparametern, stark
beeinflußt von den getopt() und getopt_long()-Funktionen, aber mit sehr 
viel besserer Argumenterweiterung. Es können beliebige argv[]-Argument-
Arrays geparst und Variablen auf der Basis von Befehlszeilenargumenten
automatisch gesetzt werden. Ferner können Befehlszeilenargumente über
Konfigurationsdateien ge-aliast werden, und die Library enthält Utility-
funktionen zum Parsen beliebiger Strings in argv[]-Arrays anhand von 
Shell-ähnlichen Regeln. 

%description -l fr
Popt est une bibliothèque C pour analyser les paramêtres de la ligne de
commande. Elle a été beaucoup influencée par les fonctions getopt() et
getopt_long() mais permet une expansion plus puissante des arguments. Elle
peut analyser des tableaux arbitraires du style argv[] et configure les
variables automatiquement selon les arguments de la ligne de commande.
Elle permet aussi à ces arguments d'être des alias via des fichiers de
configuration et inclut des fonctions utilitaires pour analyser des
chaînes arbitraires dans les tableaux argv[] en utilisant des règles
à la shell

%description -l pl
Popt jest bibliotek± C s³u¿±c± 
Popt is a C library for pasing command line parameters. It was heavily
influenced by the getopt() and getopt_long() functions, but it allows
more powerfull argument expansion. It can parse arbitrary argv[] style
arrays and automatically set variables based on command line arguments.
It also allows command line arguments to be aliased via configuration
files and includes utility functions for parsing arbitrary strings into
argv[] arrays using shell-like rules. 

%description -l tr
Popt, komut satýrý parametrelerini ayrýþtýran bir C arþividir. Geliþigüzel
argv[] tarzý dizileri ayrýþtýrabilir ve otomatik olarak komut satýrý
deðiþkenlerine dayalý deðiþkenleri atayabilir.

%package devel
Summary:	Header file and library for popt development
Summary(pl):	Pliki nag³ówkowe dla popt
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:       %{name} = %{version}

%description devel
Header file and library for popt development

%description devel -l pl
Pliki nag³ówkowe i dokumentacja dla popt

%package static
Summary:        Static library for popt development
Summary(pl):    Biblioteka statyczna do popt
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki
Requires:       %{name}-devel = %{version}

%description static
Static library for popt development

%description static -l pl
Biblioteka statyczna do popt

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=/usr \
	--enable-shared

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

make DESTDIR=$RPM_BUILD_ROOT install

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* $RPM_BUILD_ROOT/lib
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so
ln -sf ../../lib/`( cd $RPM_BUILD_ROOT/lib; echo *)` \
	$RPM_BUILD_ROOT%{_libdir}/libpopt.so
	
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%lang(ro) /usr/share/locale/ro/LC_MESSAGES/*
%attr(755,root,root) /lib/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpopt.so
%{_mandir}/man3/popt.3.gz
/usr/include/popt.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpopt.a
%{_libdir}/libpopt.la

%changelog
* Wed Apr 21 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.3-1]
- updated to 1.3,
- changed Group to Libraries,
- added Group(pl),
- DESTDIR instead of PREFIX in make install,
- added man pages in %files,
- gzipping man pages,
- ./configure moved from %setup to %build,
- added --disable-shared to configure options,
- added "rm -rf $RPM_BUILD_ROOT" in %install,
- cosmetic changes,
- recompiled on rpm 3.

* Sat Aug 15 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.1.1-3]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added pl translation,
- global %defattr macro instead %attr macros in %files.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- added ./configure step to spec file
