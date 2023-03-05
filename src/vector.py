from math import *


def angle(vect1, vect2):                                                # angle in radians
    vect1 = normalize(vect1)
    #print "vect2 is", vect2
    vect2 = normalize(vect2)
    alfa = acos(dot_prod(vect1,vect2)) 
    return alfa
    
def normalize(vector):                                                  # same vector with length 1
    leng = length(vector)
    return (vector[0]/leng, vector[1]/leng, vector[2]/leng)
    pass
    
def length(vect):                                                       # length of vector
	return sqrt((vect[0]*vect[0])+(vect[1]*vect[1])+(vect[2]*vect[2]))+0.0

def cross_prod(vect1, vect2):                                           # cross product (a 'x' b = n)
    norm = []
    norm.append(vect1[1]*vect2[2]-vect1[2]*vect2[1])
    norm.append(vect1[2]*vect2[0]-vect1[0]*vect2[2])
    norm.append(vect1[0]*vect2[1]-vect1[1]*vect2[0])
    return norm

def get_normal(vect1,vect2):                                            # get the normal between 2 vectors
    return normalize(cross_prod(vect1, vect2))

def dot_prod(vect1,vect2):                                              # dot product (a 'dot' b = len(a)*len(b)*cos(v))
	return vect1[0]*vect2[0]+vect1[1]*vect2[1]+vect1[2]*vect2[2]        # (angle = 0     <=>     dot_prod = 0)

def sub(v1, v2):
    return (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])
    
def add(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2])


if __name__ == "__main__":
    def main():
        print(2*angle((1,0,0),(0,1,0)), "is pi")
        print(angle((1,0,0),(6,0,0)), "is zero")
        print(normalize((1,1,1)))
        print(normalize((1,0,0)))
        print(length(normalize((1,1,1))))
        print(cross_prod((1,1,1), (1,1,0)))
        print(get_normal((1,1,1), (1,1,0)))
        print(dot_prod((1,1,1),(1,1,0)))
    main()


