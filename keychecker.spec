Name:           keychecker
Version:        0.1
Release:        1%{?dist}
Summary:        Generate list of installed packages sorted by GPG key

Group:          Applications/System
License:        GPLv2+
URL:            https://fedorahosted.org/keychecker
Source0:        https://fedorahosted,org/released/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch


%description
Separately list rpm's based on the GPG key they were signed with

%prep
%setup -q


%build

%install
rm -rf $RPM_BUILD_ROOT
install -dm 0755 $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 key_checker.py $RPM_BUILD_ROOT/%{_bindir}/keychecker

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/keychecker
%doc README LICENSE

%changelog
* Sun Jul 26 2009 Jon Stanley <jonstanley@gmail.com> - 0.1-1
- Initial package
