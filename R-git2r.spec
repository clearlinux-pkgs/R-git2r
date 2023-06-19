#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-git2r
Version  : 0.32.0
Release  : 121
URL      : https://cran.r-project.org/src/contrib/git2r_0.32.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/git2r_0.32.0.tar.gz
Summary  : Provides Access to Git Repositories
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MIT
Requires: R-git2r-lib = %{version}-%{release}
Requires: R-git2r-license = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : curl-dev
BuildRequires : git
BuildRequires : libgit2-dev
BuildRequires : libidn-dev
BuildRequires : libssh2-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
implementation of the 'Git' core methods. Provides access to 'Git'
    repositories to extract data and running some basic 'Git'
    commands.

%package lib
Summary: lib components for the R-git2r package.
Group: Libraries
Requires: R-git2r-license = %{version}-%{release}

%description lib
lib components for the R-git2r package.


%package license
Summary: license components for the R-git2r package.
Group: Default

%description license
license components for the R-git2r package.


%prep
%setup -q -n git2r

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681407060

%install
export SOURCE_DATE_EPOCH=1681407060
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-git2r
cp %{_builddir}/git2r/inst/COPYING %{buildroot}/usr/share/package-licenses/R-git2r/3d90371a2a6ade0808247c11cf390fa4f54f49d0 || :
cp %{_builddir}/git2r/inst/COPYRIGHTS %{buildroot}/usr/share/package-licenses/R-git2r/5eaa2ab3357c62bc6181fa1f37fb2ccf6f8e4733 || :
cp %{_builddir}/git2r/src/libgit2/deps/http-parser/COPYING %{buildroot}/usr/share/package-licenses/R-git2r/1a00a507fb89bb0018c092d6835077d541e76dc2 || :
cp %{_builddir}/git2r/src/libgit2/deps/regex/COPYING %{buildroot}/usr/share/package-licenses/R-git2r/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/git2r/AUTHORS
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
/usr/lib64/R/library/git2r/NEWS.md
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
/usr/lib64/R/library/git2r/tests/add-force.R
/usr/lib64/R/library/git2r/tests/bare_repository.R
/usr/lib64/R/library/git2r/tests/blame.R
/usr/lib64/R/library/git2r/tests/blob.R
/usr/lib64/R/library/git2r/tests/branch.R
/usr/lib64/R/library/git2r/tests/bundle.R
/usr/lib64/R/library/git2r/tests/checkout-named-branch.R
/usr/lib64/R/library/git2r/tests/checkout.R
/usr/lib64/R/library/git2r/tests/checkout_branch.R
/usr/lib64/R/library/git2r/tests/checkout_commit.R
/usr/lib64/R/library/git2r/tests/checkout_tag.R
/usr/lib64/R/library/git2r/tests/clone_bare.R
/usr/lib64/R/library/git2r/tests/clone_branch.R
/usr/lib64/R/library/git2r/tests/clone_checkout.R
/usr/lib64/R/library/git2r/tests/commit.R
/usr/lib64/R/library/git2r/tests/commits_path.R
/usr/lib64/R/library/git2r/tests/config.R
/usr/lib64/R/library/git2r/tests/diff.R
/usr/lib64/R/library/git2r/tests/fast_forward_merge.R
/usr/lib64/R/library/git2r/tests/fetch.R
/usr/lib64/R/library/git2r/tests/graph.R
/usr/lib64/R/library/git2r/tests/index.R
/usr/lib64/R/library/git2r/tests/invalid-conf-var.R
/usr/lib64/R/library/git2r/tests/libgit2.R
/usr/lib64/R/library/git2r/tests/ls_tree.R
/usr/lib64/R/library/git2r/tests/merge.R
/usr/lib64/R/library/git2r/tests/merge_named_branch.R
/usr/lib64/R/library/git2r/tests/normal_merge.R
/usr/lib64/R/library/git2r/tests/note.R
/usr/lib64/R/library/git2r/tests/odb_blobs.R
/usr/lib64/R/library/git2r/tests/pre-process-path.R
/usr/lib64/R/library/git2r/tests/pull.R
/usr/lib64/R/library/git2r/tests/push-force.R
/usr/lib64/R/library/git2r/tests/push.R
/usr/lib64/R/library/git2r/tests/reference.R
/usr/lib64/R/library/git2r/tests/reflog.R
/usr/lib64/R/library/git2r/tests/refspec.R
/usr/lib64/R/library/git2r/tests/remotes.R
/usr/lib64/R/library/git2r/tests/remove.R
/usr/lib64/R/library/git2r/tests/repository.R
/usr/lib64/R/library/git2r/tests/reset.R
/usr/lib64/R/library/git2r/tests/revparse.R
/usr/lib64/R/library/git2r/tests/signature.R
/usr/lib64/R/library/git2r/tests/stash.R
/usr/lib64/R/library/git2r/tests/status.R
/usr/lib64/R/library/git2r/tests/tag.R
/usr/lib64/R/library/git2r/tests/time.R
/usr/lib64/R/library/git2r/tests/tree.R
/usr/lib64/R/library/git2r/tests/util/check.R
/usr/lib64/R/library/git2r/tests/when.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/git2r/libs/git2r.so
/usr/lib64/R/library/git2r/libs/git2r.so.avx2
/usr/lib64/R/library/git2r/libs/git2r.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-git2r/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/R-git2r/1a00a507fb89bb0018c092d6835077d541e76dc2
/usr/share/package-licenses/R-git2r/3d90371a2a6ade0808247c11cf390fa4f54f49d0
/usr/share/package-licenses/R-git2r/5eaa2ab3357c62bc6181fa1f37fb2ccf6f8e4733
