from easysnmp import *
from datetime import *
from tabulate import *

def main():

        choose = input("""
Main menu

        1: RUN
        2: EXIT
        
Write the option: """)

        if choose == 1 :
                print('')
                print("Type the IP address:")
                print('')
                ip = raw_input()
                print('')
                print("Type the port number:")
                print('')
                ports = raw_input()
                print('\n' *2)
                community_name="public"

                process=".1.3.6.1.2.1.25.4.2.1.2"
                cpu=".1.3.6.1.2.1.25.5.1.1.1"
                memory=".1.3.6.1.2.1.25.5.1.1.2"

                now= datetime.now()
                time= now.strftime("%A,%d %B,%Y --- %H:%M:%S ---")

                monitor = []

                session = Session(hostname=ip, community=community_name, version=2)
                mon = session.walk([process, cpu, memory])
                i = 0
                for item in mon:
                        if i % 3 == 0:
                            monitor.append('{oid_index}'.format(
                                oid_index=item.oid_index))
                        monitor.append('{value}'.format(value=item.value))
                        i += 1
                monitor = [monitor[x:x+4] for x in range(0, len(monitor), 4)]


                print('')
                print(tabulate(monitor, headers=["PID", "PROCCESS", "CPU", "MEMORY"], tablefmt="grid"))
                print('')
                print('CURRENT DATE AND TIME:')
                print('')
                print(time)                
                main ()

        elif choose == 2 :
                print('\nEND!!!!!!')
        else:
                print('\nERROR \n')

if __name__== "__main__":
    main()