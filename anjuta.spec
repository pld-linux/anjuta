Summary:	GNOME integrated development environment
Summary(es.UTF-8):	Entorno integrado de desarrollo (IDE) de GNOME
Summary(pl.UTF-8):	Zintegrowane środowisko programowania dla GNOME
Summary(pt_BR.UTF-8):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	3.2.2
Release:	2
Epoch:		1
License:	GPL v2+
Group:		X11/Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/anjuta/3.2/%{name}-%{version}.tar.bz2
# Source0-md5:	1c77beea7b81e0bc19f90d9b0a4e4ec2
URL:		http://projects.gnome.org/anjuta/
BuildRequires:	autoconf >= 2.65
BuildRequires:	autogen
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	devhelp-devel >= 3.2.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	flex
BuildRequires:	gdl-devel >= 3.0.0
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	glade-devel >= 3.10.0
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	glibc-misc
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.18.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	graphviz-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.2.0
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	gtk-webkit3-devel
BuildRequires:	gtksourceview3-devel >= 3.2.0
BuildRequires:	intltool >= 0.40.1
BuildRequires:	libgda4-devel >= 4.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel
BuildRequires:	neon-devel >= 0.28.2
BuildRequires:	openldap-devel
BuildRequires:	pakchois-devel
BuildRequires:	perl-Locale-gettext
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	scrollkeeper
BuildRequires:	subversion-devel >= 1.5.0
BuildRequires:	vala >= 2:0.14.0
BuildRequires:	vte-devel >= 0.28.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires(post,postun):	glib2 >= 1:2.26.0
# Requires:	gnome-terminal
Requires:	glade >= 3.10.0
Requires:	glib2 >= 1:2.28.0
Requires:	gtksourceview3 >= 3.0.0
Requires:	hicolor-icon-theme
Requires:	libanjuta = %{epoch}:%{version}-%{release}
Requires:	libgda4-provider-sqlite >= 4.2.0
Requires:	perl-Locale-gettext
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
Requires:	gdl-devel >= 3.0.0
Requires:	gtk+3-devel >= 3.0.0
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

%description -n libanjuta-apidocs
libanjuta API documentation.

%description -n libanjuta-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libanjuta.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-omf-dir=%{_omf_dest_dir} \
	--disable-schemas-compile \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mimepngicondir=%{_iconsdir}/hicolor/48x48/mimetypes \
	mimesvgicondir=%{_iconsdir}/hicolor/scalable/mimetypes

# *.la not needed - *.so loaded through libgmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/{anjuta,glade/modules}/lib*.la

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/anjuta
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libanjuta-3.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_mime_database
%update_desktop_database
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%scrollkeeper_update_postun
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
%{_datadir}/%{name}/project
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
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.build.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.code-analyzer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.cpp.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.cvs.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.debug-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.document-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.file-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.js.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.message-manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.python.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.run.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.snippets.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.sourceview.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.symbol-db.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.anjuta.tools.gschema.xml
%{_datadir}/mime/packages/anjuta.xml
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/anjuta.1*
%{_mandir}/man1/anjuta-launcher.1*
%{_iconsdir}/hicolor/*/*/*.*

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
