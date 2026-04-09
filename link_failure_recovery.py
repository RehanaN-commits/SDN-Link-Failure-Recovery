from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PacketIn(event):
    packet = event.parsed
    in_port = event.port

    msg = of.ofp_flow_mod()
    msg.match.in_port = in_port

    # Flood if unknown
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

    event.connection.send(msg)
    log.info(f"Packet from port {in_port} forwarded")

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
