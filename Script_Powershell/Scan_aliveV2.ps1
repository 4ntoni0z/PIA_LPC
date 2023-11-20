#Juan Antonio Sena Castillo
#1973595
#Grupo 062

#dterminando el gateway
$subred= (Get-Netroute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Loading ..."
Write-Host "Tu gateway es:"$subred
#determinaso el rango del getway
$rango = $subred.Substring(0,$subred.IndexOf('.')+1+$subred.Substring($subred.IndexOf('.')+1).IndexOf('.')+3)
echo $rango

$punto=$rango.EndsWith('.')
if ($punto -like "False") {
    <# Action to perform if the condition is true #>
    $rango = $rango + '.'

}
$rango_ip=@(1..10)


Write-Output ""
Write-Host "-- Subred Actual:"
Write-Host "Escaneando: " -NoNewline ; Write-Host $rango -NoNewline; Write-Host "0/24" -ForegroundColor Red
Write-Output ""

foreach( $r in $rango_ip){
    $actual = $rango+$r
    $responde = Test-Connection $subred -Quiet -Count 1
    if ($responde -eq "True") {
        <# Action to perform if the condition is true #>
        Write-Output ""
        Write-Host "host responde: " -NoNewline; Write-Host $actual -ForegroundColor Green

    }
}


$fecha= Get-Date
Write-Host $fecha












