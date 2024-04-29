<h1>Mac-Address-Changer</h1>

<ol>
  <li>Shebang:</li>
  <pre>#!/usr/bin/env python</pre>
  <p>This line is called a shebang and is used to specify the interpreter that should be used to run the script. In this case, it indicates that the script should be run using the Python interpreter <b>('python').</b></p> 

  <li>Imports:</li>
<pre>
importsubprocesses
import optparse
</pre>
  <p>These lines import the <b>'subprocess'</b> module, which allows you to spawn new processes, and the <b>'optparse'</b> module, which is used for parsing command-line options.</p>

  <li>Function Definition: <b>mac_changer(interface, mac_addr)</b></li>
  <pre>def mac_changer(interface, mac_addr):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_addr])
    subprocess.call(["ifconfig", interface, "up"])
    print("[+] Changed the MAC address of " + interface + " to " + mac_addr)
  </pre>

  <p>This function <b>'mac_changer'</b> takes two arguments: <b>'interface'</b> (the network interface whose MAC address will be changed) and <b>'mac_addr'</b> (the new MAC address). Inside the function:</p>

  <ul>
    <li>It first brings down the specified network interface using <b>ifconfig interface down</b>.</li>
    <li>Then it sets the new MAC address for the interface using <b>ifconfig interface hw ether mac_addr.</b></li>
    <li>Finally, it brings up the interface using <b>ifconfig interface up.</b></li>
    <li>It prints a message indicating that the MAC address has been changed.</li>
  </ul>

  <li>Function Definition: <b>get_arguments()</b></li>
  <pre>
    def get_arguments():
        parser = optparse.OptionParser()
        parser.add_option("-i", "--interface", dest="interface", help="Network interface you wants to change")
        parser.add_option("-m", "--mac_addr", dest="mac_addr", help="new mac address you wants to replace")
        (options, arguments) = parser.parse_args()
        if not options.interface:
            parser.error("[-] Please specify the interface, use --help for more information")
        elif not options.mac_addr:
            parser.error("[-] Please specify the MAC address, use --help for more information")
        return options
  </pre>
  <p>This function get_arguments is used to parse command-line arguments. It sets up an OptionParser object, defines two options (-i for the interface and -m for the MAC address), and parses the command-line arguments. It returns the options (including the specified interface and MAC address). If either the interface or the MAC address is not provided, it prints an error message.</p>

  <li>Parse Command-Line Arguments:</li>
  <pre>options = get_arguments()</pre>
  <p>This line calls the get_arguments function to parse the command-line arguments and stores the result in the options variable.</p>

  <li>Call <b>'mac_changer'</b> Function:</li>
  <pre>mac_changer(options.interface, options.mac_addr)</pre>
  <p>This line calls the mac_changer function with the interface and MAC address obtained from the command-line arguments. It changes the MAC address of the specified interface using the provided MAC address.</p>
  
  
</ol>
