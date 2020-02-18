# Salonwand
Programmeer de timing van videos en fotos met RPi, omxplayer en python
De videos en timing staan op diverse RPi's in de een netwerk krijgen een startcommando
via een rpyc server

slaves : RPi met omxplayer en rpyc server

master : RPi met omxplater en thread_timer.py
          thread_timer.py om de videos op de RPi's te starten
