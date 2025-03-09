# README.md

## Aufgabe öffentlicher Dienst

Die Aufgabe besteht darin, drei Standorte eines öffentlichen Dienstes aufzubauen. Die Standorte sind Stadtwerke, Rathaus und Polizeiwache. Jeder Standort soll 2-4 Abteilungen haben, wobei jede Abteilung mindestens 3 Rechner hat.

# Standort A: Stadtwerke
## Netzwerk 1: 192.168.0.0/24 
### SWITCH 2950-24 TT
für bis zu 24 PCs
### PT-Router
    IP 192.168.0.1

| Netzwerk|Nächster Hop  | 
|---|---|
|  192.168.1.0|192.168.1.2|


- **Abteilung 1**
    1. Rechner
    - IP 192.168.0.2
    2. Rechner 
    - IP 192.168.0.3
    3. Rechner
    - IP 192.168.0.4
- **Abteilung 2**
    1. Rechner
    - IP 192.168.0.5
    2. Rechner
    - IP 192.168.0.6 
    3. Rechner
    - IP 192.168.0.7

# Standort B: Rathaus
## Netzwerk 2: 192.168.1.0/24
### SWITCH 2960-24 TT
    24 PCs
### PT-Router
    IP 192.168.2.1

- **Abteilung 1**
    1. Rechner
    - IP 192.168.1.2
    2. Rechner
    - IP 192.168.1.3
    3. Rechner
    - IP 192.168.1.4

- **Abteilung 2**
    1. Rechner
    - IP 192.168.1.5
    2. Rechner 
    - IP 192.168.1.6
    3. Rechner
    - IP 192.168.1.7
- **Abteilung 3**
    1. Rechner 
    - IP 192.168.1.8
    2. Rechner
    - IP 192.168.1.9
    3. Rechner
    - IP 192.168.1.10
- **Abteilung 4**
    1. Rechner 
    - IP 192.168.1.11
    2. Rechner
    - IP 192.168.1.12
    3. Rechner
    - IP 192.168.1.13

# Standort C: Polizeiwache
## Netzwerk 3: 192.168.2.0/24
### SWITCH 2960-24 TT
    bis zu 24 PCs
### PT-Router
    IP 192.168.1.1

- **Abteilung 1**
    1. Rechner 
    - IP 192.168.2.2
    2. Rechner 2
    - IP 192.168.2.3
    3. Rechner 3
    - IP 192.168.2.4
- **Abteilung 2**
    1. Rechner
    - IP 192.168.2.5
    2. Rechner
    - IP 192.168.2.6
    3. Rechner
    - IP 192.168.2.7

