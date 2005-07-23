#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	C library for parsing command line parameters
Summary(de):	C-Library zum Parsen von Befehlszeilenparametern
Summary(fr):	BibliothХque C pour analyser les paramХtres de la ligne de commande
Summary(pl):	Biblioteka C do przetwarzania parametrСw przekazywanych do programСw w linii poleceЯ
Summary(ru):	Библиотека C для разбора параметров командной строки
Summary(tr):	Komut satЩrЩ parametrelerini ayrЩЧtЩrЩmak iГin C arЧivi
Summary(uk):	Б╕бл╕отека C для розбору параметр╕в командно╖ стр╕чки
Name:		popt
Version:	1.10.2
Release:	1
License:	X Consortium (MIT-like)
Group:		Libraries
Source0:	ftp://jbj.org/pub/rpm-4.4.x/%{name}-%{version}.tar.gz
# Source0-md5:	eebda70ee032989a243145135175e54d
Patch0:		%{name}-values.patch
Patch1:		%{name}-gettext0.11.patch
Patch2:		%{name}-pl.po.patch
Patch3:		%{name}-libdir64.patch
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# don't require very fresh rpm.macros to build
%define		__gettextize	gettextize --copy --force --intl ; cp -f po/Makevars{.template,}

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
beeinfluъt von den getopt() und getopt_long()-Funktionen, aber mit
sehr viel besserer Argumenterweiterung. Es kЖnnen beliebige
argv[]-Argument- Arrays geparst und Variablen auf der Basis von
Befehlszeilenargumenten automatisch gesetzt werden. Ferner kЖnnen
Befehlszeilenargumente Эber Konfigurationsdateien ge-aliast werden,
und die Library enthДlt Utility- funktionen zum Parsen beliebiger
Strings in argv[]-Arrays anhand von Shell-Дhnlichen Regeln.

%description -l fr
Popt est une bibliothХque C pour analyser les paramЙtres de la ligne
de commande. Elle a ИtИ beaucoup influencИe par les fonctions getopt()
et getopt_long() mais permet une expansion plus puissante des
arguments. Elle peut analyser des tableaux arbitraires du style argv[]
et configure les variables automatiquement selon les arguments de la
ligne de commande. Elle permet aussi Ю ces arguments d'Йtre des alias
via des fichiers de configuration et inclut des fonctions utilitaires
pour analyser des chaНnes arbitraires dans les tableaux argv[] en
utilisant des rХgles Ю la shell

%description -l pl
Popt jest bibliotek╠ C sЁu©╠c╠ przetwarzaniu parametrСw wywoЁania.
Du©y wpЁyw miaЁy na ni╠ getopt() i getopt_long(), ale ma od nich
znacznie wiЙksze mo©liwo╤ci. Mo©e przetwarzaФ bezpo╤rednio tablice
typu argv[] i automatycznie ustawiaФ zmienne w oparciu i parametry
wywoЁania. Pozwala tak©e na tworzenie zwi╠zkСw pomiЙdzy argumentami
wywoЁania a plikami konfiguracyjnymi oraz pozwala zamieniaФ ci╠gi
znakСw na tablice typu argv[] z wykorzystaniem zasad znanych z powЁok
(shelli).

%description -l ru
Popt - это библиотека C для разбора параметров командной строки. Она
построена по образу и подобию функций getopt() и getopt_long(), но в
отличие от последних позволяет более мощное расширение аргументов. Она
может разбирать произвольные массивы в стиле argv[] и автоматически
устанавливать переменные в зависимости от аргументов командной строки.
Также она позволяет создавать алиасы через конфигурационные файлы и
включает функции для разбора произвольных строк в массивах argv[] с
использованием шелл-подобных правил.

%description -l tr
Popt, komut satЩrЩ parametrelerini ayrЩЧtЩran bir C arЧividir.
GeliЧigЭzel argv[] tarzЩ dizileri ayrЩЧtЩrabilir ve otomatik olarak
komut satЩrЩ deПiЧkenlerine dayalЩ deПiЧkenleri atayabilir.

%description -l uk
Popt - це б╕бл╕отека C для розбору параметр╕в командно╖ стр╕чки. Вона
побудована на кшталт функц╕й getopt() та getopt_long(), але на в╕дм╕ну
в╕д останн╕х дозволя╓ б╕льш потужне розширення аргумент╕в. Вона може
розбирати дов╕льн╕ масиви в стил╕ argv[] та автоматично встановлювати
зм╕нн╕ в залежност╕ в╕д аргумент╕в командно╖ стр╕чки. Також вона
дозволя╓ створювати ал╕аси через конф╕гурац╕йн╕ файли та м╕стить
функц╕╖ для розбору дов╕льних стр╕чок в масивах argv[] з використанням
шелл-под╕бних правил.

%package devel
Summary:	Header file and documentation for popt development
Summary(pl):	Pliki nagЁСwkowe i dokumentacja dla popt
Summary(ru):	Хедеры и библиотека, необходимые для программирования с popt
Summary(uk):	Хедери та б╕бл╕отека, необх╕дн╕ для програмування з popt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file and documentation for popt development.

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja dla popt.

%description devel -l ru
Этот пакет содержит библиотеку и хедеры, необходимые для разработки
программ, использующих popt.

%description devel -l uk
Цей пакет м╕стить б╕бл╕отеку та хедери, необх╕дн╕ для розробки
програм, що використовують popt.

%package static
Summary:	Static library for popt development
Summary(pl):	Biblioteka statyczna popt
Summary(ru):	Статические библиотеки popt
Summary(uk):	Статичн╕ б╕бл╕отеки popt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for popt development.

%description static -l pl
Biblioteka statyczna popt.

%description static -l ru
Это отдельный пакет со статическими библиотеками, которые больше не
входят в popt-devel.

%description static -l uk
Це окремий пакет з╕ статичними б╕бл╕отеками, що б╕льше не входять в
склад popt-devel.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/{eu_ES,eu}.po
mv -f po/{no,nb}.po

%build
%{__gettextize}
%{__libtoolize}
%{__autoheader}
%{__aclocal}
%{__autoconf}
%{__automake} -i
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.* $RPM_BUILD_ROOT/%{_lib}
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.so
ln -sf /%{_lib}/`(cd $RPM_BUILD_ROOT/%{_lib}; echo *)` \
	$RPM_BUILD_ROOT%{_libdir}/libpopt.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) /%{_lib}/libpopt.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpopt.so
%{_libdir}/libpopt.la
%{_mandir}/man3/*
%{_includedir}/popt.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libpopt.a
%endif
