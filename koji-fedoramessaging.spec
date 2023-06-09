Name:           koji-fedoramessaging
Version:        1.1.1
Release:        1%{?dist}
Summary:        Enable Koji to send Fedora Messaging messages
Group:          Applications/System
License:        GPLv3
URL:            https://github.com/fedora-infra/koji-fedoramessaging
Source0:        %{url}/archive/%{version}/koji-fedoramessaging-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python
BuildRequires:  python3-devel
BuildRequires:  python-setuptools

Requires:   python3-koji-hub
Requires:   python3-koji-fedoramessaging-messages

%description
Enable Koji to send Fedora Messaging messages

%prep
%setup -q

%build

%install
%{__install} -d $RPM_BUILD_ROOT%{_prefix}/lib/koji-hub-plugins
%{__install} -p -m 0644 koji-fedoramessaging/koji-fedoramessaging.py $RPM_BUILD_ROOT%{_prefix}/lib/koji-hub-plugins/koji-fedoramessaging.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_prefix}/lib/koji-hub-plugins

%changelog
* Fri Jun 09 2023 Aurelien Bompard <abompard@fedoraproject.org> - 1.1.1-1
- Don't call get_message_body() needlessly
* Fri Jun 09 2023 Aurelien Bompard <abompard@fedoraproject.org> - 1.1.0-1
- Add more data in the task and build state change messages
* Thu Feb 09 2023 Ryan Lerch <rlerch@redhat.com> - 1.0.1-1
- Tweak logging so kojihub logger can find the logs
* Tue Feb 07 2023 Ryan Lerch <rlerch@redhat.com> - 1.0-1
- Initial Release
