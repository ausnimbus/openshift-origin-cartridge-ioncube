%global cartridgedir %{_libexecdir}/openshift/cartridges/ioncube

Summary:       ionCube loader support for OpenShift
Name:          openshift-origin-cartridge-ioncube
Version:       1.0
Release:       1%{?dist}
Group:         Applications/Internet
License:       ASL 2.0
URL:           https://www.ausnimbus.com.au
Source0:       https://github.com/andrewklau/openshift-origin-ioncube-cartridge/archive/master.zip
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Provides:      openshift-origin-cartridge-ioncube = 2.0.0
BuildArch:     noarch

%description
This cartridge is an embeded cartridge to auto load the ionCube loaders to a PHP application. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__mkdir -p %{buildroot}%{httpdconfdir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}/metadata
%{cartridgedir}/usr
%{cartridgedir}/versions
%{cartridgedir}/env
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Tue Aug 30 2014 Andrew Lau <andrew@andrewklau.com> 1.0
- Initial version
