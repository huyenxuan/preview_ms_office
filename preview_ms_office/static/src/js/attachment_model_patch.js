/** @odoo-module **/

import { Attachment } from "@mail/core/common/attachment_model";
import { patch } from "@web/core/utils/patch";
import { url } from "@web/core/utils/urls";


patch(Attachment.prototype, {
    get isMsOfficeDocument() {
        const officeMimeTypes = [
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document", // .docx
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", // .xlsx
            "application/vnd.openxmlformats-officedocument.presentationml.presentation", // .pptx
            "application/msword", // .doc
            "application/vnd.ms-excel", // .xls
            "application/vnd.ms-powerpoint", // .ppt
        ];
        return officeMimeTypes.includes(this.mimetype);
    },

    get isViewable() {
        return super.isViewable || this.isMsOfficeDocument;
    },


    get urlRoute() {
        if (this.isMsOfficeDocument) {
            return `/preview-file/${this.id}`;
        }
        return super.urlRoute;
    },

    get defaultSource() {
        if (this.isMsOfficeDocument) {
            return `/preview-file/${this.id}`;
        }
        console.log("Attachment mimetype:", this.mimetype);
        console.log("Office convertible:", this.isOfficeConvertible);
        console.log("Preview URL:", this.defaultSource);
        return super.defaultSource;
    },
});