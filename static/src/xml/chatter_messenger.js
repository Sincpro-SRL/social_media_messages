odoo.define(
    "sincpro_whatsapp/static/src/xml/chatter_messenger.js",
    function (require) {
        "use strict";

        const components = {
            ChatterTopbar: require("mail/static/src/components/chatter_topbar/chatter_topbar.js"),
        };
        const container = require("mail/static/src/components/chatter_container/chatter_container.js");
        const rpc = require("web.rpc");
        const {clear} = require("mail/static/src/model/model_field_command.js");

        const {patch} = require("web.utils");

        patch(
            components.ChatterTopbar,
                "sincpro_whatsapp/static/src/xml/chatter_messenger.js",
            {
                /**
                 * @private
                 * @param {MouseEvent} ev
                 */
                _onClickMessenger(ev) {
                    console.log("Entrando a Messenger")
                },
            }
        );

        container.prototype._insertFromProps = function (props) {
        const values = Object.assign({}, props);
        rpc.query({
            model: "crm.lead",
            method: "get_data_from_model",
            args: [],
        }).then((result) => {
//            values.isSendMessage = result;
            console.log(values);
            if (values.threadId === undefined) {
                values.threadId = clear();
            }
            if (!this.chatter) {
                this.chatter = this.env.models["mail.chatter"].create(values);
            } else {
                this.chatter.update(values);
            }
        });
        }
    }
);