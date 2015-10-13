Sub Buzz Problem: Design
=========================


Things to consider
------------------

* I would add a "session_id" to the messages so we can indentify events that come from the same user visit
* If there is a way to identify a particular user, I would also add a "user_id" to the messages 
(it's different from "session_id" because a user can load some pages more than once)

With that in mind: NSQ solves the problem of scaling regarding the distribution of the messages,
the more messages we have, more clients can be executed (on one or more servers).
The bottleneck - in addition to bandwidth, which is solved by scaling the NSQ servers - would be
the data storage system of statistics: which they would be written simultaneously by all the clients.

The simplest case would be a scheme in which each desired metric has its own table.
Every consumer processes each message by adding/updating each table separately:

    1. Statistics per item (key in article):
        * Add 1 to the read subbuzzes of the corresponding article
        * Add the time to the corresponding article
    2. Statistics per subbuzz (key in subbuzz+position):
        * Add 1 to the views of the subbuzz (in the current position)
        * Add the time to the corresponding element
    3. Statistics per session (if it was implemented, key in session)
        * Add the time to the corresponding element
        * Add 1 to the number of viewed subbuzz
    4. Statistics per user (if it was implemented, key on user_id)
        * Add the time to the corresponding element
        * Add 1 to the number of viewed subbuzz


This structure is the simplest system but it has concurrency issues.
To avoid them, we could make that every customer has his own version of each of the tables and
there is some kind of periodic process which takes the information from those tables and add them
to the definitive (in a cron for example). In this way we avoid the problem of concurrence on
writing without making the system more complex but increasing the time between when the
event occurs and is reflected/recorded in the system.


We can always generate a more complex architectures using some sort of DataWarehouse as Amazon RedShift
or another provider. We can save in it the last N days of messages and, periodically, add the data
in other tables (like the ones described earlier).


For the visualization, it would take only a simple API that generates queries over the described tables
and return the serialized data (probably in JSON, but it depends on the need) to be used in any kind
of environment as a panel.
Alternatively we could improve this API to run queries a little more complex that analyze several
data simultaneously: such as how to get the most viewed article or get all the statistics of the
subbuzz of an article (so we can plot a relationship between position, visits and time spent on each).
