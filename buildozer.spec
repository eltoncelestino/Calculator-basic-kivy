[app]
title = My Calculator
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy, plyer
orientation = portrait
fullscreen = 0
android.permissions = VIBRATE, INTERNET, BATTERY_STATS
android.arch = armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
