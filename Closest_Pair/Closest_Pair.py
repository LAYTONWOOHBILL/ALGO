import math

class Point:

    """Summary of class here.

    Create a class Point with xcoord and ycoord

    Attributes:
        __repr__: A boolean indicating if we like SPAM or not.
        __gt__: Compare two point xcoord and ycoord, first on ycoord then xcoord
        __lt__: Compare two point xcoord and ycoord, first on ycoord then xcoord
        __eq__: Compare two point have same xcoord and ycoord
    """
    def __init__(self,xcoord=0,ycoord=0):
        # attributes xcoord and ycoord for a Point
        self.x = xcoord
        self.y = ycoord

    def __repr__(self):
        # representation of Point class objects
        return "Point({}, {})".format(self.x,self.y)

#readfile and add point into list
def addpoints(points,file):

    """readfile and add point into list

    Args:
        points: Empty list
        file: external file

    Returns:
        a pointlist with point been add
        example:
            [Point(0, 5), Point(-1, 3), Point(2, 4), Point(0, 0), Point(-1, -1), Point(2, 0), Point(1, -2)]

    Raises:
      if readline error

    """
    f = open(file, "r")                                 # open file
    line = f.readline()                                 # readline

    while line:                                         # while can read line do

        try:                                            # try
            line = line.split(" ")                          # ['0', '5\n']
            line[1] = line[1].rstrip("\n")                  # drop '\n'
            point = Point(eval(line[0]),eval(line[1]))      # cast str to int or float
            points.append(point)                            # append in list
            line = f.readline()                             # read next line
        except:                                         # raises error
            print("Error")                                  # print

    return


def Pre_Algo(points):

    """Sort points in list by x.xcoord

    Args:
        points: list

    Returns:
    
    increasing order by x.xcoord point list
       
    """
    points_x_sort_list = list(points)
    points_x_sort_list.sort(key=lambda Point:Point.x)

    return points_x_sort_list 


def distance(point_a,point_b):
    """return two points distance

    Args:
        point_a: point
        point_b: point

    Returns:
       two points distance

    """
    return math.sqrt((point_a.x-point_b.x)**2+(point_a.y-point_b.y)**2)


def brute_force(points,first,last):

    """return two points with the min distance in points list

    Args:
        points: list
        first: start index of the list
        last:  end index of the list

    Returns:
        min_pointa,min_pointb,min_dis
       
    """
    
    # set first two points with min_points, since points list is greater than 2
    i = first 
    j = i+1
    min_pointa=i
    min_pointb=j
    min_dis = float('inf')                              # min_distance is always 
    for i in range(last-1):                             #(0,1),(0,2),(1,2)
        for j in range(last):
            if i != j:                                  # not doing (0,0),(1,1)
                temp_dis=distance(points[i],points[j])
                if temp_dis < min_dis:                  #if new distance is less than min distance,assign 
                    min_dis = round(temp_dis,9)             
                    min_pointa = i
                    min_pointb = j
            
    return min_pointa,min_pointb,min_dis


def Closest_Pair_Algo(points,first,last):
    
    """  Closest_Pair_Algo

     less than 3 points - brute force
     
     Compute separation line L such that half the points are on one side and half on the other side.   //O(n log n)
 
     δ1 = Closest-Pair(left half)       //2T(n / 2)
     δ2 = Closest-Pair(right half)
     δ = min(δ1, δ2)

     Delete all points further than δ from separation line L   //O(n)

     Sort remaining points by y-coordinate. //O(n log n)

     Scan points in y-order and compare distance between each point and next 1   1 neighbors. If any of these distances is less than δ, update δ. //O(n)
 
     return δ.

    """
    
    # 1. if |S| ≤ 3 return a closes pair (pmin, qmin) in S by brute force;
    if (last-first) <= 3:
         return brute_force(points,first,last)

    # split points in two half and assign the vertical line D of equation x = ℓ
    mid = (first+last)//2
    x_l = points[mid].x
    
    points_left=points[:mid]
    points_right=points[mid+1:]
    
    #recurse on left side to compute a closest pair and then right side
    min_left_pointa,min_left_pointb,min_left_dis= Closest_Pair_Algo(points_left,0,len(points_left)) #left
    min_right_pointa,min_right_pointb,min_right_dis= Closest_Pair_Algo(points_right,0,len(points_right)) #right

    #assign the min points and distance
    if min_left_dis < min_right_dis:
        min_delta_distance = min_left_dis
        min_pointa = min_left_pointa
        min_pointb = min_left_pointb
    else:
        min_delta_distance = min_right_dis
        min_pointa = min_right_pointa
        min_pointb = min_right_pointb

    #find the mid region points that in the two side of min distance with vertical line x 
    region_points=[]
    for i in range(last-1):
        if (x_l-min_delta_distance) < points[i].x < (x_l+min_delta_distance):
            region_points.append(points[i])
            
    # sorted region points by y.coord
    region_points.sort(key=lambda Point:Point.y)
    

    if len(region_points)<2: #Since less than two points in the bewteen line so we don't need to check
        return min_pointa, min_pointb, min_delta_distance
    
    else:
        # we brute_force find the min distance and two points 
        min_region_pointa,min_region_pointb,min_region_point_dis = brute_force(region_points,0,len(region_points))
        
        if min_region_point_dis < min_delta_distance:  #if region points has smaller distance we resign them to min points 
            min_delta_distance = min_region_point_dis
            min_pointa = min_region_pointa
            min_pointb = min_region_pointb
        
        return min_pointa, min_pointb, min_delta_distance

def main():

    print("#Author: Wilson Wu\n#Date:2021.05.7\n#StudentID:1939700\n")
    
    file_list = ['10points.txt','100points.txt','1000points.txt']

    for file in file_list:
        points = list()                                                             # create an empty list for puting point
        addpoints(points,file)
        points_x_sort_list = Pre_Algo(points)
        min_pointa, min_pointb, min_delta_distance = Closest_Pair_Algo(points_x_sort_list,0,len(points_x_sort_list))
        print(file+" test file: \n\nThe minimum distance is: \n")
        print("{}: {}<---> {}\n".format(min_delta_distance,points[min_pointa],points[min_pointb]))
        print("="*60+"\n")
if __name__ == "__main__":
    main()
