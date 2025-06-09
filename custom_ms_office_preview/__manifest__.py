{
    "name": "Custom MS Office Preview",
    "version": "1.0",
    "summary": "Preview office files using Microsoft Online Viewer",
    "description": """
    This module allows users to preview Microsoft Office files (such as Word, Excel, and PowerPoint) 
    directly within the Odoo interface using the Microsoft Online Viewer. 
    It extends the attachment model to recognize Office file types and provides a seamless viewing experience 
    by embedding the Office Viewer in the file preview interface.
    """,
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
    'author': 'XuanHuyen',
    "installable": True,
    "application": False,
}
