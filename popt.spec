#
# Conditional build:
%bcond_with	dietlibc	# static dietlibc library

Summary:	C library for parsing command line parameters
Summary(de.UTF-8):	C-Library zum Parsen von Befehlszeilenparametern
Summary(fr.UTF-8):	Bibliothèque C pour analyser les paramètres de la ligne de commande
Summary(pl.UTF-8):	Biblioteka C do przetwarzania parametrów przekazywanych do programów w linii poleceń
Summary(ru.UTF-8):	Библиотека C для разбора параметров командной строки
Summary(tr.UTF-8):	Komut satırı parametrelerini ayrıştırımak için C arşivi
Summary(uk.UTF-8):	Бібліотека C для розбору параметрів командної стрічки
Name:		popt
Version:	1.18
Release:	2
License:	X Consortium (MIT-like)
Group:		Libraries
Source0:	http://ftp.rpm.org/popt/releases/popt-1.x/%{name}-%{version}.tar.gz
# Source0-md5:	450f2f636e6a3aa527de803d0ae76c5a
Patch0:		%{name}-diet.patch
Patch1:		%{name}-pl.po-update.patch
URL:		https://rpm.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.4
%{?with_dietlibc:BuildRequires:	dietlibc-static >= 2:0.31-5}
BuildRequires:	gettext-tools >= 0.11.5
BuildRequires:	libtool >= 2:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# for some reason known only to rpm there must be "\\|" not "\|" here
%define		dietarch	%(echo %{_target_cpu} | sed -e 's/i.86\\|pentium.\\|athlon/i386/;s/amd64/x86_64/;s/armv.*/arm/')
%define		dietlibdir	%{_prefix}/lib/dietlibc/lib-%{dietarch}

%description
Popt is a C library for passing command line parameters. It was
heavily influenced by the getopt() and getopt_long() functions, but it
allows more powerful argument expansion. It can parse arbitrary argv[]
style arrays and automatically set variables based on command line
arguments. It also allows command line arguments to be aliased via
configuration files and includes utility functions for parsing
arbitrary strings into argv[] arrays using shell-like rules.

%description -l de.UTF-8
Popt ist eine C-Library zum Parsen von Befehlszeilenparametern, stark
beeinflußt von den getopt() und getopt_long()-Funktionen, aber mit
sehr viel besserer Argumenterweiterung. Es können beliebige
argv[]-Argument- Arrays geparst und Variablen auf der Basis von
Befehlszeilenargumenten automatisch gesetzt werden. Ferner können
Befehlszeilenargumente über Konfigurationsdateien ge-aliast werden,
und die Library enthält Utility- funktionen zum Parsen beliebiger
Strings in argv[]-Arrays anhand von Shell-ähnlichen Regeln.

%description -l fr.UTF-8
Popt est une bibliothèque C pour analyser les paramêtres de la ligne
de commande. Elle a été beaucoup influencée par les fonctions getopt()
et getopt_long() mais permet une expansion plus puissante des
arguments. Elle peut analyser des tableaux arbitraires du style argv[]
et configure les variables automatiquement selon les arguments de la
ligne de commande. Elle permet aussi à ces arguments d'être des alias
via des fichiers de configuration et inclut des fonctions utilitaires
pour analyser des chaînes arbitraires dans les tableaux argv[] en
utilisant des règles à la shell

%description -l pl.UTF-8
Popt jest biblioteką C służącą przetwarzaniu parametrów wywołania.
Duży wpływ miały na nią getopt() i getopt_long(), ale ma od nich
znacznie większe możliwości. Może przetwarzać bezpośrednio tablice
typu argv[] i automatycznie ustawiać zmienne w oparciu i parametry
wywołania. Pozwala także na tworzenie związków pomiędzy argumentami
wywołania a plikami konfiguracyjnymi oraz pozwala zamieniać ciągi
znaków na tablice typu argv[] z wykorzystaniem zasad znanych z powłok
(shelli).

%description -l ru.UTF-8
Popt - это библиотека C для разбора параметров командной строки. Она
построена по образу и подобию функций getopt() и getopt_long(), но в
отличие от последних позволяет более мощное расширение аргументов. Она
может разбирать произвольные массивы в стиле argv[] и автоматически
устанавливать переменные в зависимости от аргументов командной строки.
Также она позволяет создавать алиасы через конфигурационные файлы и
включает функции для разбора произвольных строк в массивах argv[] с
использованием шелл-подобных правил.

%description -l tr.UTF-8
Popt, komut satırı parametrelerini ayrıştıran bir C arşividir.
Gelişigüzel argv[] tarzı dizileri ayrıştırabilir ve otomatik olarak
komut satırı değişkenlerine dayalı değişkenleri atayabilir.

%description -l uk.UTF-8
Popt - це бібліотека C для розбору параметрів командної стрічки. Вона
побудована на кшталт функцій getopt() та getopt_long(), але на відміну
від останніх дозволяє більш потужне розширення аргументів. Вона може
розбирати довільні масиви в стилі argv[] та автоматично встановлювати
змінні в залежності від аргументів командної стрічки. Також вона
дозволяє створювати аліаси через конфігураційні файли та містить
функції для розбору довільних стрічок в масивах argv[] з використанням
шелл-подібних правил.

%package devel
Summary:	Header file and documentation for popt development
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla popt
Summary(ru.UTF-8):	Хедеры и библиотека, необходимые для программирования с popt
Summary(uk.UTF-8):	Хедери та бібліотека, необхідні для програмування з popt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file and documentation for popt development.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla popt.

%description devel -l ru.UTF-8
Этот пакет содержит библиотеку и хедеры, необходимые для разработки
программ, использующих popt.

%description devel -l uk.UTF-8
Цей пакет містить бібліотеку та хедери, необхідні для розробки
програм, що використовують popt.

%package static
Summary:	Static library for popt development
Summary(pl.UTF-8):	Biblioteka statyczna popt
Summary(ru.UTF-8):	Статические библиотеки popt
Summary(uk.UTF-8):	Статичні бібліотеки popt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static library for popt development.

%description static -l pl.UTF-8
Biblioteka statyczna popt.

%description static -l ru.UTF-8
Это отдельный пакет со статическими библиотеками, которые больше не
входят в popt-devel.

%description static -l uk.UTF-8
Це окремий пакет зі статичними бібліотеками, що більше не входять в
склад popt-devel.

%package dietlibc
Summary:	Static dietlibc library for popt development
Summary(pl.UTF-8):	Biblioteka statyczna dietlibc popt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description dietlibc
Static dietlibc library for popt development.

%description dietlibc -l pl.UTF-8
Biblioteka statyczna dietlibc popt.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's#po/Makefile.in intl/Makefile##g' configure.ac

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake} -i

%if %{with dietlibc}
__cc="%{__cc}"
%configure \
	CC="diet ${__cc#ccache } %{rpmcflags} %{rpmldflags} -Os -static" \
	ac_cv_func_stpcpy=yes \
%if "%{?configure_cache}" == "1"
	--cache-file=%{?configure_cache_file}%{!?configure_cache_file:configure}-initrd.cache \
%endif
	--disable-shared \
	--disable-silent-rules \
	--enable-static

# libpopt.la dependency on configmake.h missing
%{__make} configmake.h
%{__make} libpopt.la
%{__mv} .libs/libpopt.a diet-libpopt.a
%{__make} clean
%endif

%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_lib}
%{?with_dietlibc:install -d $RPM_BUILD_ROOT%{dietlibdir}}

%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_libdir}/libpopt.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libpopt.so.*.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libpopt.so

%{?with_dietlibc:install diet-libpopt.a $RPM_BUILD_ROOT%{dietlibdir}/libpopt.a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) /%{_lib}/libpopt.so.*.*.*
%attr(755,root,root) %ghost /%{_lib}/libpopt.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpopt.so
%{_libdir}/libpopt.la
%{_includedir}/popt.h
%{_pkgconfigdir}/popt.pc
%{_mandir}/man3/popt.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpopt.a

%if %{with dietlibc}
%files dietlibc
%defattr(644,root,root,755)
%{dietlibdir}/libpopt.a
%endif
