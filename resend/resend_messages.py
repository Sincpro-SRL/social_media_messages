import logging

from ..dispatcher.dispatcher import dispatch
from ..dispatcher.actions import FB_SEND_MESSAGE

_logger = logging.getLogger(__name__)


def resend_message(registers_not_sent, token):
    for register in registers_not_sent:
        if register.attempts < 3:
            response = dispatch(
                FB_SEND_MESSAGE,
                data={"message": register.customer_message},
                id_facebook=register.contact.id_facebook,
                token=token,
            )
            register.write({"attempts": register.attempts + 1})
            if response.status_code == 200:
                register.write({"status_message": "SENT"})
        else:
            _logger.info("Verificar mensaje no enviado: " + register)
