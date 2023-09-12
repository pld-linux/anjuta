Summary:	GNOME integrated development environment
Summary(es.UTF-8):	Entorno integrado de desarrollo (IDE) de GNOME
Summary(pl.UTF-8):	Zintegrowane środowisko programowania dla GNOME
Summary(pt_BR.UTF-8):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	3.34.0
Release:	4
Epoch:		1
License:	GPL v2+
Group:		X11/Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/anjuta/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	f81e3c9dbe406bb8635ea065e1602029
Patch0:		%{name}-desktop.patch
Patch1:		webkit-4.1.patch
Patch2:		python3-link.patch
URL:		https://wiki.gnome.org/Apps/Anjuta
BuildRequires:	autoconf >= 2.65
BuildRequires:	autogen
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	devhelp-devel >= 3.7.4
BuildRequires:	docbook-dtd412-xml
BuildRequires:	flex
BuildRequires:	gdk-pixbuf2-devel >= 2.0.0
BuildRequires:	gdl-devel >= 3.6.0
BuildRequires:	gettext-tools
BuildRequires:	gjs-devel
BuildRequires:	glade-devel >= 3.12.0
BuildRequires:	glib2-devel >= 1:2.34.0
BuildRequires:	glibc-misc
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	gtk-webkit4.1-devel
BuildRequires:	gtksourceview3-devel >= 3.2.0
BuildRequires:	intltool >= 0.40.1
BuildRequires:	libgda5-devel >= 5.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python3-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	sed >= 4.0
# require serf-based version (for simplicity)
BuildRequires:	subversion-devel >= 1.8.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.18.0
BuildRequires:	vte-devel >= 0.28.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	shared-mime-info
Requires(post,postun):	glib2 >= 1:2.34.0
Requires:	devhelp >= 3.7.4
# see libanjuta/anjuta-utils.c
# Requires:	xdg-terminal | gnome-terminal | nxterm | xolor-xterm | rxvt | xterm | dtterm
Requires:	glade >= 3.12.0
Requires:	glib2 >= 1:2.34.0
Requires:	gtksourceview3 >= 3.2.0
Requires:	hicolor-icon-theme
Requires:	libanjuta = %{epoch}:%{version}-%{release}
Requires:	libgda5-provider-sqlite >= 5.0.0
Requires:	perl-Locale-gettext
Requires:	pkgconfig >= 1:0.22
Requires:	subversion-libs >= 1.8.0
Requires:	vte >= 0.28.0
Suggests:	ctags
Obsoletes:	gnome-build
Obsoletes:	gnome-build-devel
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
Requires:	gdl >= 3.6.0
Requires:	glib2 >= 1:2.34.0
Requires:	gtk+3 >= 3.10.0
Requires:	libxml2 >= 1:2.6.26
Conflicts:	anjuta < 1:2.0.2-1

%description -n libanjuta
libanjuta library.

%description -n libanjuta -l pl.UTF-8
Biblioteka libanjuta.

%package -n libanjuta-devel
Summary:	Header files for libanjuta library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libanjuta
Group:		X11/Development/Libraries
Requires:	gdl-devel >= 3.6.0
Requires:	gtk+3-devel >= 3.10.0
Requires:	libanjuta = %{epoch}:%{version}-%{release}
Requires:	libxml2-devel >= 1:2.6.26

%description -n libanjuta-devel
Header files for libanjuta library.

%description -n libanjuta-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libanjuta.

%package -n libanjuta-apidocs
Summary:	libanjuta API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libanjuta
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description -n libanjuta-apidocs
libanjuta API documentation.

%description -n libanjuta-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libanjuta.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' plugins/tools/scripts/*.pl

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python3} \
	--with-html-dir=%{_gtkdocdir} \
	--enable-glade-catalog \
	--disable-neon \
	--disable-schemas-compile \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# *.la not needed - *.so loaded through libgmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/{anjuta,glade/modules}/lib*.la

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/anjuta
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libanjuta-3.la

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_mime_database
%update_desktop_database_postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	-n libanjuta -p /sbin/ldconfig
%postun -n libanjuta -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FUTURE NEWS README ROADMAP THANKS TODO doc/ScintillaDoc.html
%attr(755,root,root) %{_bindir}/anjuta
%attr(755,root,root) %{_bindir}/anjuta-launcher
%attr(755,root,root) %{_bindir}/anjuta-tags
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%attr(755,root,root) %{_libdir}/%{name}/anjuta-python-autocomplete.py
%{_libdir}/%{name}/*.plugin
%attr(755,root,root) %{_libdir}/glade/modules/libgladeanjuta.so
%{_datadir}/glade/catalogs/anjuta-glade.xml
%{_pixmapsdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/build
%{_datadir}/%{name}/class-templates
%{_datadir}/%{name}/glade
%{_datadir}/%{name}/profiles
%{_datadir}/%{name}/templates
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
%{_datadir}/%{name}/snippets-global-variables.xml
%{_datadir}/%{name}/snippets.anjuta-snippets
%{_datadir}/%{name}/sources.list
%{_datadir}/%{name}/tables.sql
%{_datadir}/%{name}/welcome.txt
%{_datadir}/%{name}/AUTHORS
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.cvs.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.document-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.file-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.snippets.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.starter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.symbol-db.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.tools.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.build.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.cpp.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.debug-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.git.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.indent-c.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.indent-python.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.js.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.message-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.parser-cxx.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.project-wizard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.python.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.run.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.sourceview.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.plugins.vala.gschema.xml
%{_datadir}/metainfo/anjuta.appdata.xml
%{_datadir}/mime/packages/anjuta.xml
%{_desktopdir}/anjuta.desktop
%{_iconsdir}/hicolor/*x*/apps/anjuta.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-anjuta.png
%{_iconsdir}/hicolor/scalable/apps/anjuta.svg
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-anjuta.svg
%{_iconsdir}/hicolor/symbolic/apps/anjuta-symbolic.svg
%{_mandir}/man1/anjuta.1*
%{_mandir}/man1/anjuta-launcher.1*

%files -n libanjuta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libanjuta-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanjuta-3.so.0
%{_libdir}/girepository-1.0/Anjuta-3.0.typelib
%{_libdir}/girepository-1.0/IAnjuta-3.0.typelib

%files -n libanjuta-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libanjuta-3.so
%{_includedir}/libanjuta-3.0
%{_pkgconfigdir}/libanjuta-3.0.pc
%{_datadir}/gir-1.0/Anjuta-3.0.gir
%{_datadir}/gir-1.0/IAnjuta-3.0.gir

%files -n libanjuta-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libanjuta
