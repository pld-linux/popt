Summary:     C library for parsing command line parameters
Summary(de): C-Library zum Parsen von Befehlszeilenparametern 
Summary(fr): Biblioth�que C pour analyser les param�tres de la ligne de commande
Summary(pl): Biblioteka C do przetwarzania parametr�w przekazywanych do program�w w linii polece�
Summary(tr): Komut sat�r� parametrelerini ayr��t�r�mak i�in C ar�ivi
Name:        popt
Version:     1.1.1
Release:     3
Copyright:   LGPL
Group:       Utilities/System
Source:      ftp://ftp.redhat.com/pub/redhat/code/popt/%{name}-%{version}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

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
beeinflu�t von den getopt() und getopt_long()-Funktionen, aber mit sehr 
viel besserer Argumenterweiterung. Es k�nnen beliebige argv[]-Argument-
Arrays geparst und Variablen auf der Basis von Befehlszeilenargumenten
automatisch gesetzt werden. Ferner k�nnen Befehlszeilenargumente �ber
Konfigurationsdateien ge-aliast werden, und die Library enth�lt Utility-
funktionen zum Parsen beliebiger Strings in argv[]-Arrays anhand von 
Shell-�hnlichen Regeln. 

%description -l fr
Popt est une biblioth�que C pour analyser les param�tres de la ligne de
commande. Elle a �t� beaucoup influenc�e par les fonctions getopt() et
getopt_long() mais permet une expansion plus puissante des arguments. Elle
peut analyser des tableaux arbitraires du style argv[] et configure les
variables automatiquement selon les arguments de la ligne de commande.
Elle permet aussi � ces arguments d'�tre des alias via des fichiers de
configuration et inclut des fonctions utilitaires pour analyser des
cha�nes arbitraires dans les tableaux argv[] en utilisant des r�gles
� la shell

%description -l pl
Popt jest bibliotek� C s�u��c� 
Popt is a C library for pasing command line parameters. It was heavily
influenced by the getopt() and getopt_long() functions, but it allows
more powerfull argument expansion. It can parse arbitrary argv[] style
arrays and automatically set variables based on command line arguments.
It also allows command line arguments to be aliased via configuration
files and includes utility functions for parsing arbitrary strings into
argv[] arrays using shell-like rules. 

%description -l tr
Popt, komut sat�r� parametrelerini ayr��t�ran bir C ar�ividir. Geli�ig�zel
argv[] tarz� dizileri ayr��t�rabilir ve otomatik olarak komut sat�r�
de�i�kenlerine dayal� de�i�kenleri atayabilir.

%prep
%setup -q
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
	--prefix=/usr

%build
make

%install
make PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
/usr/lib/libpopt.a
/usr/include/popt.h

%changelog
* Sat Aug 15 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
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
