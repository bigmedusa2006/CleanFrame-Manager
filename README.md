# CleanFrame Manager

CleanFrame Manager is an independent experimental research-and-development project for studying and improving user-controlled Samsung Tizen TV home-screen workflows. It provides a guided Windows workflow for connecting to a TV in Developer Mode, reviewing installed content, and configuring an alternative launcher experience where supported.

> Use this project only on a television you own or are authorized to administer. TV firmware, model support, and available developer capabilities vary. Make a recovery plan before changing launcher or application settings.

> **Unofficial project:** CleanFrame Manager is independent software and is not affiliated with, endorsed by, or sponsored by Samsung Electronics Co., Ltd. Samsung and Tizen are trademarks of their respective owners.

![CleanFrame Manager application screenshot](cleanframe-manager-screenshot.png)

*CleanFrame Manager application screenshot for documentation and presentation. This is the CleanFrame Manager desktop application, not a photograph of a Samsung TV and not an official Samsung interface.*

## Current status

The latest packaged build is `v0.2.9`. It remains experimental and model-specific: a successful connection, temporary elevated access, or visible launcher change on one television does not prove compatibility with every Samsung TV.

The current Windows application provides a guided dashboard for entering a TV IP address, checking connection and Developer Mode state, reading available TV identity and firmware information, and reviewing the current home-screen assignment. It includes launcher management for the available Clear Home and CleanFrame/Google TV packages, including install, set-as-home, and home-assignment verification actions, plus Developer Mode guidance, free-RAM, TV self-diagnosis, restore-launcher, and reboot controls where supported.

The guided interface is provided by `tv_manager_v3.html` with the Windows backend in `manager_window.py`. Actions remain dependent on the TV model, firmware, network, Developer Mode, package compatibility, and Samsung platform behavior. Some operations may be unavailable or intentionally guarded, and the project does not guarantee compatibility, continued operation after firmware updates, or preservation of warranty coverage.

## Features

- Guided Windows dashboard for entering a TV IP address and connecting to a Samsung TV
- Connection, Developer Mode, TV identity, firmware, and home-assignment status checks
- Launcher Manager for selecting, installing, and setting supported Clear Home or CleanFrame/Google TV packages as Home
- Home-assignment verification before and after launcher changes
- Developer Mode setup guide and recovery-oriented status/checkpoint messaging
- Free-RAM, TV self-diagnosis, restore-Samsung-launcher, and reboot controls where supported
- Activity log with copy and clear controls
- Packaged Windows distribution in `dist-v0.2.9`

## Requirements

- Windows 10 or Windows 11
- A Samsung Tizen TV that you own or administer
- TV and computer on the same network
- Samsung TV Developer Mode enabled
- Network access permitted between the computer and TV
- For the packaged distribution: use the included `SamsungCleanFrameManager.exe`; Python is not required
- For source execution: Python 3.11 and the project dependencies are required

The TV must be configured for Developer Mode before installation or remote actions can work. Available actions and launcher packages vary by TV model, firmware, network state, and Samsung platform behavior.

## Packaged distribution

The current packaged build is under `dist-v0.2.9/SamsungCleanFrameManager/`. Launch `SamsungCleanFrameManager.exe` from that folder. Keep the `_internal` folder beside the executable; do not copy the executable out by itself.

The distribution also contains the launcher package files used by the application. Only install packages on a TV you own or are authorized to administer, and verify the selected launcher and recovery path before making it the Home application.

## Run from source

```powershell
Set-Location -LiteralPath 'D:\Samsung TV Project\CleanFrame Manager Workspace\CleanFrame Manager OG'
python manager_window.py
```

Install the source dependencies used by the project before running it. The exact connection and Developer Mode steps depend on the TV model and Tizen version. Follow the on-screen checks and do not continue when the application reports that a prerequisite is missing.

## Safety and recovery

CleanFrame Manager can affect the TV's application and launcher environment. Before using it:

1. Record the TV model, firmware version, and current launcher state.
2. Confirm that you can restore the original launcher or perform a TV reset if necessary.
3. Keep the original launcher and required recovery files available.
4. Use one checkpoint at a time and verify the TV after each change.
5. Stop if the TV identity, connection state, or permissions do not match the expected result.

Use only on a television you own or are authorized to administer. Do not use the project to access another person's TV, bypass access controls, or interfere with Samsung services or other users' devices.

Temporary elevated access should be treated as temporary. Do not assume that it survives a reboot or remains available after a firmware update.

## Supported models

There is no universal support guarantee. The `v0.2.9` distribution is intended for model-specific testing on Samsung Tizen TVs with Developer Mode enabled. Compatibility reports should include:

- Exact TV model code
- Tizen version and firmware version
- Developer Mode status
- CleanFrame Manager version
- The exact step that succeeded or failed
- Relevant application log output with personal information removed

## Project layout

```text
manager_window.py              Windows application backend
tv_manager_v3.html             Current guided interface
SamsungCleanFrameManager.spec  PyInstaller build configuration
CleanFrameManager-Setup.iss    Inno Setup configuration
dist-v0.2.9/                    Current packaged Windows distribution and launcher packages
cleanframe-manager-screenshot.png  CleanFrame Manager application screenshot for documentation
```

Build caches, temporary runtime data, local certificates, and machine-specific files are excluded from the source repository by default. The `dist-v0.2.9` directory is the explicit packaged distribution committed for this release. Check ownership and redistribution rights before adding any third-party package or Samsung-derived asset.

## Contributing

Please open an issue before submitting a large change. Do not include private TV addresses, credentials, certificates, signing keys, or logs containing personal information.

## License

This project is released under the MIT License. See [LICENSE](LICENSE).

## Disclaimer

This software is provided without warranty. The authors are not responsible for data loss, application loss, launcher failure, warranty impact, firmware problems, service interruption, or other damage resulting from its use. Samsung Electronics Co., Ltd. has not reviewed or approved this project.

The repository's screenshots, icons, wallpapers, and other media must be original, appropriately licensed, or used with permission. Third-party product names and logos remain the property of their respective owners and do not indicate endorsement.
