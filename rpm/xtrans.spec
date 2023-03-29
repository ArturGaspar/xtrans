Name:       xtrans
Version:    1.5.0
Release:    1%{?dist}
Summary:    X Network Transport layer shared code
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/lib/libxtrans
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-macros) >= 1.12

%description
Base package for %{name}.

%package devel
Summary:    X Network Transport layer shared code

%description devel
xtrans is a library of code that is shared among various X packages to
handle network protocol transport in a modular fashion, allowing a
single place to add new transport types.  It is used by the X server,
libX11, libICE, the X font server, and related components.

%package doc
Summary:    Documentation for %{name}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files devel
%license COPYING
%{_includedir}/X11/Xtrans
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/pkgconfig/%{name}.pc

%files doc
%license COPYING
%{_docdir}/%{name}
