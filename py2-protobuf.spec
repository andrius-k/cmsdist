### RPM external py2-protobuf 3.4.1
## INITENV +PATH PYTHONPATH %{i}/${PYTHON_LIB_SITE_PACKAGES}


%define pip_name protobuf
Requires: py2-six py2-packaging py2-setuptools py2-pyparsing py2-appdirs
## IMPORT build-with-pip

