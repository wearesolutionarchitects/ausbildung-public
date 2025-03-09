ComputerWeekly.de.com
Automatisierter Test
von Alexander S. Gillis
Automatisiertes Testen ist ein Prozess, mit dem überprüft wird, ob eine Software ordnungsgemäß funktioniert und die Anforderungen erfüllt, bevor sie für den produktiven Einsatz freigegeben wird. Diese Testmethode verwendet geskriptete Sequenzen, die von Testwerkzeugen ausgeführt werden. Automatisierte Testwerkzeuge führen Prüfungen der Software durch, berichten über die Ergebnisse und vergleichen die Ergebnisse mit früheren Testläufen.

Ein Unternehmen kann automatisierte Tests für ein breites Spektrum von Fällen anwenden, zum Beispiel für Unit-, API- und Regressionstests. Der Hauptvorteil automatisierter Softwaretests besteht darin, dass ein möglichst großer Teil des manuellen Aufwands in einer Reihe von Skripten zusammengefasst werden kann. Wenn beispielsweise Unit-Tests einen großen Teil der Ressourcen eines Qualitätssicherungsteams in Anspruch nehmen, sollte dieser Prozess als Kandidat für eine Automatisierung bewertet werden.

Automatisierte Tests können wiederholt und zu jeder Tageszeit durchgeführt werden. Dieser Ansatz passt zu den Praktiken des kontinuierlichen Testens sowie der kontinuierlichen Integration (Continuous Integration, CI) und der kontinuierlichen Bereitstellung (Continuous Deployment, CD) der Softwareentwicklung, die darauf abzielen, Codeänderungen ohne manuelle Eingriffe in die Produktion zu überführen.

Vorteile des automatisierten Testens
Automatisiertes Testen kann die Effizienz eines Qualitätssicherungsteams steigern. Einige Vorteile sind:

höhere Genauigkeit
bessere Berichtsmöglichkeiten
erhöhte Abdeckung
verbesserte Ressourceneffizienz
verbesserte Fehlererkennung
erhöhte Wiederverwendbarkeit
Wenn ein Softwaretester ein System manuell prüft, kann ihm ein Fehler unterlaufen, insbesondere wenn eine Anwendung Hunderte bis Tausende von Codezeilen enthält. Die Automatisierung hilft dem Qualitätssicherungsteam, diese menschlichen Fehler beim Testen von Anwendungen zu vermeiden, und führt die Prüfungen in einem schnelleren Zeitrahmen durch, als wenn sie von Menschenhand durchgeführt würden.

Einige Testautomatisierungs-Tools verfügen über Berichtsfunktionen, die jedes Testskript protokollieren, um den Benutzern den Status jedes Tests zu zeigen. Ein Tester kann dann die Ergebnisse mit anderen Berichten vergleichen, um zu beurteilen, wie die Software im Vergleich zu den Erwartungen und Anforderungen funktioniert.

Insgesamt ermöglichen automatisierte Tests den Mitarbeitern, manuelle Tests zu vermeiden und sich auf andere Projektprioritäten zu konzentrieren. Ein Qualitätssicherungsteam kann automatisierte Testskripte wiederverwenden, um sicherzustellen, dass jede Prüfung jedes Mal auf die gleiche Weise ausgeführt wird. Darüber hinaus helfen automatisierte Tests dem Team, Fehler in den frühen Phasen der Entwicklung schnell zu finden, was die Gesamtarbeitszeit und die Projektkosten reduziert.

Missverständnisse über automatisierte Tests
Zu den Missverständnissen über automatisierte Tests gehören:

Automatisiertes Testen verschafft Entwicklern mehr freie Zeit. In Wirklichkeit verschafft das automatisierte Testen den Entwicklern mehr Zeit, um sich auf größere Probleme im Entwicklungsprozess zu konzentrieren.
Automatisiertes Testen ist dem manuellen Testen überlegen. Automatisiertes und manuelles Testen haben beide ihre Vorteile, und das umfassendste Verständnis einer Anwendung wird durch den Einsatz beider Techniken erreicht.
Automatisiertes Testen verhindert die menschliche Interaktion. In Wirklichkeit können automatisierte Tests die Konversation verbessern, indem sie neue Kommunikationskanäle eröffnen.
Automatisiertes Testen ist zu teuer. Es stimmt, dass die anfängliche Investition kostspielig sein kann, aber im Laufe der Zeit machen sich die Vorteile der Methode bezahlt, indem sie die Kosten für Code-Revisionen und manuelle Testwiederholungen reduzieren.
Wie funktioniert automatisiertes Testen?
Ein Unternehmen implementiert die Testautomatisierung mit einem Framework, das Best Practices, Testwerkzeuge und Standards umfasst. Datengesteuerte und schlüsselwortgesteuerte Testautomatisierungs-Frameworks sind weit verbreitet, ebenso wie Frameworks für lineares Scripting und modulare Tests.

Das Framework für lineares Skripting eignet sich für kleine Anwendungen, da es die Verwendung eines Testskripts mit wenig Planung ermöglicht, aber keine wiederverwendbaren Skripte unterstützt. In modularen Test-Frameworks erstellt ein Softwaretester Skripte als kleine, unabhängige Tests, um Redundanzen zu vermeiden, aber dieser Prozess nimmt in der Regel mehr Zeit in Anspruch.

Mit datengesteuerten Frameworks können Softwaretester Skripte erstellen, die für mehrere Datensätze funktionieren und mit weniger Tests als bei modularen Optionen eine breite Qualitätsabdeckung bieten. Schlüsselwortgesteuerte Test-Frameworks verwenden Tabellenformate, um Schlüsselwörter für jede Funktion und Ausführungsmethode zu definieren. Softwaretester ohne umfassende Programmierkenntnisse können mit den Schlüsselwörtern arbeiten, um Testskripte zu erstellen. Hybride Frameworks kombinieren zwei oder mehr Verfahren, um die Vorteile beider Verfahren zu nutzen.

Zu den Open-Source-Tools und -Frameworks für die Testautomatisierung gehören Selenium, Robotium und Cypress. Selenium kann Testparameter über mehrere Webbrowser und in verschiedenen Programmiersprachen, wie zum Bespiel C#, Java und Python, automatisieren und ausführen. Robotium unterstützt Tester beim Schreiben von automatischen Benutzerakzeptanz-, Funktions- und Systemtests für Android-Geräte. Cypress deckt End-to-End-, Integrations- und Unit-Tests ab, alles innerhalb eines Browsers. Cypress ermöglicht den Zugriff auf verteilte Objektmodelle im Browser und bietet einen Debugger für weitere Tests.

Best Practices für automatisierte Tests
Automatisiertes Testen ist am vorteilhaftesten, wenn es angewendet wird auf:

Tests, die auf verschiedenen Hardware- oder Softwarekonfigurationen oder Plattformen durchgeführt werden
sich wiederholende Tests, die für verschiedene Builds verwendet werden
Tests mit mehreren Datensätzen
Tests, die manuell nicht durchführbar sind
Tests, die bei manueller Durchführung zu mühsam und zeitaufwändig sind
Tests für häufig genutzte Funktionen, die Bedingungen einführen, die das Risiko erhöhen
Tests, die häufig zu menschlichen Fehlern führen.
Weitere Best Practices sind:

frühzeitiges und häufiges Testen der Software
Auswahl des richtigen Tools für automatisierte Tests
Erstellung automatisierter Tests, die Änderungen an der Benutzeroberfläche (UI) standhalten können
separate Durchführung der automatisierten Tests
Kontinuierliche Tests
Die Grundlagen einer CI/CD-Pipeline

Unternehmen binden automatisierte Tests in der Regel in eine kontinuierliche Teststrategie ein, bei der in jedem Schritt der Softwareentwicklungs- und -bereitstellungspipeline Codeprüfungen durchgeführt werden. Kontinuierliche und automatisierte Tests helfen Unternehmen dabei, Leistungsengpässe zu reduzieren, da die Arbeit nicht von Anfang an, sondern kontinuierlich erfolgt. So kann ein Unternehmen beispielsweise Softwareänderungen mit automatisierten und kontinuierlichen Tests alle paar Stunden freigeben, anstatt alle paar Tage mit einem manuellen und kontrollierten System.

Continuous-Delivery- und Continuous-Integration-Pipelines nutzen automatisierte Tests und Bereitstellungsprozesse, die es den Entwicklern ermöglichen, den Code dann bereitzustellen, wenn er fertig ist, und nicht erst, wenn das System für die Bereitstellung verfügbar ist. CI beinhaltet häufige und isolierte Codeänderungen sowie sofortige Tests in jeder Phase der Fertigstellung, bevor die CI-Pipeline eine Aktualisierung zu einer größeren Codebasis hinzufügt. CD ermöglicht es, ausführbare Code-Updates in Staging- oder Produktionsumgebungen live zu schalten. In der Regel ist jeder Commit, der automatisierte Integrationstests oder andere Formen von großen Tests besteht, ein gültiger Kandidat für die Veröffentlichung.

Automatisierte Tests und Unit-Tests
Ein Unit-Test ist eine andere Software-Testmethode, die mit automatisierten Tests kombiniert werden kann. Beim Unit-Test wird der kleinste Teil einer Anwendung untersucht, um die Funktionalität sicherzustellen. Manchmal wird dabei jede Codezeile als separater Teil und nicht als Teil der gesamten Anwendung geprüft. Dies kann zwar helfen, Fehler zu vermeiden, schränkt aber die Bewertung der Gesamtlösung ein.

Wenn Unit-Tests manuell durchgeführt werden, können sie sehr zeitaufwändig sein und das Risiko menschlicher Fehler erhöhen. Darüber hinaus verhindern manuelle Unit-Tests den kollaborativen und umfassenden Ansatz bei der Softwareentwicklung, der durch die DevOps-Kultur populär geworden ist.

Durch die Automatisierung von Unit-Tests können mehrere Testfälle ausgeführt werden, während jede Codezeile geschrieben wird. Dadurch erhalten die Entwickler ein besseres Verständnis für die Gesamtintegrität der Software und den potenziellen Wert für die Endbenutzer während der Entwicklung. Darüber hinaus lassen sich die zuvor erörterten Vorteile automatisierter Tests auch auf die Automatisierung von Unit-Tests anwenden: Das Risiko menschlicher Fehler wird drastisch reduziert und die Zeit, die für die wiederholte Ausführung der Tests benötigt wird, verringert sich erheblich.

Automatisiertes Testen versus manuelles Testen
Manuelles Testen ist das genaue Gegenteil von automatisiertem Testen; es beinhaltet, dass Menschen alle Tests für die Software schreiben und durchführen. Dieser Mehraufwand mag zwar wie ein Nachteil erscheinen, doch profitieren die Entwickler von der Möglichkeit, Erkenntnisse aus der Untersuchung jedes einzelnen Prozessschritts zu ziehen, da sie die Software mittels SQL- und Protokollanalyse durchgehen, Nutzungs- und Eingabekombinationen testen, die gesammelten Ergebnisse mit dem geplanten Verhalten vergleichen und alle Ergebnisse aufzeichnen müssen.

Im Gegensatz dazu werden bei automatisierten Tests, sobald der Test geschrieben ist, alle Zwischenschritte ausgeblendet und der Schwerpunkt liegt auf der Bereitstellung des Endergebnisses. Dadurch können die Tests jedoch wiederholt ohne die Hilfe von Entwicklern durchgeführt werden, was ein kontinuierliches Testen ermöglicht. Im Gegensatz dazu müssen die Entwickler beim manuellen Testen jeden Schritt des Prozesses für jeden Test, der in einem bestimmten Bereich wiederholt werden muss, ständig wiederholen.

Außerdem werden automatisierte Tests häufig nach der Entwicklung der Software eingesetzt, um längere Tests durchzuführen, die bei den ersten manuellen Tests vermieden wurden. Wenn sie automatisiert sind, können diese langen Tests unbeaufsichtigt auf mehreren Computern mit verschiedenen Konfigurationen laufen.

25 Okt. 2022

Alle Rechte vorbehalten, Copyright 2013 - 2024, TechTarget | Lesen Sie unsere Datenschutzerklärung