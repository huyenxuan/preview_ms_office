{
    "name": "Preview MS Office",
    "version": "18.0",
    "summary": "Preview Office documents by converting them to PDF within Odoo",
    "description": '''
This module enables seamless previewing of Microsoft Office documents (Word, Excel, PowerPoint)
within Odoo by converting them to PDF on-the-fly using LibreOffice.

Instead of relying on external viewers like Microsoft Office Online, this approach ensures better privacy,
offline compatibility, and integration by leveraging Odoo's native PDF viewer. Attachments are converted
temporarily without storing additional files in the database, preserving storage and performance.
''',
    "depends": ["web"],
    "data": [
    ],
    "assets": {
        "web.assets_backend": [
            "custom_ms_office_preview/static/src/xml/file_viewer.xml",
            "custom_ms_office_preview/static/src/xml/mail_attachment_vew.xml",
            "custom_ms_office_preview/static/src/js/attachment_model_patch.js",
        ],
    },
    'price': 15.00,
    'currency': 'USD',
    'author': 'XuanHuyen',
    "installable": True,
    "application": False,
    'license': 'AGPL-3',
    'images': ['static/description/icon.png'],
}
