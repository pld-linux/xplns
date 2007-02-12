Summary:	Desktop astronomy simulation
Summary(pl.UTF-8):   Symulacja nieba
Name:		xplns
Version:	3.3.1
Release:	1
License:	unknown
Group:		X11/Applications/Science
Source0:	http://www.astroarts.jp/products/xplns/binaries/%{name}-%{version}-1glibc23.i386.rpm
# NoSource0-md5:	fc9bd729083be78a0f130e5bc8661163
NoSource:	0
Source1:	http://www.astroarts.jp/products/xplns/binaries/%{name}-cat-%{version}-1.i386.rpm
# NoSource1-md5:	28133ae623b0995016c312bcab854d9a
NoSource:	1
Source2:	http://www.astroarts.jp/products/xplns/binaries/%{name}-elm-%{version}-1.i386.rpm
# NoSource2-md5:	ed3f4d5d1a4157f5fc0621da165d10e3
NoSource:	2
Source3:	http://www.astroarts.jp/products/xplns/binaries/%{name}-img-%{version}-1.i386.rpm
# NoSource3-md5:	25a59654c6298a9c964539c444a48709
NoSource:	3
Source4:	%{name}.desktop
URL:		http://www.astroarts.com/products/xplns/index.html
BuildRequires:	cpio
BuildRequires:	sed >= 4.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
Desktop astronomy simulation.

%description -l pl.UTF-8
Symulacja nieba.

%prep
%setup -q -c -T
rpm2cpio %{SOURCE0} | cpio -dimu
rpm2cpio %{SOURCE1} | cpio -dimu
rpm2cpio %{SOURCE2} | cpio -dimu
rpm2cpio %{SOURCE3} | cpio -dimu

find .  -name '*.ja' -print0 | xargs -0 -r -l512 rm -f
sed -i "s#/usr/local/share#%{_datadir}#g" usr/X11R6/lib/X11/app-defaults/XPlns

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_appdefsdir}}

cp -a usr/local/bin/xplns $RPM_BUILD_ROOT%{_bindir}
cp -a usr/local/share/xplns $RPM_BUILD_ROOT%{_datadir}
cp usr/share/pixmaps/* $RPM_BUILD_ROOT%{_pixmapsdir}
cp usr/X11R6/lib/X11/app-defaults/XPlns $RPM_BUILD_ROOT%{_appdefsdir}

install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc usr/share/doc/xplns-%{version}/README
%attr(755,root,root) %{_bindir}/*
%{_appdefsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
