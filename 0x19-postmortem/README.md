
## cause and resolution
The platform is served by 2 ubuntu cloud servers. The master server web-01 was connected to serve all requests, and it stopped functioning due to memory outage as a results of so many requests because during a previous test, the client server web-02 was disconnected temporarily for testing and was not connected to the load balancer afterwards. 


The issue was fixed when the master server was temporarily disconnected for memory clean-up then connected back to the loadbalancer and round-robin algorithm was configured so that both the master and client servers can handle equal amount of requests.

## Prevention against such problem in future
- Choose the best loadbalancing algorithm for your programs
- Always keep an eye on your servers to ensure they are running properly
- Have extra back-up servers to prevent your program fro completely going offline during an issue

## Corrective and Preventative Measures

The following corrective and preventative measures have been taken to address the issue and prevent future occurrences:

    A thorough review of configuration changes will be conducted before deployment to identify potential misconfigurations.

    Automated tests will be implemented for load balancer configuration to catch distribution imbalances during the development and testing phases.

    Real-time monitoring and alerting will be enhanced to quickly detect and respond to sudden spikes in error rates and service degradation.

    Clear communication channels will be established for incident escalation to ensure timely involvement of relevant stakeholders.

    Regular training sessions will be conducted for the operations team to improve incident response capabilities and reduce the chances of misleading investigations.

## Tasks to Address the Issue

The following tasks will be completed to address the issue:

    The release process will be reviewed to implement stricter checks on configuration changes before deployment.

    Automated tests will be developed and integrated for load balancer configuration adjustments.

    Monitoring tools will be updated to provide real-time insights into traffic distribution and backend server performance.

    An incident response playbook will be created with predefined escalation paths and clear responsibilities.

    Incident response training will be conducted to ensure all team members understand their roles during service outages.


