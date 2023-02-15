# APDecode

A Python script that parses an AndroidManifest.xml file and checks the level of danger for each permission requested.

## Usage

1. Install Python (version 3.0 or later)
2. Download the APDecode.py script to your local machine
3. Navigate to the directory where APDecode.py is located
4. Run the script by typing `python APDecode.py` in your terminal
5. The script will output a list of each permission requested in the AndroidManifest.xml file, along with its danger level (normal, possibly dangerous, or dangerous).

## Features

- Identifies 28 dangerous permissions and 35 possibly dangerous permissions based on Google's [official documentation](https://developer.android.com/guide/topics/permissions/overview#dangerous_permissions).
- Checks each permission in the AndroidManifest.xml file and prints the danger level of each one.
- Uses color coding to make it easy to identify the danger level of each permission (red for dangerous, yellow for possibly dangerous, green for normal, and cyan for unknown).
- Handles both standard and custom permission names, as long as they start with the "android.permission" prefix.

## Examples

Here are a few examples of how the script outputs permission levels:

- `android.permission.READ_EXTERNAL_STORAGE (dangerous)`
- `android.permission.ACCESS_FINE_LOCATION (possibly dangerous)`
- `android.permission.BLUETOOTH_ADMIN (possibly dangerous)`
- `com.example.myapp.custom_permission (unknown)`

## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use it however you like!

## Legal Disclaimer

This script is intended for research purposes only and should not be considered authoritative. While every effort has been made to ensure that the information provided by this script is accurate and up-to-date, it is not comprehensive and may not be applicable to all scenarios. The use of this script does not guarantee the safety or security of any application, device, or system. The author and publisher of this script shall not be liable for any direct, indirect, incidental, consequential, or punitive damages arising from the use of this script. Use of this script is at your own risk.
