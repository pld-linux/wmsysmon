Summary:	Window Maker/AfterStep memory/swap/IO/uptime/ints monitor
Summary(pl):	Monitor systemu dla WindowMakera/AfterStepa
Name:		wmsysmon
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Source1:	wmsysmon.desktop
Icon:		wmsysmon.gif
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
ExclusiveArch:	%{ix86} alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
wmsysmon monitors memory, swap, disk I/O, uptime, interrupts.  Window
Maker and AfterStep dockable, but should run (I think) without them
(e.g., swallowable by fvwm).

%description -l pl
wmsysmon jest dokowalnym apletem dla WindowMakera i AfterStepa, 
monitoruj±cym wykorzystanie zasobów systemowych.

%prep
%setup -q

%build
%ifarch alpha
make -C src CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include -DHI_INTS"
%endif
%ifarch %{ix86}
make -C src CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

%ifarch alpha
install -s src/wmsysmon-alpha $RPM_BUILD_ROOT%{_bindir}/wmsysmon
%endif
%ifarch %{ix86}
install -s src/wmsysmon       $RPM_BUILD_ROOT%{_bindir}
%endif

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz
%attr(755,root,root) %{_bindir}/wmsysmon

%{_applnkdir}/DockApplets/wmsysmon.desktop
