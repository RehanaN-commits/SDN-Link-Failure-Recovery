from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# Handle packets
def _handle_PacketIn(event):
    packet = event.parsed
    in_port = event.port
    dpid = event.dpid

    msg = of.ofp_flow_mod()
    msg.match.in_port = in_port

    # Flood packets (basic forwarding)
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

    event.connection.send(msg)
    log.info(f"[DPID {dpid}] Packet received on port {in_port} -> FLOOD")

# Handle link/port status changes
def _handle_PortStatus(event):
    ofp = event.ofp

    if ofp.reason == of.OFPPR_DELETE:
        log.info("Link DOWN detected!")

    elif ofp.reason == of.OFPPR_ADD:
        log.info("Link UP detected!")

    elif ofp.reason == of.OFPPR_MODIFY:
        log.info("Link status modified!")

# Launch function
def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    core.openflow.addListenerByName("PortStatus", _handle_PortStatus)

    log.info("Link Failure Detection Controller Started")