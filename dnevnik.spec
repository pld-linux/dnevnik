Summary:	Simple diary
Summary(pl):	Prosty pamiêtnik
Name:		dnevnik
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.devbase.net/dnevnik/%{name}.tar.gz
# Source0-md5:	1ceb91aa6cd8b7aad673bc04c5144247
URL:		http://www.devbase.net/dnevnik/
BuildRequires:	qmake
BuildRequires:	qt-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moj Dnevnik is a simple diary that is written in C++ using the Qt
library, so it works on Linux, *BSD, Unix, Windows, and Mac. It holds
all data in simple text file and the GUI is in Serbian.

%description -l pl
Moj Dnevnik jest prostym pamiêtnikiem napisanym w C++ z u¿yciem
biblioteki Qt, zatem dzia³a pod Linuksem, *BSD, Uniksem, Windowsem
oraz Makiem. Wszystkie dane trzyma w prostym pliku tekstowym, a GUI
jest po serbsku.

%prep
%setup -q -n %{name}

sed -i -e 's/^\(CONFIG.*\)$/\1 thread/' dnevnik.pro

%build
qmake \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}"

%{__make} \
	QTDIR=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dnevnik $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
