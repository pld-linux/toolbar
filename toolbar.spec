# TODO:
# javadoc package
Summary:	An extension of JToolBar which adds support for ToolButton
Summary(pl.UTF-8):	Rozszerzenie JToolBara dodające obsługę ToolButtona
Name:		toolbar
Version:	0.4
Release:	0.1
License:	Apache License
Group:		Development/Languages/Java
# no idea how to compile it...
# Source0:	http://toolbar.tigris.org/files/documents/869/10303/ToolBar-%{version}-src.zip
Source0:	http://toolbar.tigris.org/files/documents/869/9314/ToolBar-%{version}-bin.zip
# Source0-md5:	76606eb81d2d59c9e3b57d1914fadcc6
URL:		http://toolbar.tigris.org/
Requires:	jakarta-log4j
#BuildRequires:	ant
#BuildRequires:	jakarta-commons-logging
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ToolBar was originally designed for the ArgoUML project and has now
been broken out to allow reuse by other Swing based applications.

%description -l pl.UTF-8
ToolBar oryginalnie został zaprojektowany dla projektu ArgoUML, a
później został wydzielony do używania także w innych aplikacjach
opartych na Swingu.

%package doc
Summary:	Javadoc for ToolBar
Summary(pl.UTF-8):	Dokumentacja Javadoc dla ToolBara
Group:		Documentation

%description doc
Javadoc for ToolBar.

%description doc -l pl.UTF-8
Dokumentacja Javadoc dla ToolBara.

%prep
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
