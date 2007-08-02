Summary:	GNOME integrated development environment
Summary(es.UTF-8):	Entorno integrado de desarrollo (IDE) de GNOME
Summary(pl.UTF-8):	Zintegrowane środowisko programowania dla GNOME
Summary(pt_BR.UTF-8):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	2.2.0
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/anjuta/%{name}-%{version}.tar.bz2
# Source0-md5:	c96861a6143bb11bf553404ac1e279ad
#Patch0: %{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-create_global_tags.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.12.0
BuildRequires:	ORBit2-devel >= 1:2.12.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	autogen
BuildRequires:	automake
BuildRequires:	binutils-devel
BuildRequires:	devhelp-devel >= 0.13
BuildRequires:	gdl-devel >= 0.7.3
BuildRequires:	gettext-devel
BuildRequires:	gnome-build-devel >= 0.1.4
BuildRequires:	gnome-doc-utils
BuildRequires:	graphviz-devel >= 2.6.0
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	gtksourceview-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgladeui-devel >= 3.0.2
BuildRequires:	libgnomeprintui-devel >= 2.12.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	neon-devel >= 0.24.5
BuildRequires:	pcre-devel >= 3.9
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	subversion-devel >= 1.0.2
BuildRequires:	vte-devel >= 0.14.0
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
# Requires:	gnome-terminal
Requires:	libanjuta = %{epoch}:%{version}-%{release}
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
Group:		Development/Libraries
Conflicts:	%{name} < 1:2.0.2-1

%description -n libanjuta
libanjuta library.

%description -n libanjuta -l pl.UTF-8
Biblioteka libanjuta.

%package -n libanjuta-devel
Summary:	Header files for libanjuta library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libanjuta
Group:		Development/Libraries
Requires:	libanjuta-devel = %{epoch}:%{version}-%{release}

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
#%patch0 -p1 NEEDS checking
%patch1 -p1
%patch2 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_desktopdir} \
	mimepngicondir=%{_iconsdir}/hicolor/48x48/mimetypes \
	mimesvgicondir=%{_iconsdir}/hicolor/scalable/mimetypes

mv -f $RPM_BUILD_ROOT%{_datadir}/anjuta/scripts/anjuta-tags $RPM_BUILD_ROOT%{_bindir}

# *.la not needed - *.so loaded through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/anjuta/lib*.la

rm -rf $RPM_BUILD_ROOT%{_docdir}/anjuta

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%update_mime_database
%gconf_schema_install anjuta-valgrind.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall anjuta-valgrind.schemas

%postun
%scrollkeeper_update_postun
%update_mime_database
%update_icon_cache hicolor

%post	-n libanjuta -p /sbin/ldconfig
%postun -n libanjuta -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FUTURE NEWS README ROADMAP THANKS TODO doc/ScintillaDoc.html
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%{_libdir}/%{name}/*.plugin
%{_pixmapsdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/build
%{_datadir}/%{name}/class-templates
%{_datadir}/%{name}/glade
%{_datadir}/%{name}/gtodo
%{_datadir}/%{name}/profiles
%{_datadir}/%{name}/project
%{_datadir}/%{name}/properties
%dir %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/scripts/create_global_tags.sh
%dir %{_datadir}/%{name}/tools
%attr(755,root,root) %{_datadir}/%{name}/tools/find-fixmes.pl
%attr(755,root,root) %{_datadir}/%{name}/tools/prepare-changelog.pl
%attr(755,root,root) %{_datadir}/%{name}/tools/translation-status.pl
%{_datadir}/%{name}/tools/tools-2.xml
%{_datadir}/%{name}/ui
%{_datadir}/%{name}/anjuta_project.template
%{_datadir}/%{name}/gdb.init
%{_datadir}/%{name}/indent_test.c
%{_datadir}/%{name}/layout.xml
%{_datadir}/%{name}/macros.xml
%{_datadir}/%{name}/welcome.txt
%{_datadir}/mime/packages/%{name}.xml
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/anjuta.1*
%{_mandir}/man1/anjuta_launcher.1*
%{_omf_dest_dir}/%{name}-manual
%{_sysconfdir}/gconf/schemas/*.*
%{_iconsdir}/hicolor/*/*/*.*

%files -n libanjuta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*

%files -n libanjuta-devel
%defattr(644,root,root,755)
%{_includedir}/libanjuta-*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc

%files -n libanjuta-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libanjuta
