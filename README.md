Working with celery - Distributed Task Queue

When can we use a task queue?
-It can be used when the work (task) can be run asynchronously.
-In a distributed system context.
-It gives you asymmetric architecture.

What it does?
The task queue distributes work across threads or machines.
Dedicated worker processes constantly monitor task queues to perform new work.
It is highly available as workers and client will automatically retry in the event of connection loss.

How celery works?
By messages. To initiate a task, client adds a message to a queue. The broker then delivers the message to a worker.
A celery system consist of multiple brokers and workers. This gives way to high availability and horizontal scaling.

Celery is written in Python.
It can run on single machine, multiple machines or even across data centers. It has an active and friendly community to support.

What it requires?
It requires message transport to send and receive messages. For e.g. RabbitMQ and Reddis or SQlite for local development.
