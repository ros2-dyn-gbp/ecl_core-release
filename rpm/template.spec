Name:           ros-indigo-ecl-devices
Version:        0.61.2
Release:        0%{?dist}
Summary:        ROS ecl_devices package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/ecl_devices
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-ecl-config
Requires:       ros-indigo-ecl-containers
Requires:       ros-indigo-ecl-errors
Requires:       ros-indigo-ecl-license
Requires:       ros-indigo-ecl-mpl
Requires:       ros-indigo-ecl-threads
Requires:       ros-indigo-ecl-type-traits
Requires:       ros-indigo-ecl-utilities
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ecl-config
BuildRequires:  ros-indigo-ecl-containers
BuildRequires:  ros-indigo-ecl-errors
BuildRequires:  ros-indigo-ecl-license
BuildRequires:  ros-indigo-ecl-mpl
BuildRequires:  ros-indigo-ecl-threads
BuildRequires:  ros-indigo-ecl-type-traits
BuildRequires:  ros-indigo-ecl-utilities

%description
Provides an extensible and standardised framework for input-output devices.

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
* Wed Aug 12 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.2-0
- Autogenerated by Bloom

* Wed Jul 22 2015 Daniel Stonier <d.stonier@gmail.com> - 0.61.1-0
- Autogenerated by Bloom

