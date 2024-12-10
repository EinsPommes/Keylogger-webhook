# Python Keylogger mit Discord Webhook

Ein Keylogger implementiert in Python, der Tastatureingaben aufzeichnet und über Discord Webhooks sendet. Entwickelt für Bildungszwecke und ethische Tests.

## ⚠️ Wichtiger Hinweis

Dieser Keylogger wurde zu Bildungszwecken entwickelt. Die Verwendung von Keyloggern ohne Einwilligung der betroffenen Personen ist in den meisten Ländern illegal. Verwenden Sie diesen Code nur in einer kontrollierten Testumgebung oder mit ausdrücklicher Genehmigung.

## 🔍 Funktionen

- Aufzeichnung von Tastatureingaben
- Automatisches Senden der Logs über Discord Webhook
- Lokale Speicherung der Logs in einer Datei
- Getarnt als "System Updater"
- Einfache und verständliche Implementierung

## 📋 Voraussetzungen

- Python 3.x
- pynput Bibliothek
- requests Bibliothek
- Ein Discord Server mit Webhook-URL

## 🛠️ Installation

1. Klonen Sie das Repository:
```bash
git clone https://github.com/IhrUsername/keylogger.git
cd keylogger
```

2. Installieren Sie die erforderlichen Abhängigkeiten:
```bash
pip install -r requirements.txt
```

3. Konfigurieren Sie Ihren Discord Webhook:
   - Erstellen Sie einen Webhook in Ihrem Discord Server
   - Fügen Sie die Webhook-URL in die Konfiguration ein

## 💻 Verwendung

1. Starten Sie den Keylogger:
```bash
python SystemUpdater.py
```

2. Der Keylogger läuft im Hintergrund und:
   - Zeichnet Tastatureingaben auf
   - Sendet die Logs automatisch an Ihren Discord Channel
   - Speichert die Logs lokal in `keylog.txt`

## 🛑 Beenden

- Drücken Sie `Esc`, um den Keylogger zu beenden
- Die aufgezeichneten Daten werden automatisch gespeichert

## 📝 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

## ⚖️ Rechtlicher Hinweis

Die Verwendung von Keyloggern kann rechtliche Konsequenzen haben. Stellen Sie sicher, dass Sie:
- Die Zustimmung aller beteiligten Parteien haben
- Die lokalen Gesetze und Vorschriften einhalten
- Das Tool nur für legale und ethische Zwecke verwenden

## 🤝 Beitragen

Beiträge sind willkommen! Bitte erstellen Sie einen Pull Request oder öffnen Sie ein Issue für Vorschläge und Verbesserungen.
