Name: phomemo-tools
Version: 1.0
Release: 1%{?dist}
Summary: A set of tools to use Phomemo M02 printer
License: GPLv3

Source: %{name}-%{version}.tar.xz
BuildArch: noarch
BuildRequires: cups

Requires: cups
Requires: python3
Requires: python3-pillow
Requires: python3-pyusb

%description
This packages provides tools to send images to print on Phomemo M02
Thermal printer.
It also installs a CUPS driver for the printer into the system.

%prep
%setup -q

%build

make all

%install

make DESTDIR=%{buildroot} install

%post
# Needed to fix the following error:
# cupsd[2659]: Can\'t open Bluetooth connection: [Errno 13] Permission denied
semanage permissive -a cupsd_t

%files
/usr/share/phomemo/LICENSE
/usr/share/phomemo/README.md
/usr/share/phomemo/phomemo-q22.xml
/usr/share/phomemo/phomemo-filter.py
/usr/share/phomemo/format-checker.py
/usr/share/cups/model/Phomemo/Phomemo-M02.ppd.gz
/usr/share/cups/model/Phomemo/Phomemo-T02.ppd.gz
/usr/share/cups/model/Phomemo/Phomemo-M110.ppd.gz
/usr/share/cups/drv/phomemo-m02_t02.drv
/usr/share/cups/drv/phomemo-m110.drv
/usr/lib/cups/filter/rastertopm02_t02
/usr/lib/cups/filter/rastertopm110
/usr/lib/cups/backend/phomemo

%changelog
* Fri Dec 4 2020 Laurent Vivier <laurent@vivier.eu> - 1.0
- First package
