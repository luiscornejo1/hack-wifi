import wifi

def scan_wifi_networks():
    wifi_scanner = wifi.WiFi()
    networks = wifi_scanner.scan()
    
    print("Redes WiFi encontradas:")
    for network in networks:
        print("SSID:", network.ssid)
        print("BSSID:", network.bssid)
        print("Señal:", network.signal)
        print("-----------")
        
scan_wifi_networks()