# Upstream hasn't ported to python3 yet
# https://github.com/psychopy/psychopy/issues/997
%global with_python3 0
%global modname psychopy
%global commit 217599b4f5ad74ef42888215652363e83a94dca6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-psychopy
Version:        1.83.01
Release:        1.git%{shortcommit}%{?dist}
Summary:        Psychophysics toolkit for Python
License:        GPLv3+
URL:            http://www.psychopy.org/
Source0:        https://github.com/psychopy/psychopy/archive/%{commit}/%{modname}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
PsychoPy uses OpenGL and Python to create a toolkit
for running psychology/neuroscience/psychophysics 
experiments.

%prep
%autosetup -n %{modname}-%{commit}

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel

%description -n python2-%{modname}
PsychoPy uses OpenGL and Python to create a toolkit
for running psychology/neuroscience/psychophysics
experiments.

Python 2 version.

%if %{with_python3}
%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel

%description -n python3-%{modname}
PsychoPy uses OpenGL and Python to create a toolkit
for running psychology/neuroscience/psychophysics
experiments.

Python 3 version.
%endif

%build
%py2_build

%if %{with_python3}
  %py3_build
%endif

%install
%py2_install

%if %{with_python3}
  %py3_install
%endif

%files -n python2-%{modname}
%license %{modname}/LICENSE.txt
%doc README.md
%{_bindir}/psychopyApp.py
%{_bindir}/psychopy_post_inst.py
%{python2_sitelib}/%{modname}*
%{python2_sitelib}/PsychoPy-1.83.1-py2.7.egg-info/*

%if %{with_python3}
%files -n python3-%{modname}
%license %{modname}/LICENSE.txt
%doc README.md
%{_bindir}/psychopyApp.py
%{_bindir}/psychopy_post_inst.py
%{python2_sitelib}/%{modname}*
%{python2_sitelib}/PsychoPy-1.83.1-py2.7.egg-info/*
%endif


%changelog
* Sat Nov  7 2015 Alves Adrian <aalves@gmail.com> - 1.83.01-1
- Initial package
