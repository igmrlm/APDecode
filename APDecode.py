import xml.etree.ElementTree as ET
import sys

DANGEROUS_PERMISSIONS = {
    "android.permission.READ_CALENDAR",
    "android.permission.WRITE_CALENDAR",
    "android.permission.CAMERA",
    "android.permission.READ_CONTACTS",
    "android.permission.WRITE_CONTACTS",
    "android.permission.GET_ACCOUNTS",
    "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.ACCESS_COARSE_LOCATION",
    "android.permission.RECORD_AUDIO",
    "android.permission.READ_PHONE_STATE",
    "android.permission.CALL_PHONE",
    "android.permission.READ_CALL_LOG",
    "android.permission.WRITE_CALL_LOG",
    "android.permission.ADD_VOICEMAIL",
    "android.permission.USE_SIP",
    "android.permission.PROCESS_OUTGOING_CALLS",
    "android.permission.BODY_SENSORS",
    "android.permission.SEND_SMS",
    "android.permission.RECEIVE_SMS",
    "android.permission.READ_SMS",
    "android.permission.RECEIVE_WAP_PUSH",
    "android.permission.RECEIVE_MMS",
    "android.permission.READ_EXTERNAL_STORAGE",
    "android.permission.WRITE_EXTERNAL_STORAGE"
}

POTENTIALLY_DANGEROUS_PERMISSIONS = {
    "android.permission.ACCESS_LOCATION_EXTRA_COMMANDS",
    "android.permission.ACCESS_NETWORK_STATE",
    "android.permission.ACCESS_WIFI_STATE",
    "android.permission.BLUETOOTH",
    "android.permission.BLUETOOTH_ADMIN",
    "android.permission.CHANGE_WIFI_STATE",
    "android.permission.CHANGE_NETWORK_STATE",
    "android.permission.CHANGE_WIFI_MULTICAST_STATE",
    "android.permission.GET_TASKS",
    "android.permission.INTERNET",
    "android.permission.KILL_BACKGROUND_PROCESSES",
    "android.permission.MODIFY_AUDIO_SETTINGS",
    "android.permission.NFC",
    "android.permission.READ_SYNC_SETTINGS",
    "android.permission.READ_SYNC_STATS",
    "android.permission.RECEIVE_BOOT_COMPLETED",
    "android.permission.REORDER_TASKS",
    "android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS",
    "android.permission.REQUEST_INSTALL_PACKAGES",
    "android.permission.SET_ALARM",
    "android.permission.SET_TIME_ZONE",
    "android.permission.SET_WALLPAPER",
    "android.permission.SET_WALLPAPER_HINTS",
    "android.permission.TRANSMIT_IR",
    "android.permission.USE_FINGERPRINT",
    "android.permission.VIBRATE",
    "android.permission.WAKE_LOCK",
    "android.permission.WRITE_SYNC_SETTINGS",
    "com.anddoes.launcher.permission.UPDATE_COUNT",
    "com.android.launcher.permission.INSTALL_SHORTCUT",
    "com.google.android.providers.gsf.permission.READ_GSERVICES",
    "com.google.android.gms.permission.ACTIVITY_RECOGNITION",
    "com.htc.launcher.permission.READ_SETTINGS",
    "com.htc.launcher.permission.UPDATE_SHORTCUT",
    "com.majeur.launcher.permission.UPDATE_BADGE",
    "com.sec.android.provider.badge.permission.READ",
    "com.sec.android.provider.badge.permission.WRITE",
    "com.sonyericsson.home.permission.BROADCAST_BADGE"
}

def check_permission(permission):
    if permission and permission.startswith("android.permission."):
        if permission in DANGEROUS_PERMISSIONS:
            return "\033[1;31;40m" + permission + " (Dangerous)" + "\033[0m"
        elif permission in POTENTIALLY_DANGEROUS_PERMISSIONS:
            return "\033[1;33;40m" + permission + " (Potentially dangerous)" + "\033[0m"
        else:
            return "\033[1;32;40m" + permission + " (Possibly normal)" + "\033[0m"
    elif permission:
        return "\033[1;36;40m" + permission + " (unknown)" + "\033[0m"
    else:
        return None



# Parse the manifest file
tree = ET.parse('AndroidManifest.xml')

# Get the root element, including the namespace
root = tree.getroot()

# Define the namespace for the "android" prefix
android_ns = {'android': 'http://schemas.android.com/apk/res/android'}

# Get all the permissions in the manifest
permissions = root.findall('.//uses-permission', android_ns)

# Check each permission and print the result
for p in permissions:
    name = p.get('name') or p.get('{' + android_ns['android'] + '}name')
    if name is not None:
        category = check_permission(name)
        if category:
            print(category)
