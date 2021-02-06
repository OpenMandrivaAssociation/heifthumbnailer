Name: heifthumbnailer
Version: 1.0
Release: %{?date:0.%{date}.}1
Source0: https://github.com/zzag/heifthumbnailer/archive/%{?date:master}%{!?date:%{version}}/%{name}-%{version}.tar.gz
Summary: Thumbnailer for HEIF image files
URL: https://github.com/zzag/heifthumbnailer
License: LGPLv3
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: pkgconfig(libheif) >= 1.1
BuildRequires: qt5-macros
BuildRequires: qmake5
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5JobWidgets)
BuildRequires: cmake(KF5Solid)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Auth)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5KIO)
BuildRequires: ninja

%description
Thumbnailer for HEIF image files

%prep
%autosetup -p1 -n %{name}-%{?date:master}%{!?date:%{version}}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/plugins/heifthumbnail.so
%{_datadir}/kservices5/heifthumbnail.desktop
