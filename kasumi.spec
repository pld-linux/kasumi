Summary:	An anthy dictionary management tool
Name:		kasumi
Version:	2.5
Release:	0.1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://jaist.dl.sourceforge.jp/kasumi/41436/%{name}-%{version}.tar.gz
# Source0-md5:	f49d010cf1fa5672b4515502b961b8c8
URL:		http://kasumi.sourceforge.jp/
BuildRequires:	anthy-devel
BuildRequires:	gtk+2-devel
Requires:	anthy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kasumi is a dictionary management tool for Anthy.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p"

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/kasumi
%{_mandir}/man1/kasumi.1*
%{_pixmapsdir}/kasumi.png
%{_desktopdir}/kasumi.desktop
