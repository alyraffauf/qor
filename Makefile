PREFIX 		?= /usr/
LIBINSTALLDIR 	?= /lib/
XDGCONFDIR 	?= /etc/xdg

make-install-dirs:
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	mkdir -p $(DESTDIR)$(PREFIX)/$(LIBINSTALLDIR)/alieninvasion
	mkdir -p $(DESTDIR)$(PREFIX)/share/applications
	mkdir -p $(DESTDIR)$(PREFIX)/share/alieninvasion
	mkdir -p $(DESTDIR)$(PREFIX)/share/alieninvasion/audio
	mkdir -p $(DESTDIR)$(PREFIX)/share/alieninvasion/images

install: make-install-dirs
	install -m 755 src/bin/alieninvasion $(DESTDIR)$(PREFIX)/bin/alieninvasion
	install -m 644 src/lib/alieninvasion/alieninvasion.py $(DESTDIR)$(PREFIX)/$(LIBINSTALLDIR)/alieninvasion/alieninvasion.py
	install -m 644 src/lib/alieninvasion/objects.py $(DESTDIR)$(PREFIX)/$(LIBINSTALLDIR)/alieninvasion/objects.py
	install -m 644 src/lib/alieninvasion/player.py $(DESTDIR)$(PREFIX)/$(LIBINSTALLDIR)/alieninvasion/player.py
	install -m 644 src/lib/alieninvasion/utils.py $(DESTDIR)$(PREFIX)/$(LIBINSTALLDIR)/alieninvasion/utils.py
	install -m 644 src/share/applications/alieninvasion.desktop $(DESTDIR)$(PREFIX)/share/applications/alieninvasion.desktop
	install -m 644 src/share/alieninvasion/audio/drillDownBySeveredFifth.ogg $(DESTDIR)$(PREFIX)/share/alieninvasion/audio/drillDownBySeveredFifth.ogg
	install -m 644 src/share/alieninvasion/audio/spaceInvadersByPornophonique.ogg $(DESTDIR)$(PREFIX)/share/alieninvasion/audio/spaceInvadersByPornophonique.ogg
	install -m 644 src/share/alieninvasion/images/asteroid.png $(DESTDIR)$(PREFIX)/share/alieninvasion/images/asteroid.png
	install -m 644 src/share/alieninvasion/images/background.png $(DESTDIR)$(PREFIX)/share/alieninvasion/images/background.png
	install -m 644 src/share/alieninvasion/images/enemyship.png $(DESTDIR)$(PREFIX)/share/alieninvasion/images/enemyship.png
	install -m 644 src/share/alieninvasion/images/spaceship.png $(DESTDIR)$(PREFIX)/share/alieninvasion/images/spaceship.png

clean:
	-find . -name "*.~[0-9]~" -exec rm -f {} \;
	-find . -name "*.py[co]" -exec rm -f {} \;
