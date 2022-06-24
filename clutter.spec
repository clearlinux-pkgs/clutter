#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clutter
Version  : 1.26.4
Release  : 32
URL      : https://download.gnome.org/sources/clutter/1.26/clutter-1.26.4.tar.xz
Source0  : https://download.gnome.org/sources/clutter/1.26/clutter-1.26.4.tar.xz
Summary  : Clutter Core Library
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: clutter-data = %{version}-%{release}
Requires: clutter-lib = %{version}-%{release}
Requires: clutter-license = %{version}-%{release}
Requires: clutter-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libXcomposite-dev
BuildRequires : libevdev-dev
BuildRequires : libxslt-bin
BuildRequires : mesa-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(cogl-1.0)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libinput)
BuildRequires : pkgconfig(pangoft2)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcomposite)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : sed
BuildRequires : xorgproto-dev

%description
The code in this directory is meant to be XIncluded into the Clutter API
reference, and thus is to be considered part of the Clutter documentation.

%package data
Summary: data components for the clutter package.
Group: Data

%description data
data components for the clutter package.


%package dev
Summary: dev components for the clutter package.
Group: Development
Requires: clutter-lib = %{version}-%{release}
Requires: clutter-data = %{version}-%{release}
Provides: clutter-devel = %{version}-%{release}
Requires: clutter = %{version}-%{release}

%description dev
dev components for the clutter package.


%package doc
Summary: doc components for the clutter package.
Group: Documentation

%description doc
doc components for the clutter package.


%package lib
Summary: lib components for the clutter package.
Group: Libraries
Requires: clutter-data = %{version}-%{release}
Requires: clutter-license = %{version}-%{release}

%description lib
lib components for the clutter package.


%package license
Summary: license components for the clutter package.
Group: Default

%description license
license components for the clutter package.


%package locales
Summary: locales components for the clutter package.
Group: Default

%description locales
locales components for the clutter package.


%prep
%setup -q -n clutter-1.26.4
cd %{_builddir}/clutter-1.26.4
pushd ..
cp -a clutter-1.26.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656097958
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%configure --disable-static --enable-wayland-backend=yes \
--enable-wayland-compositor=yes \
--enable-evdev-input=yes \
--enable-gdk-backend=yes \
--enable-egl-backend=yes \
--enable-xinput
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --enable-wayland-backend=yes \
--enable-wayland-compositor=yes \
--enable-evdev-input=yes \
--enable-gdk-backend=yes \
--enable-egl-backend=yes \
--enable-xinput --disable-introspection --disable-gtk-doc
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1656097958
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clutter
cp %{_builddir}/clutter-1.26.4/COPYING %{buildroot}/usr/share/package-licenses/clutter/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/clutter-1.26.4/doc/reference/html/license.html %{buildroot}/usr/share/package-licenses/clutter/9cc6b307b71af5508e15bc0bdcb1bb1bc92443c0
pushd ../buildavx2/
%make_install_v3
popd
%make_install
%find_lang clutter-1.0
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Cally-1.0.typelib
/usr/lib64/girepository-1.0/Clutter-1.0.typelib
/usr/lib64/girepository-1.0/ClutterGdk-1.0.typelib
/usr/lib64/girepository-1.0/ClutterX11-1.0.typelib
/usr/share/clutter-1.0/valgrind/clutter.supp
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/clutter-1.0/cally/cally-actor.h
/usr/include/clutter-1.0/cally/cally-clone.h
/usr/include/clutter-1.0/cally/cally-factory.h
/usr/include/clutter-1.0/cally/cally-group.h
/usr/include/clutter-1.0/cally/cally-main.h
/usr/include/clutter-1.0/cally/cally-rectangle.h
/usr/include/clutter-1.0/cally/cally-root.h
/usr/include/clutter-1.0/cally/cally-stage.h
/usr/include/clutter-1.0/cally/cally-text.h
/usr/include/clutter-1.0/cally/cally-texture.h
/usr/include/clutter-1.0/cally/cally-util.h
/usr/include/clutter-1.0/cally/cally.h
/usr/include/clutter-1.0/clutter/clutter-action.h
/usr/include/clutter-1.0/clutter/clutter-actor-meta.h
/usr/include/clutter-1.0/clutter/clutter-actor.h
/usr/include/clutter-1.0/clutter/clutter-align-constraint.h
/usr/include/clutter-1.0/clutter/clutter-animatable.h
/usr/include/clutter-1.0/clutter/clutter-autocleanups.h
/usr/include/clutter-1.0/clutter/clutter-backend.h
/usr/include/clutter-1.0/clutter/clutter-bin-layout.h
/usr/include/clutter-1.0/clutter/clutter-bind-constraint.h
/usr/include/clutter-1.0/clutter/clutter-binding-pool.h
/usr/include/clutter-1.0/clutter/clutter-blur-effect.h
/usr/include/clutter-1.0/clutter/clutter-box-layout.h
/usr/include/clutter-1.0/clutter/clutter-brightness-contrast-effect.h
/usr/include/clutter-1.0/clutter/clutter-cairo.h
/usr/include/clutter-1.0/clutter/clutter-canvas.h
/usr/include/clutter-1.0/clutter/clutter-child-meta.h
/usr/include/clutter-1.0/clutter/clutter-click-action.h
/usr/include/clutter-1.0/clutter/clutter-clone.h
/usr/include/clutter-1.0/clutter/clutter-cogl-compat.h
/usr/include/clutter-1.0/clutter/clutter-color-static.h
/usr/include/clutter-1.0/clutter/clutter-color.h
/usr/include/clutter-1.0/clutter/clutter-colorize-effect.h
/usr/include/clutter-1.0/clutter/clutter-config.h
/usr/include/clutter-1.0/clutter/clutter-constraint.h
/usr/include/clutter-1.0/clutter/clutter-container.h
/usr/include/clutter-1.0/clutter/clutter-content.h
/usr/include/clutter-1.0/clutter/clutter-deform-effect.h
/usr/include/clutter-1.0/clutter/clutter-deprecated.h
/usr/include/clutter-1.0/clutter/clutter-desaturate-effect.h
/usr/include/clutter-1.0/clutter/clutter-device-manager.h
/usr/include/clutter-1.0/clutter/clutter-drag-action.h
/usr/include/clutter-1.0/clutter/clutter-drop-action.h
/usr/include/clutter-1.0/clutter/clutter-effect.h
/usr/include/clutter-1.0/clutter/clutter-enum-types.h
/usr/include/clutter-1.0/clutter/clutter-enums.h
/usr/include/clutter-1.0/clutter/clutter-event.h
/usr/include/clutter-1.0/clutter/clutter-feature.h
/usr/include/clutter-1.0/clutter/clutter-fixed-layout.h
/usr/include/clutter-1.0/clutter/clutter-flow-layout.h
/usr/include/clutter-1.0/clutter/clutter-gesture-action.h
/usr/include/clutter-1.0/clutter/clutter-grid-layout.h
/usr/include/clutter-1.0/clutter/clutter-group.h
/usr/include/clutter-1.0/clutter/clutter-image.h
/usr/include/clutter-1.0/clutter/clutter-input-device.h
/usr/include/clutter-1.0/clutter/clutter-interval.h
/usr/include/clutter-1.0/clutter/clutter-keyframe-transition.h
/usr/include/clutter-1.0/clutter/clutter-keysyms.h
/usr/include/clutter-1.0/clutter/clutter-layout-manager.h
/usr/include/clutter-1.0/clutter/clutter-layout-meta.h
/usr/include/clutter-1.0/clutter/clutter-macros.h
/usr/include/clutter-1.0/clutter/clutter-main.h
/usr/include/clutter-1.0/clutter/clutter-marshal.h
/usr/include/clutter-1.0/clutter/clutter-offscreen-effect.h
/usr/include/clutter-1.0/clutter/clutter-page-turn-effect.h
/usr/include/clutter-1.0/clutter/clutter-paint-node.h
/usr/include/clutter-1.0/clutter/clutter-paint-nodes.h
/usr/include/clutter-1.0/clutter/clutter-pan-action.h
/usr/include/clutter-1.0/clutter/clutter-path-constraint.h
/usr/include/clutter-1.0/clutter/clutter-path.h
/usr/include/clutter-1.0/clutter/clutter-property-transition.h
/usr/include/clutter-1.0/clutter/clutter-rotate-action.h
/usr/include/clutter-1.0/clutter/clutter-script.h
/usr/include/clutter-1.0/clutter/clutter-scriptable.h
/usr/include/clutter-1.0/clutter/clutter-scroll-actor.h
/usr/include/clutter-1.0/clutter/clutter-settings.h
/usr/include/clutter-1.0/clutter/clutter-shader-effect.h
/usr/include/clutter-1.0/clutter/clutter-shader-types.h
/usr/include/clutter-1.0/clutter/clutter-snap-constraint.h
/usr/include/clutter-1.0/clutter/clutter-stage-manager.h
/usr/include/clutter-1.0/clutter/clutter-stage.h
/usr/include/clutter-1.0/clutter/clutter-swipe-action.h
/usr/include/clutter-1.0/clutter/clutter-tap-action.h
/usr/include/clutter-1.0/clutter/clutter-test-utils.h
/usr/include/clutter-1.0/clutter/clutter-text-buffer.h
/usr/include/clutter-1.0/clutter/clutter-text.h
/usr/include/clutter-1.0/clutter/clutter-texture.h
/usr/include/clutter-1.0/clutter/clutter-timeline.h
/usr/include/clutter-1.0/clutter/clutter-transition-group.h
/usr/include/clutter-1.0/clutter/clutter-transition.h
/usr/include/clutter-1.0/clutter/clutter-types.h
/usr/include/clutter-1.0/clutter/clutter-units.h
/usr/include/clutter-1.0/clutter/clutter-version.h
/usr/include/clutter-1.0/clutter/clutter-zoom-action.h
/usr/include/clutter-1.0/clutter/clutter.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-actor.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-alpha.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-animatable.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-animation.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-animator.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-backend.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-behaviour-depth.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-behaviour-ellipse.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-behaviour-opacity.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-behaviour-path.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-behaviour-rotate.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-behaviour-scale.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-behaviour.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-bin-layout.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-box.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-cairo-texture.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-container.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-fixed.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-frame-source.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-group.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-input-device.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-keysyms.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-list-model.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-main.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-media.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-model.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-rectangle.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-score.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-shader.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-stage-manager.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-stage.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-state.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-table-layout.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-texture.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-timeline.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-timeout-pool.h
/usr/include/clutter-1.0/clutter/deprecated/clutter-util.h
/usr/include/clutter-1.0/clutter/egl/clutter-egl-headers.h
/usr/include/clutter-1.0/clutter/egl/clutter-egl.h
/usr/include/clutter-1.0/clutter/evdev/clutter-evdev.h
/usr/include/clutter-1.0/clutter/gdk/clutter-gdk.h
/usr/include/clutter-1.0/clutter/glx/clutter-glx-texture-pixmap.h
/usr/include/clutter-1.0/clutter/glx/clutter-glx.h
/usr/include/clutter-1.0/clutter/wayland/clutter-wayland-compositor.h
/usr/include/clutter-1.0/clutter/wayland/clutter-wayland-surface.h
/usr/include/clutter-1.0/clutter/wayland/clutter-wayland.h
/usr/include/clutter-1.0/clutter/x11/clutter-x11-texture-pixmap.h
/usr/include/clutter-1.0/clutter/x11/clutter-x11.h
/usr/lib64/libclutter-1.0.so
/usr/lib64/libclutter-glx-1.0.so
/usr/lib64/pkgconfig/cally-1.0.pc
/usr/lib64/pkgconfig/clutter-1.0.pc
/usr/lib64/pkgconfig/clutter-cogl-1.0.pc
/usr/lib64/pkgconfig/clutter-egl-1.0.pc
/usr/lib64/pkgconfig/clutter-gdk-1.0.pc
/usr/lib64/pkgconfig/clutter-glx-1.0.pc
/usr/lib64/pkgconfig/clutter-wayland-1.0.pc
/usr/lib64/pkgconfig/clutter-wayland-compositor-1.0.pc
/usr/lib64/pkgconfig/clutter-x11-1.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/clutter/CallyActor.html
/usr/share/gtk-doc/html/clutter/CallyClone.html
/usr/share/gtk-doc/html/clutter/CallyGroup.html
/usr/share/gtk-doc/html/clutter/CallyRectangle.html
/usr/share/gtk-doc/html/clutter/CallyRoot.html
/usr/share/gtk-doc/html/clutter/CallyStage.html
/usr/share/gtk-doc/html/clutter/CallyText.html
/usr/share/gtk-doc/html/clutter/CallyTexture.html
/usr/share/gtk-doc/html/clutter/CallyUtil.html
/usr/share/gtk-doc/html/clutter/ClutterAction.html
/usr/share/gtk-doc/html/clutter/ClutterActor.html
/usr/share/gtk-doc/html/clutter/ClutterActorMeta.html
/usr/share/gtk-doc/html/clutter/ClutterAlignConstraint.html
/usr/share/gtk-doc/html/clutter/ClutterAlpha.html
/usr/share/gtk-doc/html/clutter/ClutterAnimatable.html
/usr/share/gtk-doc/html/clutter/ClutterAnimator.html
/usr/share/gtk-doc/html/clutter/ClutterBackend.html
/usr/share/gtk-doc/html/clutter/ClutterBehaviour.html
/usr/share/gtk-doc/html/clutter/ClutterBehaviourDepth.html
/usr/share/gtk-doc/html/clutter/ClutterBehaviourEllipse.html
/usr/share/gtk-doc/html/clutter/ClutterBehaviourOpacity.html
/usr/share/gtk-doc/html/clutter/ClutterBehaviourPath.html
/usr/share/gtk-doc/html/clutter/ClutterBehaviourRotate.html
/usr/share/gtk-doc/html/clutter/ClutterBehaviourScale.html
/usr/share/gtk-doc/html/clutter/ClutterBinLayout.html
/usr/share/gtk-doc/html/clutter/ClutterBindConstraint.html
/usr/share/gtk-doc/html/clutter/ClutterBlurEffect.html
/usr/share/gtk-doc/html/clutter/ClutterBox.html
/usr/share/gtk-doc/html/clutter/ClutterBoxLayout.html
/usr/share/gtk-doc/html/clutter/ClutterBrightnessContrastEffect.html
/usr/share/gtk-doc/html/clutter/ClutterCairoTexture.html
/usr/share/gtk-doc/html/clutter/ClutterCanvas.html
/usr/share/gtk-doc/html/clutter/ClutterChildMeta.html
/usr/share/gtk-doc/html/clutter/ClutterClickAction.html
/usr/share/gtk-doc/html/clutter/ClutterClone.html
/usr/share/gtk-doc/html/clutter/ClutterColorizeEffect.html
/usr/share/gtk-doc/html/clutter/ClutterConstraint.html
/usr/share/gtk-doc/html/clutter/ClutterContainer.html
/usr/share/gtk-doc/html/clutter/ClutterContent.html
/usr/share/gtk-doc/html/clutter/ClutterDeformEffect.html
/usr/share/gtk-doc/html/clutter/ClutterDesaturateEffect.html
/usr/share/gtk-doc/html/clutter/ClutterDeviceManager.html
/usr/share/gtk-doc/html/clutter/ClutterDragAction.html
/usr/share/gtk-doc/html/clutter/ClutterDropAction.html
/usr/share/gtk-doc/html/clutter/ClutterEffect.html
/usr/share/gtk-doc/html/clutter/ClutterFixedLayout.html
/usr/share/gtk-doc/html/clutter/ClutterFlowLayout.html
/usr/share/gtk-doc/html/clutter/ClutterGLXTexturePixmap.html
/usr/share/gtk-doc/html/clutter/ClutterGestureAction.html
/usr/share/gtk-doc/html/clutter/ClutterGridLayout.html
/usr/share/gtk-doc/html/clutter/ClutterGroup.html
/usr/share/gtk-doc/html/clutter/ClutterImage.html
/usr/share/gtk-doc/html/clutter/ClutterInputDevice.html
/usr/share/gtk-doc/html/clutter/ClutterKeyframeTransition.html
/usr/share/gtk-doc/html/clutter/ClutterLayoutManager.html
/usr/share/gtk-doc/html/clutter/ClutterLayoutMeta.html
/usr/share/gtk-doc/html/clutter/ClutterListModel.html
/usr/share/gtk-doc/html/clutter/ClutterMedia.html
/usr/share/gtk-doc/html/clutter/ClutterModel.html
/usr/share/gtk-doc/html/clutter/ClutterModelIter.html
/usr/share/gtk-doc/html/clutter/ClutterOffscreenEffect.html
/usr/share/gtk-doc/html/clutter/ClutterPageTurnEffect.html
/usr/share/gtk-doc/html/clutter/ClutterPaintNode.html
/usr/share/gtk-doc/html/clutter/ClutterPanAction.html
/usr/share/gtk-doc/html/clutter/ClutterPath.html
/usr/share/gtk-doc/html/clutter/ClutterPathConstraint.html
/usr/share/gtk-doc/html/clutter/ClutterPropertyTransition.html
/usr/share/gtk-doc/html/clutter/ClutterRectangle.html
/usr/share/gtk-doc/html/clutter/ClutterRotateAction.html
/usr/share/gtk-doc/html/clutter/ClutterScore.html
/usr/share/gtk-doc/html/clutter/ClutterScript.html
/usr/share/gtk-doc/html/clutter/ClutterScriptable.html
/usr/share/gtk-doc/html/clutter/ClutterScrollActor.html
/usr/share/gtk-doc/html/clutter/ClutterSettings.html
/usr/share/gtk-doc/html/clutter/ClutterShaderEffect.html
/usr/share/gtk-doc/html/clutter/ClutterSnapConstraint.html
/usr/share/gtk-doc/html/clutter/ClutterStage.html
/usr/share/gtk-doc/html/clutter/ClutterState.html
/usr/share/gtk-doc/html/clutter/ClutterSwipeAction.html
/usr/share/gtk-doc/html/clutter/ClutterTableLayout.html
/usr/share/gtk-doc/html/clutter/ClutterTapAction.html
/usr/share/gtk-doc/html/clutter/ClutterText.html
/usr/share/gtk-doc/html/clutter/ClutterTextBuffer.html
/usr/share/gtk-doc/html/clutter/ClutterTexture.html
/usr/share/gtk-doc/html/clutter/ClutterTimeline.html
/usr/share/gtk-doc/html/clutter/ClutterTransition.html
/usr/share/gtk-doc/html/clutter/ClutterTransitionGroup.html
/usr/share/gtk-doc/html/clutter/ClutterX11TexturePixmap.html
/usr/share/gtk-doc/html/clutter/ClutterZoomAction.html
/usr/share/gtk-doc/html/clutter/actor-box.png
/usr/share/gtk-doc/html/clutter/actor-example.png
/usr/share/gtk-doc/html/clutter/animator-key-frames.png
/usr/share/gtk-doc/html/clutter/annotation-glossary.html
/usr/share/gtk-doc/html/clutter/bin-layout.png
/usr/share/gtk-doc/html/clutter/box-layout.png
/usr/share/gtk-doc/html/clutter/building-clutter.html
/usr/share/gtk-doc/html/clutter/cally.html
/usr/share/gtk-doc/html/clutter/ch01.html
/usr/share/gtk-doc/html/clutter/ch02.html
/usr/share/gtk-doc/html/clutter/ch03.html
/usr/share/gtk-doc/html/clutter/ch04.html
/usr/share/gtk-doc/html/clutter/ch05.html
/usr/share/gtk-doc/html/clutter/ch06.html
/usr/share/gtk-doc/html/clutter/ch07.html
/usr/share/gtk-doc/html/clutter/ch08.html
/usr/share/gtk-doc/html/clutter/ch09.html
/usr/share/gtk-doc/html/clutter/ch10.html
/usr/share/gtk-doc/html/clutter/ch11.html
/usr/share/gtk-doc/html/clutter/ch12.html
/usr/share/gtk-doc/html/clutter/ch13.html
/usr/share/gtk-doc/html/clutter/ch14.html
/usr/share/gtk-doc/html/clutter/clutter-Base-geometric-types.html
/usr/share/gtk-doc/html/clutter/clutter-Cairo-integration.html
/usr/share/gtk-doc/html/clutter/clutter-ClutterWaylandSurface.html
/usr/share/gtk-doc/html/clutter/clutter-Colors.html
/usr/share/gtk-doc/html/clutter/clutter-EGL-Specific-Support.html
/usr/share/gtk-doc/html/clutter/clutter-Events.html
/usr/share/gtk-doc/html/clutter/clutter-Features.html
/usr/share/gtk-doc/html/clutter/clutter-GDK-Specific-Support.html
/usr/share/gtk-doc/html/clutter/clutter-General-API.html
/usr/share/gtk-doc/html/clutter/clutter-General.html
/usr/share/gtk-doc/html/clutter/clutter-Implicit-Animations.html
/usr/share/gtk-doc/html/clutter/clutter-Intel-CE3100-CE4100-Specific-Support.html
/usr/share/gtk-doc/html/clutter/clutter-Key-Bindings.html
/usr/share/gtk-doc/html/clutter/clutter-Paint-Nodes.html
/usr/share/gtk-doc/html/clutter/clutter-Shaders.html
/usr/share/gtk-doc/html/clutter/clutter-Stage-Manager.html
/usr/share/gtk-doc/html/clutter/clutter-Unit-conversion.html
/usr/share/gtk-doc/html/clutter/clutter-Utilities.html
/usr/share/gtk-doc/html/clutter/clutter-Value-intervals.html
/usr/share/gtk-doc/html/clutter/clutter-Versioning-Macros.html
/usr/share/gtk-doc/html/clutter/clutter-Wayland-compositor-specific-support.html
/usr/share/gtk-doc/html/clutter/clutter-Wayland-specific-support.html
/usr/share/gtk-doc/html/clutter/clutter-Win32-Specific-Support.html
/usr/share/gtk-doc/html/clutter/clutter-X11-Specific-Support.html
/usr/share/gtk-doc/html/clutter/clutter-clutter-mir.html
/usr/share/gtk-doc/html/clutter/clutter-overview.html
/usr/share/gtk-doc/html/clutter/clutter.devhelp2
/usr/share/gtk-doc/html/clutter/clutteranimation.html
/usr/share/gtk-doc/html/clutter/clutterbackends.html
/usr/share/gtk-doc/html/clutter/clutterbase.html
/usr/share/gtk-doc/html/clutter/clutterglossary.html
/usr/share/gtk-doc/html/clutter/clutterobjecthierarchy.html
/usr/share/gtk-doc/html/clutter/clutterobjectindex.html
/usr/share/gtk-doc/html/clutter/clutterobjects.html
/usr/share/gtk-doc/html/clutter/cluttertools.html
/usr/share/gtk-doc/html/clutter/constraints-example.png
/usr/share/gtk-doc/html/clutter/deprecated.html
/usr/share/gtk-doc/html/clutter/easing-modes.png
/usr/share/gtk-doc/html/clutter/event-flow.png
/usr/share/gtk-doc/html/clutter/flow-layout.png
/usr/share/gtk-doc/html/clutter/go01.html
/usr/share/gtk-doc/html/clutter/home.png
/usr/share/gtk-doc/html/clutter/index.html
/usr/share/gtk-doc/html/clutter/iterating-paths.html
/usr/share/gtk-doc/html/clutter/ix01.html
/usr/share/gtk-doc/html/clutter/left-insensitive.png
/usr/share/gtk-doc/html/clutter/left.png
/usr/share/gtk-doc/html/clutter/license.html
/usr/share/gtk-doc/html/clutter/migrating-ClutterAnimation.html
/usr/share/gtk-doc/html/clutter/migrating-ClutterBehaviour.html
/usr/share/gtk-doc/html/clutter/migrating-ClutterEffect.html
/usr/share/gtk-doc/html/clutter/migrating-ClutterPath.html
/usr/share/gtk-doc/html/clutter/migration.html
/usr/share/gtk-doc/html/clutter/offscreen-redirect.png
/usr/share/gtk-doc/html/clutter/path-alpha-func.png
/usr/share/gtk-doc/html/clutter/pt10.html
/usr/share/gtk-doc/html/clutter/right-insensitive.png
/usr/share/gtk-doc/html/clutter/right.png
/usr/share/gtk-doc/html/clutter/running-clutter.html
/usr/share/gtk-doc/html/clutter/style.css
/usr/share/gtk-doc/html/clutter/table-layout.png
/usr/share/gtk-doc/html/clutter/up-insensitive.png
/usr/share/gtk-doc/html/clutter/up.png
/usr/share/gtk-doc/html/clutter/using-cairo.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libclutter-1.0.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libclutter-1.0.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libclutter-1.0.so.0.2600.4
/usr/lib64/glibc-hwcaps/x86-64-v3/libclutter-glx-1.0.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libclutter-glx-1.0.so.0
/usr/lib64/libclutter-1.0.so.0
/usr/lib64/libclutter-1.0.so.0.2600.4
/usr/lib64/libclutter-glx-1.0.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clutter/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/clutter/9cc6b307b71af5508e15bc0bdcb1bb1bc92443c0

%files locales -f clutter-1.0.lang
%defattr(-,root,root,-)

