#!/bin/sh
TOKEN_GITHUB=$1
pip install --upgrade --force-reinstall git+https://${TOKEN_GITHUB}@github.com/Monitoramento-Usinas-STEMIS/lib_tecsci_exceptions.git
