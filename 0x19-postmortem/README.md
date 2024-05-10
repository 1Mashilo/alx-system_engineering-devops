iPostmortem: E-commerce Website Checkout Outage (Invented Scenario)
Issue Summary
Duration: Thursday, May 9, 2024, 17:30 PST - Friday, May 10, 2024, 01:00 PST (7.5 hours)
Impact: The e-commerce website's checkout process was unavailable during the outage window. Users attempting to purchase items encountered errors and were unable to complete their transactions. This is estimated to have impacted approximately 20% of website visitors during peak evening hours, resulting in lost sales and customer frustration.
Root Cause: A database connection pool configuration error led to an unexpected database connection spike, overwhelming the database server and causing it to crash.
Timeline
17:30 PST: Monitoring alerts indicated a significant increase in database connection errors on the e-commerce website.
17:35 PST: The engineering team investigated the alerts and observed a surge in failed checkout transactions.
17:40 PST: Initial suspicion fell on the payment gateway due to the checkout errors. The team contacted the payment gateway provider but they confirmed their service was operational.
18:00 PST: Further investigation revealed the database server was overloaded and unresponsive.
18:15 PST: The incident was escalated to the database administration team.
18:30 PST: The database team identified a misconfiguration in the connection pool settings, allowing a much higher number of concurrent connections than intended.
20:00 PST: A temporary fix was implemented by adjusting the connection pool size to a more appropriate value. The database server recovered and checkout functionality was restored.
23:00 PST: A permanent configuration change was implemented to prevent future occurrences.
01:00 PST: The engineering team confirmed system stability and cleared the incident.
Root Cause and Resolution
The root cause of the outage was a misconfigured database connection pool. The pool was allowing a much higher number of concurrent connections than the database server could handle effectively. This surge in connections overloaded the database server, causing it to crash and become unresponsive.
The issue was resolved by:
Temporary Fix (20:00 PST): Adjusting the connection pool size to a lower value allowed the database server to recover and resume operations.
Permanent Fix (23:00 PST): A permanent configuration change was implemented to set the connection pool size to a more appropriate value based on expected load. This will prevent future occurrences of connection overload.
Corrective and Preventative Measures
Review and update database configuration documentation: The connection pool configuration error highlights the need for thorough documentation and regular review of critical system configurations.
Implement automated monitoring: Automated monitoring for database connection pool metrics and server health can provide early warnings of potential issues before they cause outages.
Database performance tuning: The database server should be regularly analyzed and optimized to ensure it can handle expected traffic volume.
Conduct code reviews: Code review processes should emphasize infrastructure configuration management to identify potential issues before deployment.
This postmortem outlines the cause and resolution of the e-commerce website checkout outage. By implementing the corrective and preventative measures outlined above, we aim to improve system resiliency and prevent similar incidents in the future.


