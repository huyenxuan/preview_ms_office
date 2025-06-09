import logging
import tempfile
import subprocess
import base64
import os
from odoo import http
from odoo.http import request
from werkzeug.exceptions import NotFound

_logger = logging.getLogger(__name__)

class OfficeToPDFPreview(http.Controller):

    @http.route("/preview-file/<int:attachment_id>", type="http", auth="user")
    def convert_office_to_pdf(self, attachment_id, **kwargs):
        attachment = request.env["ir.attachment"].sudo().browse(attachment_id)
        if not attachment.exists():
            raise NotFound()

        if not attachment.mimetype or not (
            attachment.mimetype.startswith("application/vnd")
            or attachment.mimetype.startswith("application/msword")
        ):
            return request.not_found()

        # Tạo file tạm
        with tempfile.TemporaryDirectory() as tmpdir:
            ext = "." + attachment.name.split(".")[-1]
            office_path = os.path.join(tmpdir, f"source{ext}")
            pdf_path = os.path.join(tmpdir, "source.pdf")

            with open(office_path, "wb") as f:
                f.write(base64.b64decode(attachment.datas))

            # Convert qua LibreOffice
            try:
                subprocess.run([
                    "libreoffice",
                    "--headless",
                    "--convert-to",
                    "pdf",
                    "--outdir",
                    tmpdir,
                    office_path
                ], check=True)

                if not os.path.exists(pdf_path):
                    raise Exception("Convert failed, PDF not found")

                with open(pdf_path, "rb") as pdf_file:
                    pdf_data = pdf_file.read()

                # Trả về file PDF
                return request.make_response(
                    pdf_data,
                    headers=[
                        ("Content-Type", "application/pdf"),
                        ("Content-Disposition", "inline; filename=%s.pdf" % attachment.name),
                    ]
                )
            except Exception as e:
                _logger.exception("❌ Failed to convert Office file to PDF: %s", e)
                raise NotFound()
