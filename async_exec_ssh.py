from asyncio import create_subprocess_exec
socksClient= create_subprocess_exec.Popen("ssh -D1080 -N root@domain1.example.com -p2223",stderr=PIPE)
socksClient.wait()
print(socksClient.stdout)
