%define		snap	20030405

Summary:	Gnome integrated development environment
Summary(pl):	Zintegrowane ¶rodowisko programowania dla Gnome
Summary(pt_BR):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	1.2.0
Release:	0.%{snap}.1
License:	GPL
Group:		Development/Tools
#Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.bz2
Patch0:		%{name}-am.patch
Patch1:		%{name}-gettext.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	libzvt-devel >= 2.0.0
BuildRequires: 	ncurses-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	vte-devel >= 0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anjuta is a very versatile integrated development environment for C
and C++ GNU/Linux. Written in GTK/Gnome and written for GTK/Gnome, it
features many advanced programming tools and utilities. Besides many
other, it has project management, application wizards, onboard
interactive debugger, and a powerful source editor with source
browsing.

%description -l pl
Anjuta to wszechstronne zintegrowane ¶rodowisko programowania dla
jêzyka C oraz C++. Zosta³o napisane z wykorzystaniem tandemu
GTK/Gnome, w³a¶nie po to by go w takim otoczeniu u¿ywaæ. Miêdzy innymi
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

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions"
#rm -f missing
#%%{__gettextize}
#intltoolize
#%%{__libtoolize}
#%%{__aclocal} -I /usr/share/aclocal/gnome2-macros
#%%{__autoheader}
#%%{__autoconf}
#%%{__automake}
./autogen.sh
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_datadir}/applications

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS COPYING 
%doc FUTURE INSTALL doc/ScintillaDoc.html
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/anjuta
%attr(755,root,root) %{_libdir}/anjuta/lib*.so*
%{_libdir}/anjuta/lib*.la
%{_pixmapsdir}/anjuta
%{_datadir}/anjuta
%{_datadir}/applications/*
%{_datadir}/mime-info/*
%{_datadir}/mimelnk/application/*
%{_mandir}/man1/*
