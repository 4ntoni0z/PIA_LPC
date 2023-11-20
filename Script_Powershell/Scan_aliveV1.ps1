#Juan Antonio Sena Castillo
#1973595
#Grupo: 062

$portstoscan=@(20,21,22,23,50,53,60,119,110,135,80)
$waittime=100

Write-Host "Direccion ip a escanear: " -NoNewline
$direccion = Read-Host

foreach( $p in $portstoscan){

    $TCPObject= New-Object System.Net.Sockets.Tcpclient
        try{ $resultado = $TCPObject.ConnectAsync($direccion,$p).wait($waittime)}catch{}
        if ($resultado -eq "True")
        {
            Write-Host "Puertos abiertos: " -NoNewline; Write-Host $p -ForegroundColor Green

        }
}

$fecha= Get-Date
Write-Host $fecha
