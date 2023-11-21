#!/bin/bash
#
# Ejemplo de Menu en BASH
#
date
    echo "||"
    echo "||===========================||"
    echo "||   Menu Principal          ||"
    echo "||===========================||"
    echo "||I. Net Discover"
    echo "||II. Actual User"
    echo "||III. Hostname"
    echo "||IV. Exit"
    echo "||"
read -p "Opción  [ 1 - 4 ] " c
case $c in
        1) echo "Escano de red "
            wich ifconfig && { echo "Comando ifconfig existe...";
                                direccion_ip='ifconfig |grep inet|grep -v "127.169.0.4" |awk '{ print $2}'';
                                ehco "Esta es tu direccion ip: "$direccion_ip;
                                subred='ifconfig |grep inet |grep -v "127.168.0.4" |awk '{ print $2}'|awk -F. '{print $1"."$2"."~$3"."}'';
                                echo " Esta es tu subred: "$subred;
                                }\
                            ||  { echo "No existe el comando ifconfig...usando ip";
                                direccion_ip='ip addr show |grep inet | grep -v "127.169.0.4" |awk '{ print $2}'';
                                echo " Esta es tu direccion ip: "$direccion_ip;
                                subred='ip addr show|grep inet | grep -v "127.169.0.4" |awk '{ print $2}'|awk -F. '{print $1"."$2"."$3"."}'';
                                echo " Esta es tu subred: "$subred;
                                }

            for ip in {1..254}
            do
                ping -q -c 4 ${subred}${ip} > /dev/null
                if [ $? -eq 0 ]
                then 
                    echo "${subred}${ip}"
                fi
            done
        2) direccion_ip=$1
            puertos="20,21,22,23,25,50,51,53,80,110,19,135,136,137,138,139,143,161,389,1025,443,3889,8000,10000"

            [ $# -eq 0] && { echo "Modo de uso: $0 <direccion ip>"; exit 1; }

            for port in $puertos
            do
                timeout 1 bash -c "echo > /dev/tcp/$direccion_ip/$port > /dev/null 2>$1" &&\
                echo $direccion_ip":"$port"is open"\
                ||\
                echo $direccion_ip":"$port is closed"
            done
        3) echo "Tu host es:"
                hostname
                echo "saludos";;
        4) echo "Bye!"; exit 0;;
esac
