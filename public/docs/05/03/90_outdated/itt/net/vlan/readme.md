# Cisco-VLAN-Befehle für Switche 

## Modi:
1. **User Exec Mode**: Einfache show-Befehle für jeden
    ```
    Switch>
    ```
2. **Privileged Exec Mode**: Erweiterte show-Befehle für Administratoren
    ```
    Switch>enable
    Password (falls ein Passwort eingerichtet wurde)
    Switch#
    ```
3. **Global Config Mode**: Globaler Konfigurationsmodus für allgemeine Switcheinstellungen
    ```
    Switch#configure terminal
    Switch#(config)
    ```

## Switchnamen vergeben:
    ```
    Switch(config)#hostname Switch1
    Switch1(config)#
    ```

## Passworte setzen:
1. Zugriff zum privileged exec mode:
    ```
    Switch(config)#enable password <password> (nicht verschlüsselt)
    Switch(config)#enable secret <password>       (verschlüsselt)
    Passwortverschlüsselung auch im show-Befehl:
    Switch(config)#service password-encryption
    Switch(config)#no service password-encryption
    ```
2. Switchzugriffspassword (enable-Password)

## Konsole:
    ```
    Switch(config)#line console 0
    Switch(config-line)#password <password>
    Switch(config-line)#login
    ```
## Virtual Terminal Line (0-4) (remote, z.B. telnet)
    ```
    Switch(config)#line vty 0 4
    Switch(config-line)#password <password>
    Switch(config-line)#login 
    ```

## VLANs erstellen 
1. global configuration mode aktivieren
2. interface mode aktivieren
## VLANs erstellen und benennen
    ```
    Switch(config)#vlan 2
    Switch(config-vlan)#name Verkauf
    Switch(config-vlan)#vlan 3
    Switch(config-vlan)#name Einkauf
    ```
## VLANs entfernen (löschen)
    ```
    Switch(config)#no vlan 2 (die meisten Befehle können 
                        mit einem vorgesetzten no rückgängig gemacht werden)
    ```
## Interface einem VLAN als Access-Port zuordnen
    ```
    Switch(config)#interface fa0/0
    Switch(config-if)#switchport mode access vlan 2
    Switch(config-if)#no shutdown    - Port permanent aktiv (bei switches eher nicht nötig)
    Switch(config-if)#interface fa0/1
    Switch(config-if)#switchport mode access vlan 3
    Switch(config-if)#no shutdown    - Port permanent aktiv (bei Switches eher nicht nötig)
    ```
## Interface als Trunk-Port einrichten
    ```
    Switch(config)#interface fa0/2
    Switch(config-if)#switchport mode trunk
    Switch(config-if)#switchport trunk allowed vlan add 2
    Switch(config-if)#switchport trunk allowed vlan add 3    - statt add 2 und add 3
                                               auch all (für alle)
    ```

## Konfigurationsänderungen im Switch speichern 
    ```
    Switch#copy running-config startup-config
    ```

## Wichtige Befehle zum Überprüfen der Funktionalität:
    ```
    Switch# show running-config        ->    zeigt alle Einstellungen des Routers
    ```
