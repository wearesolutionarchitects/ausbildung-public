---
marp: true
paginate: true
class: invert
---

# Vorbereitung OOP LEK Fragen

---

## Frage 1: Was ist das Hauptprinzip der objektorientierten Programmierung?

- [ ] Prozedurale Programmierung
- [ ] Vererbung
- [x] Kapselung
- [ ] Datenbankmanagement

---

## Frage 2: Was ist ein Objekt?

- [ ] Eine Funktion
- [ ] Ein Attribut
- [ ] Ein Wert
- [x] Eine Instanz einer Klasse

---

## Frage 3: Was ist eine Klasse?

- [ ] Ein Attribut
- [x] Eine Vorlage zur Erstellung von Objekten
- [ ] Ein Objekt
- [ ] Eine Funktion

---

## Frage 4: Was bezeichnet man als "Methodenüberladung"?

- [x] Das Erstellen mehrerer Methoden mit demselben Namen und unterschiedlichen Parametern
- [ ] Das Ersetzen einer Methode in einer abgeleiteten Klasse
- [ ] Das Erstellen einer Methode, die keine Parameter hat
- [ ] Das Zusammenfassen von mehreren Methoden in einer Klasse

---

## Welches der Schlüsselwort wird verwendet, um ein Attribut einer Klasse zugänglich zu machen?

```python
class Person:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
```

- [ ] public
- [ ] private
- [ ] protected
- [x] self

---
