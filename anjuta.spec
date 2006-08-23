# TODO:
# - subversion plugin
# - post/preun mime registration
#
Summary:	GNOME integrated development environment
Summary(pl):	Zintegrowane ¶rodowisko programowania dla GNOME
Summary(es):	Entorno integrado de desarrollo (IDE) de GNOME
Summary(pt_BR):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	2.0.2
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/anjuta/%{name}-%{version}.tar.gz
# Source0-md5:	e0d1e216da809df32816d233d7c55165
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-build_fixes.patch
Patch3:		%{name}-as_needed.patch
Patch4:		%{name}-flags.patch
Patch5:		%{name}-glade_fix.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	ORBit2-devel >= 1:2.14.2
BuildRequires:	autoconf >= 2.52
BuildRequires:	autogen-devel
BuildRequires:	automake
BuildRequires:	devhelp-devel >= 0.12
BuildRequires:	gd-devel
BuildRequires:	gdl-devel >= 0.6.1
BuildRequires:	gnome-build-devel >= 0.1.3
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	graphviz-devel >= 2.2.1
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	gtksourceview-devel >= 0.7.2
BuildRequires:	guile-devel >= 1.6.7
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgladeui-devel >= 3.0.1
BuildRequires:	libgnomeprintui-devel >= 2.12.1
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel >= 1.1.17
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel >= 3.9
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
# requires old subversion version to build
#BuildRequires:	subversion-devel >= 1.0.2
BuildRequires:	scrollkeeper
BuildRequires:	vte-devel >= 0.13.5
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	gtk+2 >= 2.10.1
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anjuta is a very versatile integrated development environment for C
and C++ for GNU/Linux. Written in GTK/GNOME and written for GTK/GNOME,
it features many advanced programming tools and utilities. Besides
many other, it has project management, application wizards, onboard
interactive debugger, and a powerful source editor with source
browsing.

%description -l es
Anjuta es un entorno integrado de desarrollo para C y C++ para
GNU/Linux. Escrito en y para GTK/GNOME, proporciona muchas
herramientas de programación avanzadas. Entre otros, habilita
manejamiento de proyectos, wizards de aplicaciones, depurador
interactivo y un editador potente de código fuente que permite
hojearlo.

%description -l pl
Anjuta to wszechstronne zintegrowane ¶rodowisko programowania dla
jêzyka C oraz C++. Zosta³o napisane z wykorzystaniem tandemu
GTK/GNOME, w³a¶nie po to by go w takim otoczeniu u¿ywaæ. Miêdzy innymi
posiada zarz±dcê projektów, kreator aplikacji, wbudowany interaktywny
odpluskwiacz oraz edytor z mo¿liwo¶ci± przegl±dania ¼róde³.

%description -l pt_BR
O Anjuta é um ambiente de desenvolvimento integrado (IDE) versátil
para as linguagens C e C++. Foi escrito para o GTK/GNOME e tem uma
série de características de programação avançadas. Basicamente é uma
interface gráfica com o usuário para um conjunto de utilitários de
linha de comando e ferramentas para programação para o Linux. Estas
são geralmente executadas em um console em modo texto e podem ser não
amigáveis.

%package libs
Summary:	Anjuta shared libraries
Summary(pl):	Bibloteki wspó³dzielone Anjuta
Group:		Development/Libraries

%description libs
Anjuta shared libraries.

%description libs -l pl
Bibloteki wspó³dzielone Anjuta.

%package devel
Summary:	Anjuta header files
Summary(pl):	Pliki nag³ówkowe Anjuta
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Anjuta header files.

%description devel -l pl
Pliki nag³ówkowe Anjuta.

%package static
Summary:	Anjuta static library
Summary(pl):	Biblioteka statyczna Anjuta
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Anjuta static library.

%description static -l pl
Biblioteka statyczna Anjuta.

%package apidocs
Summary:	libanjuta API documentation
Summary(pl):	Dokumentacja API libanjuta
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libanjuta API documentation.

%description apidocs -l pl
Dokumentacja API libanjuta.

%prep
%setup -q
# update me!
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

sed -i -e 's|^(packageplugindir=)lib/|$1%{_lib}/|' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-plugin-subversion \
	--disable-schemas-install \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mimeicondir="%{_iconsdir}/hicolor/48x48/mimetypes"

# *.la not needed - *.so loaded through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/anjuta/lib*.{a,la}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install anjuta-valgrind.schemas
%scrollkeeper_update_post
%update_mime_database
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall anjuta-valgrind.schemas

%postun
%scrollkeeper_update_post
%update_mime_database
%update_icon_cache hicolor

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FUTURE MAINTAINERS NEWS README ROADMAP TODO doc/ScintillaDoc.html
%{_sysconfdir}/gconf/schemas/anjuta-valgrind.schemas
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libanjuta-*.so*
%{_libdir}/%{name}/*.plugin
%{_datadir}/%{name}
%{_datadir}/mime/packages/*.xml
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/hicolor/*/mimetypes/*
%{_pixmapsdir}/%{name}
%{_mandir}/man1/*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/*-C.omf

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libanjuta-1.0
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libanjuta
