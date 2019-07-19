import argparse
import nmap

def nmapScan(target_host, target_port):
  port_scanner = nmap.PortScanner()
  port_scanner.scan(target_host, target_port)
  state = port_scanner[target_host]['tcp'][int(target_port)]['state']
  print(" [*] " + target_host + " TCP/" + target_port + " " + state)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('-H', dest='target_host', type=str, help='specify target host', required=True)
  parser.add_argument('-p', dest='target_ports', type=str, nargs='+', help='specify target ports separated by a space', required=True)

  args = parser.parse_args()

  target_host = args.target_host
  target_ports = args.target_ports
  
  for target_port in target_ports:
    nmapScan(target_host, target_port)

if __name__ == "__main__":
  main()