#!/bin/bash
# install.sh

echo "Iniciando instalacao dos perfis do CIIA no Hermes..."

# Instala o Jo
hermes profile install ./profiles/jo --name jo --force -y

# Instala a Larissa
hermes profile install ./profiles/larissa --name larissa --force -y

# Instala o Vini
hermes profile install ./profiles/vini --name vini --force -y

echo "Todos os agentes (Jo, Larissa e Vini) foram instalados com sucesso!"
echo "Para conversar com um deles, use:"
echo "   hermes --profile jo"
echo "   hermes --profile larissa"
echo "   hermes --profile vini"
