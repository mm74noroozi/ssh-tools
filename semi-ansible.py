import asyncio
from asyncio.subprocess import PIPE
from yaml import safe_load as load
import logging
import subprocess


logging.basicConfig(format='%(asctime)s - %(name)s: %(message)s',level=logging.INFO)

with open("config.yml","r+") as f:
    obj=load(f.read())
    vms=obj["vms"]
    exec=obj["exec"]
    target=exec["target"]
    commands=exec["commands"]



async def run_commands(vm,commands):
    logger=logging.getLogger(vm["name"])
    sshProcess = subprocess.Popen(f"ssh -tt root@{vm['host']} -p {vm['port']}",shell=True,stdin=subprocess.PIPE,stdout = subprocess.PIPE)
    for command in commands:
        logger.info("->"+command)
        logger.info(sshProcess.communicate(input=command.encode())[0].decode('utf8'))

async def main():
    jobs=[asyncio.create_task(run_commands(vm,commands)) for vm in vms if target in vm["tags"]]
    await asyncio.gather(*jobs)

if __name__ == "__main__":
    asyncio.run(main())
