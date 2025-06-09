# Custom MS Office Preview

## Overview
This module allows users to preview Microsoft Office files (such as Word, Excel, and PowerPoint) directly within the Odoo interface using the Microsoft Online Viewer. It extends the attachment model to recognize Office file types and provides a seamless viewing experience by embedding the Office Viewer in the file preview interface.

## Features
- Preview Microsoft Office files (Word, Excel, PowerPoint) within Odoo.
- Extends the attachment model to recognize Office file types.
- Embeds the Microsoft Online Viewer in the file preview interface.

## Installation
1. Clone the repository into your Odoo addons directory:
    ```sh
    git clone https://github.com/quodoo/odoo_addons.git
    ```
2. Update your Odoo configuration file to include the new module directory.
3. Restart the Odoo server.
4. Install the "Custom MS Office Preview" module from the Apps menu.

## Usage
1. Upload a Microsoft Office file (Word, Excel, PowerPoint) as an attachment in Odoo.
2. Open the attachment to preview it using the Microsoft Online Viewer.

## Configuration
No additional configuration is required.

## Technical Details
- **Controller**: Handles the public URL for previewing attachments.
- **JavaScript**: Patches the attachment model to recognize Office file types and generate the appropriate preview URL.
- **XML**: Extends the file viewer templates to embed the Microsoft Online Viewer.

## Warning
The controller makes all attachments public. You can create a guest token for a public link that allows the Microsoft preview to show the attachment. If you need help, contact me.

## Author
### Quang Trinh
![Contact me on Zalo](../zalo.jpg)

## Support
If you find this module helpful, please consider buying me a coffee to keep me motivated.

![Buy me a coffee](../tpbank_qr.jpg)