import heapq
import math
import collections
class assignment(object):
    actions = {1:[1,0,0], 2:[-1,0,0], 3:[0,1,0], 4:[0,-1,0], 5:[0,0,1], 6:[0,0,-1],
               7:[1,1,0] , 8:[1,-1,0], 9:[-1,1,0],10:[-1,-1,0],
               11:[1,0,1],12:[1,0,-1],13:[-1,0,1],14:[-1,0,-1],
               15:[0,1,1],16:[0,1,-1],17:[0,-1,1],18:[0,-1,-1]}
    non_diags = {1,2,3,4,5,6}
    

    def __init__(self):
        inp = open("input.txt","r")
        algo = inp.readline().strip()
        
        if not algo :
            output = open("output.txt","w")
            output.write("FAIL")

        maxpoints = inp.readline().split()
        max_points = list(map(int,maxpoints))
    
        
        start_points = inp.readline().split()
        start = list(map(int,start_points))
        

        end_points = inp.readline().split()
        end = list(map(int,end_points))

        n = int(inp.readline())
        

        dct = {}
        while n:
            nums = inp.readline().split()
            nums1 = list(map(int,nums))
            
            dct[str(nums1[0:3])] = set(nums1[3:])
            n=n-1
        
        if algo == "BFS":
            
            visited1,end,start = self.BFS(start,end,dct)
            self.BFS_OUTPUT(visited1,end,start)
        elif algo == "UCS":
            
            visited,cost1,end,start = self.UCS(start,end,dct)
            self.UCS_OUTPUT(visited,cost1,end,start)
        else:
            
            visited,cost1,end,start = self.Astar(start,end,dct)
            self.UCS_OUTPUT(visited,cost1,end,start)
        

    def BFS(self,start,end,dct):
        visited = set()
        visited1 = {str(start) : 0}
        dqueue = collections.deque()
        dqueue.append(start)
        while dqueue:
            point = dqueue.popleft()

            if str(point) in dct and str(point) not in visited:
                set1 = dct[str(point)]
                for val in iter(set1):
                    list1 = self.actions[val]
                    temp = [0]*3
                    temp[0] = point[0]+list1[0] 
                    temp[1] = point[1]+list1[1] 
                    temp[2] = point[2]+list1[2]
                    
                    if str(temp)  not in visited1:
                        visited1[str(temp)] = point
                    
                    dqueue.append(temp)
                    if temp == end:
                        return visited1,end,start
            
            visited.add(str(point))

        return visited1,end,start
        

    def BFS_OUTPUT(self,visited1,end,start):
        output = open("output.txt","w")
        stack =[]
        if str(end) not in visited1 :
            output.write(str("FAIL"))

        
        else:
            temp = end
            while visited1[str(temp)]!=0:
                stack.append(temp)
                temp = visited1[str(temp)]
            stack.append(start)

            output.write(str(len(stack)-1))
            output.write("\n")

            output.write(str(len(stack)))
            output.write("\n")
            
            while stack:
                temp1 = stack.pop()
                
                temp2= list(temp1)
                if temp2 != start:
                    temp2.append(1)
                else:
                    temp2.append(0)
                
                output.write(" ".join(map(str,temp2)))
                output.write("\n")

            

    def UCS(self,start,end,dct):
        queue= []
        visited = {str(start) : 0}
        cost1 = {str(start) : 0}
        
        
        queue.append((0,start))
        heapq.heapify(queue)
        
        while queue:
            cost,point = heapq.heappop(queue)
            
            
            if str(point) in dct :
                set1 = dct[str(point)]
                for val in iter(set1):
                    list1 = self.actions[val]
                    
                    temp = [0]*3
                    temp[0] = point[0]+list1[0] 
                    temp[1] = point[1]+list1[1] 
                    temp[2] = point[2]+list1[2]
                    
                    
                    
                    if val not in self.non_diags:
                        temp_cost = 14
                    else:
                        temp_cost = 10

                    if str(temp) not in visited or cost1[str(temp)] > temp_cost+cost:
                        visited[str(temp)] = point
                        cost1[str(temp)] = temp_cost + cost
                        
                        heapq.heappush(queue, (cost+temp_cost, temp))
                    
                    
        return visited,cost1,end,start
    
    def UCS_OUTPUT(self,visited,cost1,end,start):
        output = open("output.txt","w")
        stack = []
        if str(end) not in cost1 :
            output.write(str("FAIL"))
        else:
            output.write(str(cost1[str(end)]))
            output.write("\n")
            temp = end
            while visited[str(temp)]!=0:
                stack.append(temp)
                temp = visited[str(temp)]
            stack.append(start)
            output.write(str(len(stack)))
            output.write("\n")
            
            while stack:
                temp1 = stack.pop()
                
                temp2= list(temp1)
                if temp2 != start:
                    
                    temp2.append(cost1[str(temp2)] - cost1[str(visited[str(temp2)])])
                else:
                    temp2.append(0)
                
                output.write(" ".join(map(str,temp2)))
                output.write("\n")
    
    def Astar(self,start,end,dct):
        queue= []
        visited = {str(start) : 0}
        cost1 = {str(start) : 0}
        
        queue.append((0,start,0))
        heapq.heapify(queue)
        
        while queue:
            heur,point,cost = heapq.heappop(queue)
            
            if str(point) in dct :
                set1 = dct[str(point)]
                for val in iter(set1):
                    list1 = self.actions[val]
                    temp_point = [0]*3
                    temp_point[0] = point[0]+list1[0] 
                    temp_point[1] = point[1]+list1[1] 
                    temp_point[2] = point[2]+list1[2]
                    
                    if val not in self.non_diags:
                        temp_cost = 14
                    else:
                        temp_cost = 10
                    
                    if str(temp_point) not in visited or cost1[str(temp_point)] > temp_cost+cost:
                        visited[str(temp_point)] = point
                        cost1[str(temp_point)] = temp_cost + cost
                        
                        heapq.heappush(queue, (cost+temp_cost + self.heuristic(temp_point,end), temp_point , cost+temp_cost))
                    

        return visited,cost1,end,start
    def heuristic(self,point,end):
        distance = int(math.sqrt( (point[0]-end[0])**2 + (point[1]-end[1])**2 + (point[2]-end[2])**2 ))
        return distance


ass = assignment()
