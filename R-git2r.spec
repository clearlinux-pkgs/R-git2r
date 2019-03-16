#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-git2r
Version  : 0.24.0
Release  : 68
URL      : https://cran.r-project.org/src/contrib/git2r_0.24.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/git2r_0.24.0.tar.gz
Summary  : Provides Access to Git Repositories
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: R-git2r-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : curl-dev
BuildRequires : git
BuildRequires : libgit2-dev
BuildRequires : libidn-dev
BuildRequires : libssh2-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libssh2)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev

%description
implementation of the 'Git' core methods. Provides access to 'Git'
    repositories to extract data and running some basic 'Git'
    commands.

%package lib
Summary: lib components for the R-git2r package.
Group: Libraries

%description lib
lib components for the R-git2r package.


%prep
%setup -q -c -n git2r

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546903242

%install
export SOURCE_DATE_EPOCH=1546903242
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library git2r
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library git2r
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library git2r
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library git2r|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/git2r/AUTHORS
/usr/lib64/R/library/git2r/CITATION
/usr/lib64/R/library/git2r/COPYING
/usr/lib64/R/library/git2r/COPYRIGHTS
/usr/lib64/R/library/git2r/DESCRIPTION
/usr/lib64/R/library/git2r/INDEX
/usr/lib64/R/library/git2r/Meta/Rd.rds
/usr/lib64/R/library/git2r/Meta/features.rds
/usr/lib64/R/library/git2r/Meta/hsearch.rds
/usr/lib64/R/library/git2r/Meta/links.rds
/usr/lib64/R/library/git2r/Meta/nsInfo.rds
/usr/lib64/R/library/git2r/Meta/package.rds
/usr/lib64/R/library/git2r/NAMESPACE
/usr/lib64/R/library/git2r/NEWS
/usr/lib64/R/library/git2r/R/git2r
/usr/lib64/R/library/git2r/R/git2r.rdb
/usr/lib64/R/library/git2r/R/git2r.rdx
/usr/lib64/R/library/git2r/help/AnIndex
/usr/lib64/R/library/git2r/help/aliases.rds
/usr/lib64/R/library/git2r/help/git2r.rdb
/usr/lib64/R/library/git2r/help/git2r.rdx
/usr/lib64/R/library/git2r/help/paths.rds
/usr/lib64/R/library/git2r/html/00Index.html
/usr/lib64/R/library/git2r/html/R.css
/usr/lib64/R/library/git2r/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/git2r/libs/git2r.so
/usr/lib64/R/library/git2r/libs/git2r.so.avx2
/usr/lib64/R/library/git2r/libs/git2r.so.avx512
