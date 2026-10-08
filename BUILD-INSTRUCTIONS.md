# WaveClock native build projects

This package contains **native app wrapper projects** for Android and Windows, using the WaveClock web app as the UI.

Important: this is source/build material, not precompiled APK/EXE installers. This execution environment did not have the Android SDK/Gradle or Electron build toolchain available, so binary installers could not be compiled or device-tested here.

## Android APK (Android Studio)
1. Install Android Studio and its Android SDK (API 35 recommended).
2. Open the `android` folder as an existing project.
3. Let Gradle sync and install any prompted SDK components.
4. Select Build → Build Bundle(s) / APK(s) → Build APK(s).
5. Install the generated APK from `android/app/build/outputs/apk/debug/app-debug.apk`.

The Android shell loads the app from local assets, so it does not need a hosted website. Notifications from the HTML app remain subject to Android WebView/browser limitations; timer sound/vibration while app is open are more dependable.

## Windows installer / portable EXE
1. Install Node.js LTS on Windows.
2. Open PowerShell in `windows-electron`.
3. Run `npm install`
4. Run `npm run dist`
5. Find the generated installer and portable app in `windows-electron/dist`.

## Current UI behavior
The app includes India Standard Time, stopwatch with optional milliseconds and laps, countdown timer, ocean wave animation, touch controls, keyboard shortcuts, and best-effort timer alert behavior.

## Sanity checks
The web UI source previously passed five static sanity tests. This package does not claim a full Android emulator or Windows installation test; please test the generated binaries on target devices.
