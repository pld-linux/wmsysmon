Summary:	Window Maker/AfterStep memory/swap/IO/uptime/ints monitor
Summary(pl):	Monitor systemu dla WindowMakera/AfterStepa
Name:		wmsysmon
Version:	0.3
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Source1:	wmsysmon.desktop
Icon:		wmsysmon.gif
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
ExclusiveArch:	%{ix86} alpha
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
wmsysmon monitors memory, swap, disk I/O, uptime, interrupts.  Window
Maker and AfterStep dockable, but should run (I think) without them
(e.g., swallowable by fvwm).

%description -l pl
wmsysmon jest dokowalnym apletem dla WindowMakera i AfterStepa, 
monitoruj±cym wykorzystanie zasobów systemowych.

%prep
%setup -q -n %{name}.app

%build
make -C wmsysmon FLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/usr/X11R6/share/applnk/DockApplets}

%ifnarch alpha
install -s wmsysmon/wmsysmon       $RPM_BUILD_ROOT%{_bindir}
%endif
%ifarch alpha
install -s wmsysmon/wmsysmon-alpha $RPM_BUILD_ROOT%{_bindir}/wmsysmon
%endif

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets


gzip -9nf BUGS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/wmsysmon

/usr/X11R6/share/applnk/DockApplets/wmsysmon.desktop
