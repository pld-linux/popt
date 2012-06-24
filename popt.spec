%define snap 20030515
Summary:	C library for parsing command line parameters
Summary(de):	C-Library zum Parsen von Befehlszeilenparametern
Summary(fr):	Biblioth�que C pour analyser les param�tres de la ligne de commande
Summary(pl):	Biblioteka C do przetwarzania parametr�w przekazywanych do program�w w linii polece�
Summary(tr):	Komut sat�r� parametrelerini ayr��t�r�mak i�in C ar�ivi
Name:		popt
Version:	1.9
Release:	0.%{snap}.1
License:	LGPL
Group:		Libraries
#Source0:	ftp://ftp.rpm.org/pub/rpm/dist/rpm-4.1.x/%{name}-%{version}.%{snap}.tar.gz
Source0:	%{name}-%{version}.%{snap}.tar.gz
# Source0-md5:	bd43546659a4b6b1b462f62ace22a0d7
Patch0:		%{name}-values.patch
Patch1:		%{name}-gettext0.11.patch
Patch2:		%{name}-pl.po.patch
Patch3:		%{name}-zh_CN.patch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	libtool
BuildRequires:	glibc-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't require very fresh rpm.macros to build
%define         __gettextize gettextize --copy --force --intl ; cp -f po/Makevars{.template,}

%description
Popt is a C library for passing command line parameters. It was heavily
influenced by the getopt() and getopt_long() functions, but it allows
more powerful argument expansion. It can parse arbitrary argv[] style
arrays and automatically set variables based on command line
arguments. It also allows command line arguments to be aliased via
configuration files and includes utility functions for parsing
arbitrary strings into argv[] arrays using shell-like rules.

%description -l de
Popt ist eine C-Library zum Parsen von Befehlszeilenparametern, stark
beeinflu�t von den getopt() und getopt_long()-Funktionen, aber mit
sehr viel besserer Argumenterweiterung. Es k�nnen beliebige
argv[]-Argument- Arrays geparst und Variablen auf der Basis von
Befehlszeilenargumenten automatisch gesetzt werden. Ferner k�nnen
Befehlszeilenargumente �ber Konfigurationsdateien ge-aliast werden,
und die Library enth�lt Utility- funktionen zum Parsen beliebiger
Strings in argv[]-Arrays anhand von Shell-�hnlichen Regeln.

%description -l fr
Popt est une biblioth�que C pour analyser les param�tres de la ligne
de commande. Elle a �t� beaucoup influenc�e par les fonctions getopt()
et getopt_long() mais permet une expansion plus puissante des
arguments. Elle peut analyser des tableaux arbitraires du style argv[]
et configure les variables automatiquement selon les arguments de la
ligne de commande. Elle permet aussi � ces arguments d'�tre des alias
via des fichiers de configuration et inclut des fonctions utilitaires
pour analyser des cha�nes arbitraires dans les tableaux argv[] en
utilisant des r�gles � la shell

%description -l pl
Popt jest bibliotek� C s�u��c� przetwarzaniu parametr�w wywo�ania.
Du�y wp�yw mia�y na ni� getopt() i getopt_long(), ale ma od nich
znacznie wi�ksze mo�liwo�ci. Mo�e przetwarza� bezpo�rednio tablice
typu argv[] i automatycznie ustawia� zmienne w oparciu i parametry
wywo�ania. Pozwala tak�e na tworzenie zwi�zk�w pomi�dzy argumentami
wywo�ania a plikami konfiguracyjnymi oraz pozwala zamienia� ci�gi
znak�w na tablice typu argv[] z wykorzystaniem zasad znanych z pow�ok
(shelli).

%description -l tr
Popt, komut sat�r� parametrelerini ayr��t�ran bir C ar�ividir.
Geli�ig�zel argv[] tarz� dizileri ayr��t�rabilir ve otomatik olarak
komut sat�r� de�i�kenlerine dayal� de�i�kenleri atayabilir.

%package devel
Summary:	Header file and documentation for popt development
Summary(pl):	Pliki nag��wkowe i dokumentacja dla popt
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header file and documentation for popt development.

%description devel -l pl
Pliki nag��wkowe i dokumentacja dla popt.

%package static
Summary:	Static library for popt development
Summary(pl):	Biblioteka statyczna popt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static library for popt development.

%description static -l pl
Biblioteka statyczna popt.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .orig
%patch3 -p1

mv -f po/zh_CN{.GB2312,}.po

%build
rm -f missing
%{__gettextize}
autoupdate
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake} -i
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* $RPM_BUILD_ROOT/lib
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so
ln -sf /lib/`(cd $RPM_BUILD_ROOT/lib; echo *)` \
	$RPM_BUILD_ROOT%{_libdir}/libpopt.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) /lib/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpopt.so
%{_libdir}/libpopt.la
%{_mandir}/man3/*
%{_includedir}/popt.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libpopt.a
