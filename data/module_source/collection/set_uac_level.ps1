Function Set-UACNotificationLevel {
<#
.SYNOPSIS
Cambia el nivel de notificacion de control de cuentas de usuario.

.DESCRIPTION
Cambia el nivel de notificacion de control de cuentas de usuario, cambiando la clave en el registro.

.PARAMETER Level
Nivel al que se cambiará el nivel de notificación del UAC

.EXAMPLE
 Set-UAC -Level 3
Cambia el nivel de notificacion del UAC a 3 (Notificar siempre)

.EXAMPLE
 Set-UAC 2
Cambia el nivel de notificacion del UAC a 2

#>
    Param (
        [Parameter(Mandatory = $False, Position = 0)]
        [Int] $Level = 0
    )

    function IsAdmin {
        return (New-Object Security.Principal.WindowsPrincipal ([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
    }

    $UACLevels = (
        (0, 0),
        (5, 0),
        (5, 1),
        (2, 1)
    )

    if (-Not (IsAdmin)) {
        return '[!] Error: Se necesitan permisos de administrator'
    }
    
    if ($Level -gt 3 -or $Level -lt 0) {
        return "[!] Error: Valor Invalido`n[>] Valores validos: 0, 1, 2, 3"
    } else {
        
        $UACLevel = $UACLevels[$Level]
        
        $Path = 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
        
        Set-ItemProperty -Path $Path -Name 'ConsentPromptBehaviorAdmin' -Value $UACLevel[0] -Force
        Set-ItemProperty -Path $Path -Name 'PromptOnSecureDesktop' -Value $UACLevel[1] -Force
        return '[>] Done'
    }
}
