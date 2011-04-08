Summary:	GNOME integrated development environment
Summary(es.UTF-8):	Entorno integrado de desarrollo (IDE) de GNOME
Summary(pl.UTF-8):	Zintegrowane środowisko programowania dla GNOME
Summary(pt_BR.UTF-8):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	3.0.0.0
Release:	0.1
Epoch:		1
License:	GPL v2+
Group:		X11/Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/anjuta/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	ae7b5b9e89f1251d7c1e2109671ccd33
URL:		http://projects.gnome.org/anjuta/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	autogen
BuildRequires:	automake >= 1:1.9
BuildRequires:	devhelp-devel >= 0.22
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdl-devel >= 3.0.0
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	glibc-misc
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	graphviz-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	gtk-webkit-devel
BuildRequires:	gtksourceview3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgda4-devel >= 4.2.0
BuildRequires:	libgladeui-devel >= 3.6.7
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.0.0
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel
BuildRequires:	neon-devel >= 0.28.2
BuildRequires:	perl-Locale-gettext
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	subversion-devel >= 1.5.0
BuildRequires:	vala >= 0.12.0
BuildRequires:	vte-devel >= 0.28.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
# Requires:	gnome-terminal
Requires:	glib2 >= 1:2.26.0
Requires:	gtksourceview2 >= 2.10.0
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
Requires:	GConf2-devel >= 2.26.0
Requires:	gtk+2-devel >= 2:2.20.0
Requires:	libanjuta = %{epoch}:%{version}-%{release}

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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-omf-dir=%{_omf_dest_dir} \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--disable-static

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	mimepngicondir=%{_iconsdir}/hicolor/48x48/mimetypes \
	mimesvgicondir=%{_iconsdir}/hicolor/scalable/mimetypes

# *.la not needed - *.so loaded through libgmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/{anjuta,glade3/modules}/lib*.la

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/anjuta
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libanjuta.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_mime_database
%update_desktop_database
%gconf_schema_install anjuta-build-basic-autotools-plugin.schemas
%gconf_schema_install anjuta-cvs-plugin.schemas
%gconf_schema_install anjuta-document-manager.schemas
%gconf_schema_install anjuta-debug-manager.schemas
%gconf_schema_install anjuta-editor-sourceview.schemas
%gconf_schema_install anjuta-language-cpp-java.schemas
%gconf_schema_install anjuta-message-manager-plugin.schemas
%gconf_schema_install preferences.schemas
%gconf_schema_install anjuta-symbol-db.schemas
%gconf_schema_install anjuta-terminal-plugin.schemas
%gconf_schema_install file-manager.schemas
%gconf_schema_install python-plugin-properties.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall anjuta-build-basic-autotools-plugin.schemas
%gconf_schema_uninstall anjuta-cvs-plugin.schemas
%gconf_schema_uninstall anjuta-document-manager.schemas
%gconf_schema_uninstall anjuta-debug-manager.schemas
%gconf_schema_uninstall anjuta-editor-sourceview.schemas
%gconf_schema_uninstall anjuta-language-cpp-java.schemas
%gconf_schema_uninstall anjuta-message-manager-plugin.schemas
%gconf_schema_uninstall preferences.schemas
%gconf_schema_uninstall anjuta-symbol-db.schemas
%gconf_schema_uninstall anjuta-terminal-plugin.schemas
%gconf_schema_uninstall file-manager.schemas
%gconf_schema_uninstall python-plugin-properties.schemas

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
%attr(755,root,root) %{_bindir}/anjuta-launcher
%attr(755,root,root) %{_bindir}/anjuta-tags
%attr(755,root,root) %{_bindir}/gbf-am-parse
%attr(755,root,root) %{_bindir}/gbf-mkfile-parse
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%attr(755,root,root) %{_libdir}/%{name}/anjuta-python-autocomplete.py
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
%{_datadir}/mime/packages/anjuta.xml
%{_datadir}/glade3/catalogs/anjuta-glade.xml
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/anjuta.1*
%{_mandir}/man1/anjuta-launcher.1*
%{_sysconfdir}/gconf/schemas/anjuta-build-basic-autotools-plugin.schemas
%{_sysconfdir}/gconf/schemas/anjuta-cvs-plugin.schemas
%{_sysconfdir}/gconf/schemas/anjuta-document-manager.schemas
%{_sysconfdir}/gconf/schemas/anjuta-debug-manager.schemas
%{_sysconfdir}/gconf/schemas/anjuta-editor-sourceview.schemas
%{_sysconfdir}/gconf/schemas/anjuta-language-cpp-java.schemas
%{_sysconfdir}/gconf/schemas/anjuta-message-manager-plugin.schemas
%{_sysconfdir}/gconf/schemas/anjuta-symbol-db.schemas
%{_sysconfdir}/gconf/schemas/anjuta-terminal-plugin.schemas
%{_sysconfdir}/gconf/schemas/file-manager.schemas
%{_sysconfdir}/gconf/schemas/preferences.schemas
%{_sysconfdir}/gconf/schemas/python-plugin-properties.schemas
%{_iconsdir}/hicolor/*/*/*.*

%files -n libanjuta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libanjuta.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanjuta.so.0
%attr(755,root,root) %{_libdir}/libanjuta-foocanvas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libanjuta-foocanvas.so.0
%{_libdir}/girepository-1.0/Anjuta-1.0.typelib
%{_libdir}/girepository-1.0/IAnjuta-1.0.typelib

%files -n libanjuta-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libanjuta.so
%attr(755,root,root) %{_libdir}/libanjuta-foocanvas.so
%{_libdir}/libanjuta-foocanvas.la
%{_includedir}/libanjuta-1.0
%{_pkgconfigdir}/libanjuta-1.0.pc
%{_datadir}/gir-1.0/Anjuta-1.0.gir
%{_datadir}/gir-1.0/IAnjuta-1.0.gir

%files -n libanjuta-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libanjuta
