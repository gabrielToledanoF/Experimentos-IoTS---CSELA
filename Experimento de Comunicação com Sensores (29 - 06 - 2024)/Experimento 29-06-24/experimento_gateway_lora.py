from pyLoraRFM9x import LoRa, ModemConfig
import time

# This is our callback function that runs when a message is received
def on_recv(payload):
    print("From:", payload.header_from)
    print("Received:", payload.message)
    print("Msg:", payload.header_id)
    #for i in range(len(payload.message)):
    #	    print(payload.message[i], end='')
    print()
    print("RSSI: {}; SNR: {}".format(payload.rssi, payload.snr))
    lora.send_ack(payload.header_to, payload.header_id)
    print("ACK SENT to ")
    lora.set_mode_rx()  
    time.sleep(5)

# Use chip select 1. GPIO pin 5 will be used for interrupts and set reset pin to 25
# The address of this device will be set to 2
#lora = LoRa(0, 5, 2, reset_pin = 25, modem_config=ModemConfig.Bw125Cr45Sf128, tx_power=14, acks=False)
#lora = LoRa(1, 5, 2, reset_pin = 25, modem_config=ModemConfig.Bw125Cr45Sf128, tx_power=20, acks=False, receive_all=True, default_mode=0)
lora = LoRa(1, 5, 2, reset_pin = 25, modem_config=ModemConfig.Bw125Cr48Sf4096, tx_power=18, acks=False, receive_all=True)
lora.on_recv = on_recv
#lora.set_mode_cad()
lora.set_mode_rx()  

# Send a message to a recipient device with address 10
# Retry sending the message twice if we don't get an  acknowledgment from the recipient
message = "Hello there!/n"
while(True):
	#lora.close()
	time.sleep(3)
#status = lora.send_to_wait(message, 10, retries=2)
#if status is True:
#    print("Message sent!")
#else:
#    print("No acknowledgment from recipient")
#lora.close()
