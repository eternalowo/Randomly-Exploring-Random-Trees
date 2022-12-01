<h1>Rapidly Exploring Random Trees Algorithm</h1>

Let's assume that we have some mobile robot which is material point with coordinates q_init(x, y), as well as a point q_end(x, y), to which it needs to get.

![smth](https://user-images.githubusercontent.com/98911288/205058003-86ce326b-2241-46b7-b436-da4a1c7084f0.png)
\
\
\
\
Also let's assume that we can have some rectangle obstacles on our way, which robot should get around passing them.

![smth](https://user-images.githubusercontent.com/98911288/205058687-8c6d8b0b-e09d-4ac1-9c07-87195ec7c6aa.png)
\
\
\
\
So our goal is to find the shortest path that our robot can follow in order to get in q_end point.

![smth](https://user-images.githubusercontent.com/98911288/205059429-48399216-6723-495a-b693-73d72827838a.png)
\
\
\
\
Robot configuration - is a set of characteristics which defines position of our robot. Since we have only x and y, our space of configurations is 2D plane with x and y axis', so we can break down our space of configurations to Cfree (configuration space that robot can be located in) and Cobs (configuration space in which robot can't be located)

![smth_w](https://user-images.githubusercontent.com/98911288/205062382-a5605820-d3b0-4185-82cb-998ebb857d33.png)
