from pathlib import Path
import json, re, unittest
ROOT=Path(__file__).parent
HTML=(ROOT/"index.html").read_text(encoding="utf-8")
class AppSanityTests(unittest.TestCase):
    def test_pwa_files_exist(self):
        for name in ["index.html","manifest.webmanifest","service-worker.js","icon.svg"]:
            self.assertTrue((ROOT/name).is_file(), name)
    def test_manifest_is_valid_json(self):
        data=json.loads((ROOT/"manifest.webmanifest").read_text(encoding="utf-8"))
        self.assertEqual(data["display"],"standalone")
        self.assertTrue(data["icons"])
    def test_required_features_present(self):
        for text in ["Asia/Kolkata","Stopwatch","Countdown timer","showMs","Notification.requestPermission","serviceWorker.register","requestAnimationFrame","beforeinstallprompt","addLap"]:
            self.assertIn(text,HTML)
    def test_timer_guards_zero_duration(self):
        self.assertIn('if(timerRemaining<=0){toast("Set a timer longer than zero");return}',HTML)
    def test_keyboard_and_accessibility(self):
        for text in ['e.code==="Space"','e.key.toLowerCase()==="l"','aria-live="polite"','aria-selected']:
            self.assertIn(text,HTML)
if __name__=="__main__": unittest.main(verbosity=2)
