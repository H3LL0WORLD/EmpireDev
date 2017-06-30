# EmpireDev
#### [ES] Algunos módulos para el framework [Empire 2.0](https://github.com/empireproject/empire)
#### [EN] Some modules for the framework [Empire 2.0](https://github.com/empireproject/empire)
# 
## GetUACLevel
#### [ES] Obtener el nivel de notificación del UAC
#### [EN] Get the UAC notification level
#### [get_uac_level.py](lib/modules/powershell/collection/get_uac_level.py)
# 
## SetUACLevel
#### [ES] Establecer el nivel de notificación del UAC
#### [EN] Set the UAC notification level
#### [set_uac_level.py](lib/modules/powershell/collection/set_uac_level.py), [set_uac_level.ps1](data/module_source/collection/set_uac_level.ps1)
# 
## Hotfixes
#### [ES] Obtener el listado de los parches instalados usando WMI
#### [EN] Get the list of installed hotfixes using WMI
#### [hotfixes.py](lib/modules/powershell/collection/hotfixes.py)
# 
## Invoke-SDCLTBypass
#### [ES] Saltarse el UAC secuestrando el valor "IsolatedCommand" en "shell\runas\command", mas info [aqui](https://enigma0x3.net/2017/03/17/fileless-uac-bypass-using-sdctl-exe)
#### [EN] Bypasses UAC by hijacking the "IsolatedCommand" value in "shell unas\command", more info [here](https://enigma0x3.net/2017/03/17/fileless-uac-bypass-using-sdclt-exe)
#### [bypassuac_sdclt.py](lib/modules/powershell/privesc/bypassuac_sdclt.py), [Invoke-SDCLTBypass.ps1](data/module_source/privesc/Invoke-SDCLTBypass.ps1)
