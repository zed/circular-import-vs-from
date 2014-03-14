"""`import lib.a` in `lib/b.py` works. `from libfrom import a` fails."""
import lib.a
import lib.b

lib.a.f()
lib.b.f()

import libfrom.a
import libfrom.b

libfrom.a.f()
libfrom.b.f()
