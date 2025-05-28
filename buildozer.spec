version = 0.1

# (list) Requisiti Python / Android
requirements = python3,kivy

# (str) API minima Android (minSdkVersion)
android.minapi = 21

# (str) SDK target Android
android.api = 31

# (int) Versione SDK build tools
android.sdk = 30

# (int) Versione NDK
android.ndk = 25b

# (int) NDK API level
android.ndk_api = 21

# (str) Permessi Android (aggiungi se servono)
android.permissions = INTERNET

# (bool) Usa SDL2 bootstrap (necessario per Kivy moderno)
android.bootstrap = sdl2

# (bool) Abilita debug
log_level = 2

# (str) Directory di output per la build
bin_dir = bin

# (bool) Abilita il debug della JVM Java (opzionale)
android.debug = True
