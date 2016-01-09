Name:           ros-indigo-ecl-converters
Version:        0.61.8
Release:        0%{?dist}
Summary:        ROS ecl_converters package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_converters
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-concepts
Requires:       ros-indigo-ecl-config
Requires:       ros-indigo-ecl-errors
Requires:       ros-indigo-ecl-exceptions
Requires:       ros-indigo-ecl-license
Requires:       ros-indigo-ecl-mpl
Requires:       ros-indigo-ecl-type-traits
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-concepts
BuildRequires:  ros-indigo-ecl-config
BuildRequires:  ros-indigo-ecl-errors
BuildRequires:  ros-indigo-ecl-exceptions
BuildRequires:  ros-indigo-ecl-license
BuildRequires:  ros-indigo-ecl-mpl
BuildRequires:  ros-indigo-ecl-type-traits

%description
Some fast/convenient type converters, mostly for char strings or strings. These
are not really fully fleshed out, alot of them could use the addition for the
whole range of fundamental types (e.g. all integers, not just int, unsigned
int). They will come as the need arises.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Jan 10 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.8-0
- Autogenerated by Bloom

* Sat Jan 09 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.7-0
- Autogenerated by Bloom

* Wed Jan 06 2016 Daniel Stonier <d.stonier@gmail.com> - 0.61.6-1
- Autogenerated by Bloom

* Tue Nov 24 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.5-0
- Autogenerated by Bloom

* Sat Oct 10 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.4-0
- Autogenerated by Bloom

* Sat Sep 05 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.3-0
- Autogenerated by Bloom

* Wed Aug 12 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.2-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.1-0
- Autogenerated by Bloom

* Fri Sep 12 2014 Daniel Stonier <d.stonier@gmail.com> - 0.61.0-0
- Autogenerated by Bloom

