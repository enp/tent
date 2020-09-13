Name: example
Version: %{example_version}
Release: %{example_release}
Summary: Example Groovy Application
Group: System/Utils

Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License: ASL 2.0
Source0: example-%{example_base_version}.tar.gz
Source1: bigtop.bom

%description 
Example Groovy Application

%prep
%setup

%build
gradle jar

%install
%__rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/%{name}
install build/libs/* ${RPM_BUILD_ROOT}/usr/lib/%{name}/

%files
%defattr(-,root,root,644)
/usr/lib/%{name}
