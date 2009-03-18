Summary:	GNOME integrated development environment
Summary(es.UTF-8):	Entorno integrado de desarrollo (IDE) de GNOME
Summary(pl.UTF-8):	Zintegrowane środowisko programowania dla GNOME
Summary(pt_BR.UTF-8):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	2.26.0.0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/anjuta/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	6da89e8d31786376eb7f37d77ccbddf7
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-includes.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	ORBit2-devel >= 1:2.14.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	autogen
BuildRequires:	automake >= 1:1.9
BuildRequires:	binutils-devel >= 3:2.15.92
BuildRequires:	devhelp-devel >= 0.22
BuildRequires:	gdl-devel >= 2.26.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.20.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils
BuildRequires:	graphviz-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	gtk-webkit-devel
BuildRequires:	gtksourceview2-devel >= 2.5.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgda4-devel >= 3.99.7
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgladeui-devel >= 3.5.7
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel
BuildRequires:	neon-devel >= 0.28.2
BuildRequires:	perl-Locale-gettext
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	subversion-devel >= 1.5.0
BuildRequires:	unique-devel >= 1.0.0
BuildRequires:	vte-devel >= 0.17.4
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
# Requires:	gnome-terminal
Requires:	glib2 >= 1:2.19.7
Requires:	libanjuta = %{epoch}:%{version}-%{release}
Requires:	libgda4-provider-sqlite >= 3.99.7
Requires:	pkgconfig
Suggests:	ctags
Obsoletes:	gnome-build
Obsoletes:	gnome-build-devel
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anjuta is a very versatile integrated development environment for C
and C++ for GNU/Linux. Written in GTK/GNOME and written for GTK/GNOME,
it features many advanced programming tools and utilities. Besides
many other, it has project management, application wizards, onboard
interactive debugger, and a powerful source editor with source
browsing.

%description -l es.UTF-8
Anjuta es un entorno integrado de desarrollo para C y C++ para
GNU/Linux. Escrito en y para GTK/GNOME, proporciona muchas
herramientas de programación avanzadas. Entre otros, habilita
manejamiento de proyectos, wizards de aplicaciones, depurador
interactivo y un editador potente de código fuente que permite
hojearlo.

%description -l pl.UTF-8
Anjuta to wszechstronne zintegrowane środowisko programowania dla
języka C oraz C++. Zostało napisane z wykorzystaniem tandemu
GTK/GNOME, właśnie po to by go w takim otoczeniu używać. Między innymi
posiada zarządcę projektów, kreator aplikacji, wbudowany interaktywny
odpluskwiacz oraz edytor z możliwością przeglądania źródeł.

%description -l pt_BR.UTF-8
O Anjuta é um ambiente de desenvolvimento integrado (IDE) versátil
para as linguagens C e C++. Foi escrito para o GTK/GNOME e tem uma
série de características de programação avançadas. Basicamente é uma
interface gráfica com o usuário para um conjunto de utilitários de
linha de comando e ferramentas para programação para o Linux. Estas
são geralmente executadas em um console em modo texto e podem ser não
amigáveis.

%package -n libanjuta
Summary:	libanjuta library
Summary(pl.UTF-8):	Biblioteka libanjuta
Group:		X11/Libraries
Conflicts:	%{name} < 1:2.0.2-1

%description -n libanjuta
libanjuta library.

%description -n libanjuta -l pl.UTF-8
Biblioteka libanjuta.

%package -n libanjuta-devel
Summary:	Header files for libanjuta library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libanjuta
Group:		X11/Development/Libraries
Requires:	libanjuta-devel = %{epoch}:%{version}-%{release}
Requires:	libglade2-devel >= 1:2.6.2
Requires:	libgnomeui-devel >= 2.24.0

%description -n libanjuta-devel
Header files for libanjuta library.

%description -n libanjuta-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libanjuta.

%package -n libanjuta-apidocs
Summary:	libanjuta API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libanjuta
Group:		Documentation
Requires:	gtk-doc-common

%description -n libanjuta-apidocs
libanjuta API documentation.

%description -n libanjuta-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libanjuta.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-apr-config=%{_bindir}/apr-1-config \
	--with-apu-config=%{_bindir}/apu-1-config \
	--with-neon-config=%{_bindir}/neon-config \
	--with-omf-dir=%{_omf_dest_dir} \
	--disable-scrollkeeper \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	mimepngicondir=%{_iconsdir}/hicolor/48x48/mimetypes \
	mimesvgicondir=%{_iconsdir}/hicolor/scalable/mimetypes

# *.la not needed - *.so loaded through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/{anjuta,glade3/modules}/lib*.la

rm -rf $RPM_BUILD_ROOT%{_docdir}/anjuta

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_mime_database
%update_desktop_database
%gconf_schema_install anjuta-valgrind.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall anjuta-valgrind.schemas

%postun
%scrollkeeper_update_postun
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor

%post	-n libanjuta -p /sbin/ldconfig
%postun -n libanjuta -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FUTURE NEWS README ROADMAP THANKS TODO doc/ScintillaDoc.html
%attr(755,root,root) %{_bindir}/anjuta
%attr(755,root,root) %{_bindir}/anjuta_launcher
%attr(755,root,root) %{_bindir}/gbf-am-parse
%attr(755,root,root) %{_bindir}/gbf-mkfile-parse
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%{_libdir}/%{name}/*.plugin
%attr(755,root,root) %{_libdir}/glade3/modules/libgladeanjuta.so
%{_pixmapsdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/GBF
%{_datadir}/%{name}/build
%{_datadir}/%{name}/class-templates
%{_datadir}/%{name}/glade
%{_datadir}/%{name}/gtodo
%{_datadir}/%{name}/profiles
%{_datadir}/%{name}/project
%{_datadir}/%{name}/properties
%dir %{_datadir}/%{name}/tools
%attr(755,root,root) %{_datadir}/%{name}/tools/find-fixmes.pl
%attr(755,root,root) %{_datadir}/%{name}/tools/prepare-changelog.pl
%attr(755,root,root) %{_datadir}/%{name}/tools/translation-status.pl
%{_datadir}/%{name}/tools/tools-2.xml
%{_datadir}/%{name}/ui
%{_datadir}/%{name}/anjuta_project.template
%{_datadir}/%{name}/gdb.init
%{_datadir}/%{name}/languages.xml
%{_datadir}/%{name}/layout.xml
%{_datadir}/%{name}/macros.xml
%{_datadir}/%{name}/tables.sql
%{_datadir}/%{name}/welcome.txt
%{_datadir}/%{name}/AUTHORS
%{_datadir}/mime/packages/anjuta.xml
%{_datadir}/glade3/catalogs/anjuta-glade.xml
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/anjuta.1*
%{_mandir}/man1/anjuta_launcher.1*
%{_sysconfdir}/gconf/schemas/anjuta-valgrind.schemas
%{_iconsdir}/hicolor/*/*/*.*

%files -n libanjuta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libanjuta.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanjuta.so.0

%files -n libanjuta-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libanjuta.so
%{_libdir}/libanjuta.la
%{_includedir}/libanjuta-1.0
%{_pkgconfigdir}/libanjuta-1.0.pc

%files -n libanjuta-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libanjuta
