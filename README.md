## Test of setup for running long background jobs

The goal is to have a flask application in elastic beanstalk that sends jobs to an AWS SQS queue. This jobs should be
retrieved by workers (running on other EC2 instances) and executed.

The setup here seems to work but when sending a task, e.g. by visiting `localhost:5000/do_work/5`, the call to
`send_task` in this route doesn't work as no job appear in the queue. The code is based on [this
repository](https://github.com/yccheok/celery-hello-world).

Logs when running the containes and visiting `localhost:5000/do_work/5`:

**flask**

```shell
flask      |  * Serving Flask app 'app'
flask      |  * Debug mode: on
flask      | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI
server instead.
flask      |  * Running on all addresses (0.0.0.0)
flask      |  * Running on http://127.0.0.1:5000
flask      |  * Running on http://172.21.0.2:5000
flask      | Press CTRL+C to quit
flask      |  * Restarting with stat
flask      |  * Debugger is active!
flask      |  * Debugger PIN: 105-859-236
flask      | 172.21.0.1 - - [07/Apr/2023 09:47:11] "GET /do_work/5 HTTP/1.1" 200 -
```


**earning**

```shell
earning    | /usr/local/lib/python3.11/site-packages/celery/platforms.py:840: SecurityWarning: You're running the
worker with superuser privileges: this is
earning    | absolutely not recommended!
earning    |
earning    | Please specify a different user using the --uid option.
earning    |
earning    | User information: uid=0 euid=0 gid=0 egid=0
earning    |
earning    |   warnings.warn(SecurityWarning(ROOT_DISCOURAGED.format(
earning    |
earning    |  -------------- celery@716a207ad867 v5.2.7 (dawn-chorus)
earning    | --- ***** -----
earning    | -- ******* ---- Linux-6.2.9-arch1-1-x86_64-with 2023-04-07 09:46:58
earning    | - *** --- * ---
earning    | - ** ---------- [config]
earning    | - ** ---------- .> app:         earning:0x7f5fb7981510
earning    | - ** ---------- .> transport:   sqs://ABCDEFGHIJKLMNOPQRST:**@localhost//
earning    | - ** ---------- .> results:
earning    | - *** --- * --- .> concurrency: 12 (prefork)
earning    | -- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
earning    | --- ***** -----
earning    |  -------------- [queues]
earning    |                 .> earning          exchange=earning(direct) key=earning
earning    |
earning    |
```
