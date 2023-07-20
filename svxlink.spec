#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : svxlink
Version  : 19.09.2
Release  : 1
URL      : https://github.com/sm0svx/svxlink/archive/19.09.2/svxlink-19.09.2.tar.gz
Source0  : https://github.com/sm0svx/svxlink/archive/19.09.2/svxlink-19.09.2.tar.gz
Summary  : The SvxLink project files
Group    : Development/Tools
License  : GPL-2.0 ISC LGPL-2.1 MIT Zlib
Requires: svxlink-bin = %{version}-%{release}
Requires: svxlink-data = %{version}-%{release}
Requires: svxlink-lib = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : gsm-dev
BuildRequires : libgcrypt-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(librtlsdr)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(opus)
BuildRequires : pkgconfig(popt)
BuildRequires : pkgconfig(sigc++-2.0)
BuildRequires : pkgconfig(speex)
BuildRequires : qtbase-dev
BuildRequires : qttools-dev
BuildRequires : tcl-dev tk-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The SvxLink project is a multi purpose voice services system for
ham radio use. For example, EchoLink connections are supported.
Also, the SvxLink server can act as a repeater controller.

This is the source package which can be used to build binary RPMS:

        rpmbuild --rebuild svxlink-%{RELEASE_DATE}-%{RELEASE_NO}.src.rpm

You also need to setup the %%dist variable to something identifying the
distribution you're compiling SvxLink for, like "fc8" if you're compiling
SvxLink for Fedora 8.

%package bin
Summary: bin components for the svxlink package.
Group: Binaries
Requires: svxlink-data = %{version}-%{release}

%description bin
bin components for the svxlink package.


%package data
Summary: data components for the svxlink package.
Group: Data

%description data
data components for the svxlink package.


%package dev
Summary: dev components for the svxlink package.
Group: Development
Requires: svxlink-lib = %{version}-%{release}
Requires: svxlink-bin = %{version}-%{release}
Requires: svxlink-data = %{version}-%{release}
Provides: svxlink-devel = %{version}-%{release}
Requires: svxlink = %{version}-%{release}

%description dev
dev components for the svxlink package.


%package lib
Summary: lib components for the svxlink package.
Group: Libraries
Requires: svxlink-data = %{version}-%{release}

%description lib
lib components for the svxlink package.


%prep
%setup -q -n svxlink-19.09.2
cd %{_builddir}/svxlink-19.09.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689893908
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ../src
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1689893908
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/devcal
/usr/bin/qtel
/usr/bin/remotetrx
/usr/bin/siglevdetcal
/usr/bin/svxlink
/usr/bin/svxlink_gpio_down
/usr/bin/svxlink_gpio_up
/usr/bin/svxreflector

%files data
%defattr(-,root,root,-)
/usr/share/applications/qtel.desktop
/usr/share/icons/link.xpm
/usr/share/qtel/sounds/connect.raw
/usr/share/qtel/translations/qtel_de.qm
/usr/share/qtel/translations/qtel_es.qm
/usr/share/qtel/translations/qtel_fr.qm
/usr/share/qtel/translations/qtel_hu.qm
/usr/share/qtel/translations/qtel_it.qm
/usr/share/qtel/translations/qtel_ja.qm
/usr/share/qtel/translations/qtel_nl.qm
/usr/share/qtel/translations/qtel_ru.qm
/usr/share/qtel/translations/qtel_sv.qm
/usr/share/qtel/translations/qtel_tr.qm
/usr/share/qtel/translations/qtel_uk.qm
/usr/share/svxlink/events.d/CW.tcl
/usr/share/svxlink/events.d/DtmfRepeater.tcl
/usr/share/svxlink/events.d/EchoLink.tcl
/usr/share/svxlink/events.d/Frn.tcl
/usr/share/svxlink/events.d/Help.tcl
/usr/share/svxlink/events.d/Logic.tcl
/usr/share/svxlink/events.d/MetarInfo.tcl
/usr/share/svxlink/events.d/Module.tcl
/usr/share/svxlink/events.d/Parrot.tcl
/usr/share/svxlink/events.d/PropagationMonitor.tcl
/usr/share/svxlink/events.d/RepeaterLogic.tcl
/usr/share/svxlink/events.d/SelCall.tcl
/usr/share/svxlink/events.d/SelCallEnc.tcl
/usr/share/svxlink/events.d/SimplexLogic.tcl
/usr/share/svxlink/events.d/Tcl.tcl.example
/usr/share/svxlink/events.d/TclVoiceMail.tcl
/usr/share/svxlink/events.d/Trx.tcl
/usr/share/svxlink/events.d/locale.tcl
/usr/share/svxlink/events.tcl
/usr/share/svxlink/modules.d/ModulePropagationMonitor.tcl
/usr/share/svxlink/modules.d/ModuleSelCallEnc.tcl
/usr/share/svxlink/modules.d/ModuleTcl.tcl.example
/usr/share/svxlink/modules.d/ModuleTclVoiceMail.tcl

%files dev
%defattr(-,root,root,-)
/usr/include/svxlink/AsyncApplication.h
/usr/include/svxlink/AsyncAtTimer.h
/usr/include/svxlink/AsyncAudioAmp.h
/usr/include/svxlink/AsyncAudioClipper.h
/usr/include/svxlink/AsyncAudioCompressor.h
/usr/include/svxlink/AsyncAudioDebugger.h
/usr/include/svxlink/AsyncAudioDecimator.h
/usr/include/svxlink/AsyncAudioDecoder.h
/usr/include/svxlink/AsyncAudioDelayLine.h
/usr/include/svxlink/AsyncAudioDevice.h
/usr/include/svxlink/AsyncAudioDeviceFactory.h
/usr/include/svxlink/AsyncAudioEncoder.h
/usr/include/svxlink/AsyncAudioFifo.h
/usr/include/svxlink/AsyncAudioFilter.h
/usr/include/svxlink/AsyncAudioFsf.h
/usr/include/svxlink/AsyncAudioGenerator.h
/usr/include/svxlink/AsyncAudioIO.h
/usr/include/svxlink/AsyncAudioInterpolator.h
/usr/include/svxlink/AsyncAudioJitterFifo.h
/usr/include/svxlink/AsyncAudioMixer.h
/usr/include/svxlink/AsyncAudioNoiseAdder.h
/usr/include/svxlink/AsyncAudioPacer.h
/usr/include/svxlink/AsyncAudioPassthrough.h
/usr/include/svxlink/AsyncAudioProcessor.h
/usr/include/svxlink/AsyncAudioReader.h
/usr/include/svxlink/AsyncAudioRecorder.h
/usr/include/svxlink/AsyncAudioSelector.h
/usr/include/svxlink/AsyncAudioSink.h
/usr/include/svxlink/AsyncAudioSource.h
/usr/include/svxlink/AsyncAudioSplitter.h
/usr/include/svxlink/AsyncAudioStreamStateDetector.h
/usr/include/svxlink/AsyncAudioValve.h
/usr/include/svxlink/AsyncConfig.h
/usr/include/svxlink/AsyncCppApplication.h
/usr/include/svxlink/AsyncDnsLookup.h
/usr/include/svxlink/AsyncExec.h
/usr/include/svxlink/AsyncFdWatch.h
/usr/include/svxlink/AsyncFileReader.h
/usr/include/svxlink/AsyncFramedTcpConnection.h
/usr/include/svxlink/AsyncIpAddress.h
/usr/include/svxlink/AsyncMsg.h
/usr/include/svxlink/AsyncPty.h
/usr/include/svxlink/AsyncPtyStreamBuf.h
/usr/include/svxlink/AsyncQtApplication.h
/usr/include/svxlink/AsyncSerial.h
/usr/include/svxlink/AsyncSigCAudioSink.h
/usr/include/svxlink/AsyncSigCAudioSource.h
/usr/include/svxlink/AsyncTcpClient.h
/usr/include/svxlink/AsyncTcpClientBase.h
/usr/include/svxlink/AsyncTcpConnection.h
/usr/include/svxlink/AsyncTcpServer.h
/usr/include/svxlink/AsyncTcpServerBase.h
/usr/include/svxlink/AsyncTimer.h
/usr/include/svxlink/AsyncUdpSocket.h
/usr/include/svxlink/CppStdCompat.h
/usr/include/svxlink/EchoLinkDirectory.h
/usr/include/svxlink/EchoLinkDispatcher.h
/usr/include/svxlink/EchoLinkProxy.h
/usr/include/svxlink/EchoLinkQso.h
/usr/include/svxlink/EchoLinkStationData.h
/usr/include/svxlink/common.h
/usr/lib64/libasyncaudio.so
/usr/lib64/libasynccore.so
/usr/lib64/libasynccpp.so
/usr/lib64/libasyncqt.so
/usr/lib64/libecholib.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libasyncaudio.so.1.6
/usr/lib64/libasyncaudio.so.1.6.0
/usr/lib64/libasynccore.so.1.6
/usr/lib64/libasynccore.so.1.6.0
/usr/lib64/libasynccpp.so.1.6
/usr/lib64/libasynccpp.so.1.6.0
/usr/lib64/libasyncqt.so.1.6
/usr/lib64/libasyncqt.so.1.6.0
/usr/lib64/libecholib.so.1.3
/usr/lib64/libecholib.so.1.3.3
/usr/lib64/svxlink/ModuleDtmfRepeater.so
/usr/lib64/svxlink/ModuleEchoLink.so
/usr/lib64/svxlink/ModuleFrn.so
/usr/lib64/svxlink/ModuleHelp.so
/usr/lib64/svxlink/ModuleMetarInfo.so
/usr/lib64/svxlink/ModuleParrot.so
/usr/lib64/svxlink/ModuleTcl.so
/usr/lib64/svxlink/ModuleTrx.so
