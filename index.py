#!/usr/bin/env python
# coding: utf-8

# In[1]:


import copy

Z = 0
decision_vars = []

class backpack_object:
    def __init__(self, p, c):
        self.pi = p
        self.ci = c
 
    def __repr__(self):
        return '{' + str(self.pi) + ', ' + str(self.ci) + '}'

### question 4
class node : 
    def __init__(self,fixed_vars):
        self.fixed_vars = fixed_vars
        self.decision_vars = []
        self.z = None
        self.left = None
        self.right = None
    
    ### question 3 évaluation
    def evaluate(self) :
        decision_vars = []
        left_pi = max_pi
        z = 0

        for i in range(len(backpack_objects)): 
            try : 
                if self.fixed_vars[i] == 1 : 
                    if backpack_objects[i].pi > left_pi : 
                        return
                    left_pi -= backpack_objects[i].pi
                    z +=  backpack_objects[i].ci
                decision_vars.append(self.fixed_vars[i])
            except :
                break            


        for object in backpack_objects[len(self.fixed_vars):] : 
            if object.pi <= left_pi : 
                decision_vars.append(1)
                left_pi -= object.pi
                z +=  object.ci
            
            else :
                decision_vars.append(0)
        self.decision_vars = decision_vars
        self.z = z

    ### question 3 séparation
    def separate(self) : 
        if len(self.fixed_vars) != len(self.decision_vars) : 
            
            left_vars  = copy.deepcopy(self.fixed_vars)
            right_vars = copy.deepcopy(self.fixed_vars)

            left_vars.append(1)
            right_vars.append(0)
            self.left = node(left_vars)
            self.right = node(right_vars)
        else : 
            pass
        
    def execute(self) : 
        self.evaluate()
        if self.z is None : 
            return
        if self.z >= Z : 
            update_borne(self.z, self.decision_vars)
            
            self.separate()
            if self.left is not None : 
                self.left.execute()
            if self.right is not None : 
                self.right.execute()
        
    def __repr__(self):
        left_part = ""
        right_part = ""
        if self.left is not None : 
            left_part = self.left
        if self.right is not None : 
            right_part = self.right

        return '\n{' + str(self.z) + ', ' + str(self.decision_vars) + '}\n left : '+str(left_part)+'\n right : '+str(right_part)


### question 1
def sorting (backpack_objects) : 
    backpack_objects.sort(key=lambda x:(x.ci/x.pi), reverse=True)

### question 2
def initial_solution(backback_objects) : 
    decision_vars = []
    left_pi = max_pi
    z = 0

    for object in backback_objects : 
        if object.pi <= left_pi : 
            decision_vars.append(1)
            left_pi = left_pi - object.pi
            z += object.ci
        else :
            decision_vars.append(0)
        
    return decision_vars, z

def update_borne(z, vars) : 
    global Z
    global decision_vars

    Z = z
    
    decision_vars = vars

def filter_fixed(value):
    
    return value == 1


backpack_objects = []

max_pi = 0


def main():

    ### params : 
    global decision_vars
    global z 
    global backpack_objects 
    global max_pi 

    typing = True

    while typing : 
        try : 
         
            backpack_objects = [
                backpack_object(6,12),
                backpack_object(3,8),
                backpack_object(9,20),
                backpack_object(5,9),
                backpack_object(3,6),
                backpack_object(7,16),
            ]
            max_pi = 17

            sorting(backpack_objects)
            decision_vars,z = initial_solution(backpack_objects)

            update_borne(z,decision_vars)

            root_node = node([])

            ### 5
            root_node.execute()

            print('\n la solution de P est : ')
            print('\n Z: ', Z)
            print("\n xi : ", decision_vars)
            typing =False
        except : 
            print("\nVeuillez saisir un nombre entier\n")
            pass


main()


# In[ ]:




