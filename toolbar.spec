# TODO:
# javadoc package
Summary:	An extension of JToolBar which adds support for ToolButton
Name:		toolbar
Version:	0.4
Release:	0.1
License:	Apache License
# no idea how to compile it...
# Source0:	http://toolbar.tigris.org/files/documents/869/10303/ToolBar-%{version}-src.zip
Source0:	http://toolbar.tigris.org/files/documents/869/9314/ToolBar-%{version}-bin.zip
# Source0-md5:	76606eb81d2d59c9e3b57d1914fadcc6
Url:		http://toolbar.tigris.org/
Requires:	jakarta-log4j
#BuildRequires:	jakarta-ant
#BuildRequires:	jakarta-commons-logging
Group:		Development/Languages/Java
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ToolBar was originally designed for the ArgoUML project and has now
been broken out to allow reuse by other swing based applications.

%package	doc
Summary:	Javadoc for %{name}
Group:		Documentation

%description	doc
Javadoc for %{name}.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/*
