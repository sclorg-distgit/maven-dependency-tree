%{?scl:%scl_package maven-dependency-tree}
%{!?scl:%global pkg_name %{name}}


Name:          %{?scl_prefix}maven-dependency-tree
Version:       3.0
Release:       3.1%{?dist}
Summary:       Maven dependency tree artifact
Group:         Development/Libraries
License:       ASL 2.0
Url:           http://maven.apache.org/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
BuildArch:     noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-compat)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven:maven-core)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  %{?scl_prefix}mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.aether:aether-api)
BuildRequires:  %{?scl_prefix}mvn(org.eclipse.aether:aether-util)

Provides:      %{?scl_prefix}maven-shared-dependency-tree = %{version}-%{release}

%description
Apache Maven dependency tree artifact. Originally part of maven-shared.

%package javadoc
Group:         Documentation
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q

find -name Maven3DependencyGraphBuilder.java -delete
%pom_remove_dep org.sonatype.aether:

%pom_remove_plugin :apache-rat-plugin

%build
# Incompatible version of jMock (Fedora has 2.x, upstream uses 1.x)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 3.0-3.1
- Automated package import and SCL-ization

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct  9 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0-1
- Update to upstream version 3.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2-1
- Update to upstream version 2.2

* Mon Aug  4 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-8
- Fix build-requires on parent POM

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-6
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-5
- Fix unowned directory

* Fri Jan 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-4
- Update to Maven 3 APIs

* Thu Oct  3 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-3
- Add missing BuildRequires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-1
- Remove dependency on Sonatype Aether
- Resolves: rhbz#985704

* Mon Jul 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-1
- Update to upstream version 2.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-2
- Build with xmvn

* Wed Oct 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-1
- Initial package
