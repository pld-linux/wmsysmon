Summary:	Window Maker/AfterStep memory/swap/IO/uptime/ints monitor
Summary(pl):	Monitor systemu dla WindowMakera/AfterStepa
Name:		wmsysmon
Version:	0.7.6
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.gnugeneration.com/software/wmsysmon/src/%{name}-%{version}.tar.gz
# Source0-md5:	1f8b7872c20fa6af1c89265ea2126c31
Source1:	%{name}.desktop
Icon:		wmsysmon.gif
BuildRequires:	XFree86-devel
URL:		http://www.gnugeneration.com/software/wmsysmon/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
wmsysmon monitors memory, swap, disk I/O, uptime, interrupts. Window
Maker and AfterStep dockable, but should run (I think) without them
(e.g., swallowable by fvwm).

%description -l pl
wmsysmon jest dokowalnym apletem dla WindowMakera i AfterStepa,
monitoruj±cym wykorzystanie zasobów systemowych.

%prep
%setup -q

%build
%{__make} -C src \
	CC=%{__cc} \
%ifarch %{ix86}	
	CFLAGS="%{rpmcflags} -I%{_includedir}"
%else
	CFLAGS="%{rpmcflags} -I%{_includedir} -DHI_INTS"
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install src/wmsysmon       $RPM_BUILD_ROOT%{_bindir}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/wmsysmon

#%%{_applnkdir}/DockApplets/wmsysmon.desktop
