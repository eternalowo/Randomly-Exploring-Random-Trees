<h1>Rapidly Exploring Random Trees Algorithm</h1>

Let's assume that we have some mobile robot which is material point with coordinates q_init(x, y), as well as a point q_end(x, y), to which it needs to get.

![smth](https://user-images.githubusercontent.com/98911288/205058003-86ce326b-2241-46b7-b436-da4a1c7084f0.png)
\
\
Also let's assume that we can have some rectangle obstacles on our way, which robot should get around passing them.

![smth](https://user-images.githubusercontent.com/98911288/205058687-8c6d8b0b-e09d-4ac1-9c07-87195ec7c6aa.png)
\
\
So our goal is to find the shortest path that our robot can follow in order to get in q_end point.

![smth](https://user-images.githubusercontent.com/98911288/205059429-48399216-6723-495a-b693-73d72827838a.png)
\
\
Robot configuration - is a set of characteristics which defines position of our robot. Since we have only x and y, our space of configurations С is 2D plane with x and y axis', so we can break down our space of configurations to Cfree (configuration space that robot can be located in) and Cobs (configuration space in which robot can't be located)

![smth_w](https://user-images.githubusercontent.com/98911288/205062382-a5605820-d3b0-4185-82cb-998ebb857d33.png)
\
\
Since in our configuration space the robot configuration is a material point, the problem of finding the shortest path is reduced to the problem of searching in С the shortest curve/polyline lying completely in Cfree and connecting the initial and final configurations of q_init and q_goal.

![smth_w](https://user-images.githubusercontent.com/98911288/205066096-dd8f248a-d11e-4eda-a5b2-8ad0db8f1b2e.png)
\
\
So, in order to find path we will be using method that based on random samples which is Randomly Exploring Random Trees (RRT)
In this method we will be building tree from our q_init that will fill Cfree. After buiding this tree we will add an q_end into it and we will search for the shortest path from q_init to q_end.

![image](https://user-images.githubusercontent.com/98911288/205068756-7439bd7a-2bcd-479e-8f5a-96f06c6bd264.png)
\
\
Well, how RRT works?
In this algorithm we will be using some auxiliary functions, such as:
function: nearest(G, Point) - returns the vertex from graph G closest to the Point configuration. If it turns out that the point is close not to one vertex, but to an edge (that is, that the configuration closest to the point lies on the edge of the graph), then at this point the edge is divided into two parts and a new vertex is added to the graph, which then returns.
\
\
Closest configuration is a vertex of graph:
![case](https://user-images.githubusercontent.com/98911288/205071480-d64a0859-a8dd-4252-a877-5d76e9a3073e.png)
\
\
Closest configuration is lying on edge of graph:
![case](https://user-images.githubusercontent.com/98911288/205072108-2966cfd2-406f-4a04-b0ba-b0c952fe8fda.png)
\
\
